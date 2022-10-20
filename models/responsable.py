from odoo import api, fields, models,api
class Responsable(models.Model):
    _name="responsable"

    name=fields.Char("", compute="nom_prenom")
    nom=fields.Char("Nom du personnel", required=True)
    prenom=fields.Char("Prenom du personnel", required=True)
    departement=fields.Char("Département", required=True)
    telephone=fields.Integer("Numéro de telephone", required=True)
    x_stagiaire_ids= fields.One2many('stagiaire', 'x_responsable_id', string='stagiaires')

    @api.depends('nom','prenom')
    def nom_prenom(self):
        for record in self:
            record.name=record.nom +" "+ record.prenom