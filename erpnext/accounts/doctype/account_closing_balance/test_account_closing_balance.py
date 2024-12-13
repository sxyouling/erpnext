# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAccountClosingBalance(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestAccountClosingBalance(UnitTestCase):
	"""
	Unit tests for AccountClosingBalance.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAccountClosingBalance(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	pass
