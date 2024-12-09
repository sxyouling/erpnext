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
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
