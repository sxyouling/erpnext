<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> da09316d4c (fix: precision check for salvage value)

from erpnext.utilities.activation import get_level


<<<<<<< HEAD
class TestActivation(FrappeTestCase):
=======
class TestActivation(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
