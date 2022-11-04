{
    'name':'Carga de buque',
    'description':'Aplicacion que permitira administrar y controlar la carga de buques mediante blablablabla',
    'depends':['base', 'contacts'],
    'data':[
        'security/ir.model.access.csv',
        'views/ship.xml',
        'views/load_control.xml',
        ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}