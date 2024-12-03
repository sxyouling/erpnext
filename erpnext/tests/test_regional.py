import unittest

import frappe
<<<<<<< HEAD
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 329d14957b (fix: validate negative qty)

import erpnext


@erpnext.allow_regional
def test_method():
	return "original"


<<<<<<< HEAD
class TestInit(unittest.TestCase):
=======
class TestInit(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
