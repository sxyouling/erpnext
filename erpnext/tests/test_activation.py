<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)

from erpnext.utilities.activation import get_level


<<<<<<< HEAD
class TestActivation(FrappeTestCase):
=======
class TestActivation(IntegrationTestCase):
>>>>>>> d847f75ade (chore: remove 'debug' param and linter fix)
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
