<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 329d14957b (fix: validate negative qty)

from erpnext.utilities.activation import get_level


<<<<<<< HEAD
class TestActivation(FrappeTestCase):
=======
class TestActivation(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
