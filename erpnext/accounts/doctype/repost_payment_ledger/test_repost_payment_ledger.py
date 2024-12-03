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
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
