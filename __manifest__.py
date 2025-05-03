# -*- coding: utf-8 -*-
{
    'name': "Real Estate Ads",

    'summary': """
        Real Estate module
    """,

    'description': """
        Real Estate module to show avalilable properties, its features, etc
    """,

    'author': "LGPM Developments",
    'website': "https://github.com/laguipemo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/real_estate_ads_groups.xml',
        'security/ir.model.access.csv',
        'security/model_access.xml',
        'security/ir_rule.xml',
        'views/property_views.xml',
        'views/property_type_views.xml',
        'views/property_tag_views.xml',
        'views/property_offer_views.xml',
        'views/views.xml',
        'views/menu_items.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'real_estate_ads/static/src/js/my_custom_tag.js',
            'real_estate_ads/static/src/xml/my_custom_tag.xml',
        ],
    },
    "installable": "True",
    "application": "True",
    "licence": "LGPL-3"
}
