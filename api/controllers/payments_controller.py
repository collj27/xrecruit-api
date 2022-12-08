import json
import os

from flask import Blueprint
from api.db_models.player import db, Player
import stripe

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

# create blueprint
payments_controller_bp = Blueprint('payments_controller', __name__)


@payments_controller_bp.route('/payments/<name>', methods=['GET', 'POST'])
def create_stripe_express_account(name):
    print(name)
    account = stripe.Account.create(type="express")
    account_link = stripe.AccountLink.create(
        account=account.id,
        refresh_url="https://example.com/reauth",
        return_url="https://example.com/return",
        type="account_onboarding",
    )

    print(account_link.url)

    return "it worked!"


@payments_controller_bp.route('/checkout/<name>/<dollar_amount>', methods=['GET'])
def get_checkout_session(name, dollar_amount):
    # TODO: listen to completion events, https://stripe.com/docs/webhooks/quickstart

    # create price data object
    price_data = {
        'currency': "USD",
        'unit_amount_decimal': int(dollar_amount) * 100,  # convert dollar amount to cents
        'product_data': {
            'name': "Donate",
            'description': "To " + name
        }
    }

    # create payment intent object
    payment_intent_data = {
        'application_fee_amount': 123,
        'transfer_data': {
            'destination': "acct_1MBkb7D5sbHtwsvg"
            # TODO: parametize account id (destination), https://dashboard.stripe.com/test/connect/accounts/overview
        },
    }

    # create session
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': price_data,
            'quantity': 1
        }],
        mode='payment',
        success_url=os.environ['CORS_ORIGINS'] + "/paymentConfirmation",
        cancel_url=os.environ['CORS_ORIGINS'],
        payment_intent_data=payment_intent_data
    )

    return json.dumps(session.url)
