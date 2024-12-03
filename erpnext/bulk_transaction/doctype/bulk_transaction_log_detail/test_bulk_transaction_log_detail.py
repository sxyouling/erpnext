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
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
