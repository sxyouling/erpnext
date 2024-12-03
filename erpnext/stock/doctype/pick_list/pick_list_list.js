// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.listview_settings["Pick List"] = {
	get_indicator: function (doc) {
		const status_colors = {
<<<<<<< HEAD
			Draft: "red",
=======
			Draft: "grey",
>>>>>>> 329d14957b (fix: validate negative qty)
			Open: "orange",
			Completed: "green",
			Cancelled: "red",
		};
		return [__(doc.status), status_colors[doc.status], "status,=," + doc.status];
	},
};
