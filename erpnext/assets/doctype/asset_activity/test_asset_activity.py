# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAssetActivity(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestAssetActivity(UnitTestCase):
	"""
	Unit tests for AssetActivity.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAssetActivity(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	pass
