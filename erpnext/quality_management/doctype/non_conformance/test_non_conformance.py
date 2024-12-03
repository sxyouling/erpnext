# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

# import frappe
import unittest


class TestNonConformance(unittest.TestCase):
=======
# import frappe
import unittest

from frappe.tests import IntegrationTestCase


class TestNonConformance(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
