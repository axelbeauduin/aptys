# -*- coding: utf-8 -*-
{
    'name': 'Aptys timesheet',
    'version': '13.0.1.0.0',
    'summary': """Additional features for timesheet module""",
    'description': 'Additional features for timesheet odoo module',
    'category': 'Timesheet',
    'author': 'Idealis Consulting',
    'website': 'http://www.idealisconsulting.com',
    'depends': ['base','hr_timesheet','timesheet_grid'],
    'data': [
        # 'security/hr_timesheet_security.xml',
        'views/hr_timesheet_views.xml',
    ],
    'images': [],
    'license': 'LGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
