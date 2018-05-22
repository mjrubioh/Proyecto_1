# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError




class sugerecla(models.Model):
    _name = "suge.recla"
    
    name = fields.Char(string='Nombre:', required=True, readonly=False,)
    apell = fields.Char(string='Apellido:', required=True, readonly=False,)
    ced = fields.Char(string='Cédula:', required=True, readonly=False, )
    corr = fields.Char(string='Correo:', required=True, readonly=False,)
    tlf = fields.Char(string='Teléfono:', required=True, readonly=False,)
    sex = fields.Selection([
        ('mas', 'Masculino'),
        ('fem', 'Femenino'),
        ('ind', 'Indefinido'),
        ], string='Sexo:', compute='_compute_invoice_status', store=True, readonly=False)
    semes = fields.Char(string='Semestre:', required=True, readonly=False,)
    carr = fields.Char(string='Carrera:', required=True, readonly=False,)
    horario = fields.Many2one('clase.horario', string='Horario', required=True)
    suge = fields.Text(string='Sugerencias o Reclamos:', required=True, readonly=False,)
    
   class claseCategoria(models.Model):
    _name = "clase.horario"
    

    name = fields.Char(string='Diurno', required=True, readonly=False,)
    noct = fields.Integer(string='Nocturno', required=True, readonly=False,)
    mixt = fields.Boolean(string='Mixto', required=True, readonly=False,)
   
    def create(self, vals):
        Sugerencias = vals['suge']   
        malas_palabras = ['culo','guebo','mamaguebo','maduro','mardito','trimardito']
        lista_sugerencias = Sugerencias.split('')
        for i in lista_sugerencias:
			if i in malas_palabras:
			    raise UserError(_('No se aceptan malas palabras.'))
		 
return super(SaleOrderLine, self).create(vals)
