{
    "name": "Invoice Tracking",
    "version": "1.0",
    "category": "Accounting",
    "summary": "Invoice Tracking",
    "author": "Horizon 4 Services",
    'website': "https://www.horizonservices.com",
    "description": "Invoice Tracking",

    # any module necessary for this one to work correctly
    "depends": ["base", "account", "documents"],

    # always loaded
    "data": [
         'security/ir.model.access.csv',
        'views/res_config_settings_view.xml',
        'views/sequence.xml',
        'views/ir_attachment_views.xml',
        'views/invoice_tracking_view.xml',
        'views/invoice_document_view.xml',
        'views/stage_views.xml',
        'views/menu_item.xml'
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}