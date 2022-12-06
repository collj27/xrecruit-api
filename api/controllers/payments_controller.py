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


@payments_controller_bp.route('/checkout', methods=['GET'])
def get_checkout_session():
    confirmation_url = os.environ['CORS_ORIGINS'] + "/paymentConfirmation"
    cancel_url = os.environ['CORS_ORIGINS']  # TODO: parametize this


    session = stripe.checkout.Session.create(
        line_items=[{
            'price': 'price_1M71PeDKqvpH79kR5FkDuNSb',
            # TODO: parametize price id, https://dashboard.stripe.com/test/products/prod_Mqir77Y217YkBm
            'quantity': 1,
        }],
        mode='payment',
        success_url=confirmation_url,
        cancel_url=cancel_url,
        payment_intent_data={
            'application_fee_amount': 123,
            'transfer_data': {
                'destination': 'acct_1MBkb7D5sbHtwsvg'
                # TODO: parametize account id (destination), https://dashboard.stripe.com/test/connect/accounts/overview
            },
        },
    )

    return json.dumps(session.url)
