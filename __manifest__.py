# -*- coding: utf-8 -*-
{
    'name': "Parametros Contabilidad - Peru",

    'summary': """
        Estrablece parametros y permisos para la contabilidad de Peru""",

    'description': """
        - Completa tipos de comprobantes de pago como "[91] No domiciliados", etc.
    """,

    'author': "Tagre app",
    'website': "https://tagre.app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Localizations',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'l10n_pe'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/account_tax_data.xml',
        'data/l10n_pe_document_type.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
