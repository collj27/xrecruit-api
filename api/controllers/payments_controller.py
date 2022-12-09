import json
import os
import asyncio

from flask import Blueprint, request, jsonify

from api.models.payment import Payment
from api.models.player import db, Player
import stripe

stripe.api_key = os.environ['STRIPE_SECRET_KEY']
endpoint_secret = os.environ['STRIPE_ENDPOINT_SECRET']

# create blueprint
payments_controller_bp = Blueprint('payments_controller', __name__)


@payments_controller_bp.route('/webhook', methods=['POST'])
def webhook():
    payload = request.data

    try:
        event = json.loads(payload)
    except stripe.error as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return jsonify(success=False)

    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('Webhook signature verification failed.' + str(e))
            return jsonify(success=False)

    if event['type'] == 'payment_intent.succeeded' or event['type'] == 'payment_intent.payment_failed':
        # customer payment succeeds
        payment_intent = event['data']['object']
        commit_payment(payment_intent)

    return jsonify(success=True)


def commit_payment(payment_intent):
    payment = Payment(
        payment_id=payment_intent['id'],
        dollar_amount=payment_intent['amount'] / 100,  # convert to dollars
        is_successful=True if payment_intent['status'] == "succeeded" else False,
        destination_account_id=payment_intent['transfer_data']['destination'],
        player_id=payment_intent['metadata']['player_id'] if 'player_id' in payment_intent['metadata'] else None,
        user_id=payment_intent['metadata']['user_id'] if 'user_id' in payment_intent['metadata'] else None
    )
    db.session.add(payment)
    db.session.commit()


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
        'metadata': {
            'player_id': 1,
            #'user_id': None # only add user id if provided
        }
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
