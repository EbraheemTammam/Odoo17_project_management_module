{
    'name':"Project Management",
    'auther':"Ebraheem Tammam",
    'version':'17.0.0.1.0',
    'category': '',
    'depends':[
        'base',
        'hr',
    ],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/project_view.xml',
        'views/task_view.xml',
        'views/project_dashboard.xml',
        'reports/project_report.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'project_management/static/src/css/global.css',
            'project_management/static/src/css/product.css',
        ]
    },
    'application':True,
}
