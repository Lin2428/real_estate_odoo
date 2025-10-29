{
    "name": "Annonces Imobilières",
    "version": "1.0",
    "website": "https://horizon4services.com",
    "authoe": "Lin Daily",
    "description": """
        Real Estate to show available properties
    """,
    "category": "Sales",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tags_view.xml',
        'views/menu_items.xml',
        
        #Data
        #'data/property_type.xml'
         #'data/estate.property.type.csv'
    ],
    'images': ['static/description/icon.png'],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}