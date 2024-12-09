# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Mode of Payment')


class TestModeofPayment(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestModeofPayment(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	pass
