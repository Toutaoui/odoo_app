from odoo import models, fields

class TpIncident(models.Model):
    _name = "tp.incident"
    _description = "Incident"

    name = fields.Char(string="Titre de l'incident", required=True)
    responsable = fields.Char(string="Responsable")
    date_signalement = fields.Date(string="Date de signalement")
    statut = fields.Selection([
        ("nouveau", "Nouveau"),
        ("en_cours", "En cours"),
        ("resolu", "Résolu"),
    ], string="Statut", default="nouveau")
    description = fields.Text(string="Description détaillée")