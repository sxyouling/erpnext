# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestProcessPaymentReconciliation(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestProcessPaymentReconciliation(UnitTestCase):
	"""
	Unit tests for ProcessPaymentReconciliation.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestProcessPaymentReconciliation(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	pass
