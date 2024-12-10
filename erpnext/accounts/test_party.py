import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> da09316d4c (fix: precision check for salvage value)

from erpnext.accounts.party import get_default_price_list


<<<<<<< HEAD
class PartyTestCase(FrappeTestCase):
=======
class PartyTestCase(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	def test_get_default_price_list_should_return_none_for_invalid_group(self):
		customer = frappe.get_doc(
			{
				"doctype": "Customer",
				"customer_name": "test customer",
			}
		).insert(ignore_permissions=True, ignore_mandatory=True)
		customer.customer_group = None
		customer.save()
		price_list = get_default_price_list(customer)
		assert price_list is None
