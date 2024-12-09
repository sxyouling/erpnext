# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestRepostPaymentLedger(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestRepostPaymentLedger(UnitTestCase):
	"""
	Unit tests for RepostPaymentLedger.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestRepostPaymentLedger(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	pass
