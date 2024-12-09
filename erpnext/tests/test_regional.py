import unittest

import frappe
<<<<<<< HEAD
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)

import erpnext


@erpnext.allow_regional
def test_method():
	return "original"


<<<<<<< HEAD
class TestInit(unittest.TestCase):
=======
class TestInit(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
