from odoo import models, fields, api

class InvoiceDocument(models.Model):
    #_name = 'invoice.document'
    _inherit = 'documents.document'
    _description = 'Invoice Document'


    number = fields.Char(string='N°', required=True)
    status = fields.Selection([
        ('recieved', 'Reçue'),
        ('visa_dg', 'Visa DG'),
        ('visa_difi', 'Visa DIFI'),
        ('chef_unite_valide', 'Validation Chef Unité'),
        ('chef_comptable_valide', 'Validation Chef Comptable'),
        ('cost_control_valide', 'Validation Cost Control'),
        ('paiement_prepare', 'Préparation Paiement'),
        ('archive', 'Archivage')
    ], default='recieved', string='Statut')  
    assigned_to = fields.Many2one('hr.department', string='Assigné à')
    history_ids = fields.One2many('invoice.history', 'document_id', string='Historique')

    @api.model
    def create(self, vals):
        if not vals.get('number'):
            vals['number'] = self.env['ir.sequence'].next_by_code('documents.document.number.sequence') or '/'
        return super(InvoiceDocument, self).create(vals)

    @api.model
    def change_status(self, new_status, comment=None):
        for record in self:
            record.status = new_status
            self.env['invoice.history'].create({
                'document_id': record.id,
                'user_id': self.env.user.id,
                'action': 'validation' if 'valide' in new_status else 'rejet',
                'comment': comment
            })
            record.message_post(body=f'Statut changé à {new_status}')

    def view_action(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'documents.document',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'self',
        }