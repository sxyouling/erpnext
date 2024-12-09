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
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	pass
