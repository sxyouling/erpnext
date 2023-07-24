// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Procurement Tracker"] = {
	filters: [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
		},
		{
			fieldname: "cost_center",
			label: __("Cost Center"),
			fieldtype: "Link",
			options: "Cost Center",
		},
		{
			fieldname: "project",
			label: __("Project"),
			fieldtype: "Link",
			options: "Project",
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
<<<<<<< HEAD
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[1],
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), with_dates=true)[1],
>>>>>>> 4496a6760e (fix: Default year start and end dates in reports)
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
<<<<<<< HEAD
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), true)[2],
=======
			default: erpnext.utils.get_fiscal_year(frappe.datetime.get_today(), with_dates=true)[2],
>>>>>>> 4496a6760e (fix: Default year start and end dates in reports)
		},
	],
};
