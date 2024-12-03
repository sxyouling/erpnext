# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestBulkTransactionLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestBulkTransactionLog(UnitTestCase):
	"""
	Unit tests for BulkTransactionLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestBulkTransactionLog(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
