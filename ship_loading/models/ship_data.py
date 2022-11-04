from odoo import models, fields

class ship(models.Model):
    _name = 'ship.data'

    # Datos del buque
    ship_name = fields.Char(string="Nombre del buque")
    hold_quantity = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')], string='Cantidad de bodegas', default='5')

    # Capacidad de carga
    ship_capacity = fields.Integer(string="Capacidad del buque")

    # Carga actual
    ship_cargo = fields.Integer(string='Carga actual del buque')

    # Carga restante
    ship_remain = fields.Integer(string='Carga restante del buque')
    
    # Control de tiempo
    start_date = fields.Date(string='Fecha de inicio')
    end_date = fields.Date(string='Fecha de finalizacion')
    operation_time = fields.Datetime(string='Tiempo de operacion')

    # Estado de operacion
    ship_stage = fields.Selection([('0','Preparacion'),('1','A la espera'),('2','En proceso'),('3','Finalizado/Archivado'),], string='Fase del buque', default='0')

#class holdData(models.Model):
    #_name = 'hold.data'

    # Datos de la bodega
    hold_number = fields.Integer(string='Numero de la bodega')

    # Capacidad de carga por bodega
    hold_capacity = fields.Integer(string="Capacidad por bodega")

    # Carga actual por bodega
    hold_cargo1 = fields.Integer(string='Carga actual de bodega 1')
    hold_cargo2 = fields.Integer(string='Carga actual de bodega 2')
    hold_cargo3 = fields.Integer(string='Carga actual de bodega 3')
    hold_cargo4 = fields.Integer(string='Carga actual de bodega 4')
    hold_cargo5 = fields.Integer(string='Carga actual de bodega 5')
    hold_cargo6 = fields.Integer(string='Carga actual de bodega 6')

    # Carga restante por bodega
    hold_remain = fields.Integer(string='Carga restante de bodega')
    h2old_remain = fields.Integer(string='Carga restante de bodega')


    load_control_id = fields.One2many('load.control', 'ship_data_id', string='Plan de carga')

