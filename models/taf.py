from odoo import fields,models,api


class Taf(models.Model):
    _name = "taf"
    
    name = fields.Char("Nom de la tâche", required=True)
