# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

import frappe

test_records = frappe.get_test_records("Sales Taxes and Charges Template")


class TestSalesTaxesandChargesTemplate(unittest.TestCase):
=======
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestSalesTaxesandChargesTemplate(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	pass
