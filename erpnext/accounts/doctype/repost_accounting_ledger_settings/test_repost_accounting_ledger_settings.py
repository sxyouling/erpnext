# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestRepostAccountingLedgerSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestRepostAccountingLedgerSettings(UnitTestCase):
	"""
	Unit tests for RepostAccountingLedgerSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestRepostAccountingLedgerSettings(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	pass
