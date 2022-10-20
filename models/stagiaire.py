
from odoo import api, fields, models

class Stagiaire(models.Model):
    _name="stagiaire"

    name=fields.Char("Nom du stagiaire", required=True)
    
    prenom=fields.Char("Prenom du stagiaire", required=True)
    theme=fields.Char("Thème de stage", required=True)
    dateDebut=fields.Date("date de début de stage", required=True)
    dateFin=fields.Date("date de fin de stage", required=True)
    x_responsable_id=fields.Many2one("responsable",string="Responsable")
    taches = fields.Many2many('taf','stagiaire_taf', 'stagiaire_id', 'taf_id', string="Tâches")