# -*- coding: utf-8 -*-
{
    'name': 'Aptys project',
    'version': '13.0.1.0.0',
    'summary': """Additional features for project module""",
    'description': 'Additional features for project odoo module',
    'category': 'Project',
    'author': 'Idealis Consulting',
    'website': 'http://www.idealisconsulting.com',
    'depends': ['base','project','sale_timesheet'],
    'data': [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'view/project_task_views.xml',
    ],
    'images': [],
    'license': 'LGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
