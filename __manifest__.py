{
    'name': 'tiket pesawat',
    'version': '1.0',
    'author': 'amira Balqhis',
    'summary': 'module yang berisikan Pesawat, Form pesawat, Harga',
    'description': """ ini adalah module custom di udoo mengenai tiket pesawat """,
    'website': 'https://www.odooairplane.com',
    'depends': ['base'],
    'data': [
        'views/plane.xml',
        'reports/report.xml',
        'reports/boarding_pass.xml',
        'data/data.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

#{
    #'name' : 'Tiket Pesawat',
    #'author' : 'Amira Balqhis',
    #'version' : '1.0',
    #'website' : 'https://www.odooairplane.com',
    #'summary' : 'Module yang berisikan Pesawat, Form pesawat, Harga',
    #'data' : [
        #'plane.xml'
    #]
    
#}
