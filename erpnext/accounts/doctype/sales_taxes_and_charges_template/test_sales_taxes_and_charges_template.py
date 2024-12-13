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
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	pass
