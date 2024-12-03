// Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.listview_settings["Subcontracting Receipt"] = {
	get_indicator: function (doc) {
		const status_colors = {
<<<<<<< HEAD
			Draft: "red",
=======
			Draft: "grey",
>>>>>>> 329d14957b (fix: validate negative qty)
			Return: "gray",
			"Return Issued": "grey",
			Completed: "green",
		};
		return [__(doc.status), status_colors[doc.status], "status,=," + doc.status];
	},
};
