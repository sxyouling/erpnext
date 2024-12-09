# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from frappe.model.document import Document


class UOM(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

<<<<<<< HEAD
		enabled: DF.Check
		must_be_whole_number: DF.Check
=======
		common_code: DF.Data | None
		description: DF.SmallText | None
		enabled: DF.Check
		must_be_whole_number: DF.Check
		symbol: DF.Data | None
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
		uom_name: DF.Data
	# end: auto-generated types

	pass
