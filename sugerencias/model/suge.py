# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _




class sugerecla(models.Model):
    _name = "suge.recla"
    
    

    name = fields.Char(string='Nombre', required=True, readonly=False,)
	apell = fields.Char(string='Apellido', required=True, readonly=False,)
	carr = fields.Char(string='Carrera', required=True, readonly=False,)
	Horario = fields.Many2one('clase.horaria', string='Horario', required=True)
    reclamos = fields.One2many('clase.sugerecla', 'unefa_id', string='Suge Recla', )

   


class claseCategoria(models.Model):
    _name = "clase.horario"
    

    name = fields.Char(string='Diurno', required=True, readonly=False,)
    noct = fields.Integer(string='Nocturno', required=True, readonly=False,)
    mixt = fields.Boolean(string='Mixto', required=True, readonly=False,)
    
    

class claseunefa2(models.Model):
    _name = "clase.sugerecla"
    

    name = fields.Char(string='Sugerencia', required=True, readonly=False,)
    recla = fields.Char(string='Reclamos', required=True, readonly=False,)
    
    unefa_id = fields.Many2one('suge.recla', string='Unefa',)
"""
