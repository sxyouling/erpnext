import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)

INDEXED_FIELDS = {
	"Bin": ["item_code"],
	"GL Entry": ["voucher_no", "posting_date", "company", "party"],
	"Purchase Order Item": ["item_code"],
	"Stock Ledger Entry": ["warehouse"],
}


<<<<<<< HEAD
class TestPerformance(FrappeTestCase):
=======
class TestPerformance(IntegrationTestCase):
>>>>>>> 325b20491a (fix: make rate of depreciation mandatory)
	def test_ensure_indexes(self):
		# These fields are not explicitly indexed BUT they are prefix in some
		# other composite index. If those are removed this test should be
		# updated accordingly.
		for doctype, fields in INDEXED_FIELDS.items():
			for field in fields:
				self.assertTrue(
					frappe.db.sql(
						f"""SHOW INDEX FROM `tab{doctype}`
						WHERE Column_name = "{field}" AND Seq_in_index = 1"""
					)
				)
