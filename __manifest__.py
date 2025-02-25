# -*- coding: utf-8 -*-
{
    'name': "Partner Delivery for Shipping methods",
    'version': '18.0.0.1',
    'category': 'stock/stock',
    'description': """ Add new fields partner delivery for shipping methods """,
    'depends': ['delivery', 'base'],

    'data': [

        'views/delivery_carrier.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',

}

