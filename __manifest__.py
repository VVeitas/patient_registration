# -*- coding: utf-8 -*-
{
    'name': "patient_registration",

    'summary': """
        Patient registration system.""",

    'description': """
        Patient registration system with registrations of patients, doctors, visits, supplements etc...
    """,

    'author': "Valentas",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/disease_views.xml',
        'views/patient_views.xml',
        'views/relationship_views.xml',
        'views/doctor_views.xml',
        'views/visit_views.xml',

        'report/visit_report_templates.xml',
        'report/visit_report.xml',
    ],
}
