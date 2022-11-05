from odoo import models, fields

class load_control(models.Model):
    _name = 'load.control'

    gabarra_id = fields.Char(string='Gabarra ID')
    # ub = fields.Char(string='???')
    berthing_date = fields.Date(string='Fecha de atraque')
    # rem = fields.????

    ### Aqui falta el control de tiempo, posiblemente se realice en otro modelo

    total_time = fields.Datetime(string='Tiempo de descarga de Gabarra')
    cargo_unload = fields.Integer(string='Peso descargado')
    gabarra_ratio = fields.Float(string='Material descargado por hora')

    #Bodegas
    hold1_unload = fields.Integer(string='Bodega 1')
    hold2_unload = fields.Integer(string='Bodega 2')
    hold3_unload = fields.Integer(string='Bodega 3')
    hold4_unload = fields.Integer(string='Bodega 4')
    hold5_unload = fields.Integer(string='Bodega 5')
    hold6_unload = fields.Integer(string='Bodega 6')
    hold7_unload = fields.Integer(string='Bodega 7')
    hold8_unload = fields.Integer(string='Bodega 8')
    hold9_unload = fields.Integer(string='Bodega 9')
    hold10_unload = fields.Integer(string='Bodega 10')
    hold11_unload = fields.Integer(string='Bodega 11')
    hold12_unload = fields.Integer(string='Bodega 12')

    ship_data_id = fields.Many2one('ship.data', string='Info del buque')

