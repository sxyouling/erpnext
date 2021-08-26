# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

<<<<<<< HEAD
=======
import stripe

>>>>>>> 16eed07a0f (fix: use Stripe's Price API for plan-price information (#26107))
import frappe
import stripe
from frappe import _
from frappe.integrations.utils import create_request_log


def create_stripe_subscription(gateway_controller, data):
	stripe_settings = frappe.get_doc("Stripe Settings", gateway_controller)
	stripe_settings.data = frappe._dict(data)

	stripe.api_key = stripe_settings.get_password(fieldname="secret_key", raise_exception=False)
	stripe.default_http_client = stripe.http_client.RequestsClient()

	try:
		stripe_settings.integration_request = create_request_log(stripe_settings.data, "Host", "Stripe")
		stripe_settings.payment_plans = frappe.get_doc(
			"Payment Request", stripe_settings.data.reference_docname
		).subscription_plans
		return create_subscription_on_stripe(stripe_settings)

	except Exception:
		frappe.log_error(frappe.get_traceback())
<<<<<<< HEAD
		return {
			"redirect_to": frappe.redirect_to_message(
				_("Server Error"),
				_(
					"It seems that there is an issue with the server's stripe configuration. In case of failure, the amount will get refunded to your account."
				),
			),
			"status": 401,
=======
		return{
			"redirect_to": frappe.redirect_to_message(
				_('Server Error'),
				_("It seems that there is an issue with the server's stripe configuration. In case of failure, the amount will get refunded to your account.")
			),
			"status": 401
>>>>>>> 16eed07a0f (fix: use Stripe's Price API for plan-price information (#26107))
		}


def create_subscription_on_stripe(stripe_settings):
	items = []
	for payment_plan in stripe_settings.payment_plans:
		plan = frappe.db.get_value("Subscription Plan", payment_plan.plan, "product_price_id")
		items.append({"price": plan, "quantity": payment_plan.qty})

	try:
		customer = stripe.Customer.create(
			source=stripe_settings.data.stripe_token_id,
			description=stripe_settings.data.payer_name,
<<<<<<< HEAD
			email=stripe_settings.data.payer_email,
=======
			email=stripe_settings.data.payer_email
>>>>>>> 16eed07a0f (fix: use Stripe's Price API for plan-price information (#26107))
		)

		subscription = stripe.Subscription.create(customer=customer, items=items)

		if subscription.status == "active":
<<<<<<< HEAD
			stripe_settings.integration_request.db_set("status", "Completed", update_modified=False)
			stripe_settings.flags.status_changed_to = "Completed"

		else:
			stripe_settings.integration_request.db_set("status", "Failed", update_modified=False)
			frappe.log_error("Subscription N°: " + subscription.id, "Stripe Payment not completed")
	except Exception:
		stripe_settings.integration_request.db_set("status", "Failed", update_modified=False)
=======
			stripe_settings.integration_request.db_set('status', 'Completed', update_modified=False)
			stripe_settings.flags.status_changed_to = "Completed"

		else:
			stripe_settings.integration_request.db_set('status', 'Failed', update_modified=False)
			frappe.log_error('Subscription N°: ' + subscription.id, 'Stripe Payment not completed')
	except Exception:
		stripe_settings.integration_request.db_set('status', 'Failed', update_modified=False)
>>>>>>> 16eed07a0f (fix: use Stripe's Price API for plan-price information (#26107))
		frappe.log_error(frappe.get_traceback())

	return stripe_settings.finalize_request()
