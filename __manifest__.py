# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    "name": "Employee Self Service",
    "version": "2.7.1",
    "category" : "Human Resources",
    "license": "Other proprietary",
    "price": 49.0,
    "currency": "EUR",
    "summary": """This module allow your employee to have self service in Odoo.""",
    "description": """
It will include all the  Employee self service info. 
Allowed Employee to edit own information
Allowed Employee to manage Timesheet
Allowed Employee to manage Detail Activities
Allowed Employee to mofy attendes
Allowed Employee to manage own leave request
Allowed Employee to manage Expenses
Allowed Employee to send maintanance requests
Allowed Employee to manage contracts
Allowed Employee to manage projects
Allowed Employee to manage Tasks
employee login
emloyee information
employee detail
sse
ess employee
Self Service
Self Service/Calendar
Self Service/Employee
Self Service/Employee/Employee Details
Self Service/Expenses
Self Service/Expenses/Expenses to Submit
Self Service/Leave Request
Self Service/Leave Request/Leaves Requests
Self Service/Maintenance
Self Service/Maintenance/Maintenance Requests
Self Service/Projects
Self Service/Projects/Projects
Self Service/Projects/Tasks
Self Service/Timesheet
Self Service/Timesheet/Attendences
Self Service/Timesheet/Detailed Activities
Self Service/Timesheet/My Timesheets
employee self service
ESS
ess
self service odoo
self service
self portal
odoo self service employee
self service odoo employee
employee leave
employee timesheet
employee holidays
self service portal
""",
    "author": "Probuse Consulting Service Pvt. Ltd.",
    "website": "http://www.probuse.com",
    "support": "contact@probuse.com",
    "images": ["static/description/img1.jpg"],
#    "live_test_url": "https://youtu.be/Ou1sWt7ndTw",
    "live_test_url": 'https://probuseappdemo.com/probuse_apps/employee_self_service_odoo/812',#"https://youtu.be/GDn3mfnu8is",
    "depends": [
#                 "hr_timesheet_sheet",
                'hr_timesheet',
                'hr_contract',
                # "hr_payroll",
                "hr_holidays",
                "hr_expense",
                "hr_attendance",
                "hr_maintenance",
                "project",
                ],
    "data":[
        # "security/ir.model.access.csv",
        "views/employee_view.xml",
        "views/menu.xml",
    ],
    "installable" : True,
    "application" : False,
    "auto_install" : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
