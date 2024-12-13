<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)

from erpnext.utilities.activation import get_level


<<<<<<< HEAD
class TestActivation(FrappeTestCase):
=======
class TestActivation(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
