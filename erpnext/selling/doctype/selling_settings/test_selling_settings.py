# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

import frappe


class TestSellingSettings(unittest.TestCase):
=======
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestSellingSettings(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	def test_defaults_populated(self):
		# Setup default values are not populated on migrate, this test checks
		# if setup was completed correctly
		default = frappe.db.get_single_value("Selling Settings", "maintain_same_rate_action")
		self.assertEqual("Stop", default)
