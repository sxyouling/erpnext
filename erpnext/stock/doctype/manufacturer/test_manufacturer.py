# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Manufacturer')


class TestManufacturer(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestManufacturer(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	pass
