{
    'name': 'Invoice Tracking',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Invoice Tracking',
    'description': 'Invoice Tracking',
    'depends': ['base', 'account', 'documents'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/invoice_document_views.xml',
        'views/invoice_document_menus.xml',
    ],
    'installable': True,
    'application': True,
    "license": "LGPL-3"
}