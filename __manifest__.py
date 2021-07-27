# -*- coding: utf-8 -*-
{
    'name': "Cadastro dos Atendimentos",

    'summary': """
        Cadastro dos Atendimentos Presenciais""",

    'description': """
        Atendimento Presencial
    """,

    'author': "Ricardo Correa Ribeiro",
    'website': "https://github.com/ricardocr18",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/seguranca.xml',
        'security/ir.model.access.csv',
        'reports/pdf_report.xml',
        'reports/report.xml',
        'views/views.xml',
        'views/templates.xml',
        #'views/cadastro_categoria.xml',
        'views/solicitacao_procon.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
