from odoo import models, fields

class InvoiceHistory(models.Model):
    _name = 'invoice.history'
    _description = 'Historique des actions sur la facture'

    document_id = fields.Many2one('documents.document', string='Document')
    user_id = fields.Many2one('res.users', string='Utilisateur')
    action =  fields.Selection([
        ('validation', 'Validation'),
        ('rejet', 'Rejet'),
        ('accounting', 'Comptabilisation'),
        ('archivage', 'Archivage')
    ], string='Action')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    comment = fields.Text(string='Commentaire')
