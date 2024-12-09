<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)

from erpnext.utilities.activation import get_level


<<<<<<< HEAD
class TestActivation(FrappeTestCase):
=======
class TestActivation(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	def test_activation(self):
		levels = get_level()
		self.assertTrue(levels)
