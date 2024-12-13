import unittest

import frappe
<<<<<<< HEAD
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)

import erpnext


@erpnext.allow_regional
def test_method():
	return "original"


<<<<<<< HEAD
class TestInit(unittest.TestCase):
=======
class TestInit(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
