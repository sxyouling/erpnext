import unittest

import frappe
<<<<<<< HEAD
=======
from frappe.tests import IntegrationTestCase
>>>>>>> da09316d4c (fix: precision check for salvage value)

import erpnext


@erpnext.allow_regional
def test_method():
	return "original"


<<<<<<< HEAD
class TestInit(unittest.TestCase):
=======
class TestInit(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
