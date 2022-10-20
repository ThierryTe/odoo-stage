from odoo import api, models
from odoo.addons.stage.models import stagiaire

""""
def print_report(self):
    data = {
       'nom': self.nom,
       'prenom': self.prenom,
       'theme' : self.theme,
       'dateDebut' : self.dateDebut,
       'dateFin' : self.dateFin,
       'x_responsable_id': self.x_responsable_id
    }

    return self.env.ref('stage.action_stagiaire_id_card').report_action(None, data=data)
"""

class StagiaireCard(models.AbstractModel):
    _name = 'report_stagiaire_id_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env[stagiaire].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': model.model,
            'docs': docs,
            'data': data,
            'get_something': self.get_something,
        }

    def get_something(self):
        return 3