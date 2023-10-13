# noinspection PyUnresolvedReferences
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #todo_ids = fields.Many2one(
     #   comodel_name='todo.task',
      #  string='To-do Teams',
    #)
