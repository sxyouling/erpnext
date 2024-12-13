# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestBulkTransactionLogDetail(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestBulkTransactionLogDetail(UnitTestCase):
	"""
	Unit tests for BulkTransactionLogDetail.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestBulkTransactionLogDetail(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	pass
