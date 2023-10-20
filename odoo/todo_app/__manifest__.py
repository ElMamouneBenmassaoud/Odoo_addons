# -*- coding: utf-8 -*-
{
    'name': "todo_app",

    'summary': """
        Todo App offre une interface intuitive pour créer, modifier, 
        supprimer et marquer les tâches comme complètes ou en attente.
        """,

    'description': """
        L'application Todo App est une solution de gestion de tâches inspirée par les principes du développement Odoo. 
        Elle a été créée en suivant les directives du livre "Daniel Reis, Odoo 11 Development Essentials - Third Edition," publié par Packt en mars 2018. 
        Cette application permet aux utilisateurs de gérer efficacement leurs tâches quotidiennes, de rester organisés et de suivre leurs progrès de manière transparente.
    """,

    'author': "El Mamoune Benmassaoud",
    'website': "www.mamoun.vercel.app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
