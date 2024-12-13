# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestLedgerHealthMonitor(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestLedgerHealthMonitor(UnitTestCase):
	"""
	Unit tests for LedgerHealthMonitor.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestLedgerHealthMonitor(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	pass
