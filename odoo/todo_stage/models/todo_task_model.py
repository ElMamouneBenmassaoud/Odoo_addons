# noinspection PyUnresolvedReferences
from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task']

    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")

    desc = fields.Text('Description')

    #type(state) : liste déroulante (clé -> valeur)
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], default='draft')

    docs = fields.Html('Documentation')

    # Date fields:
    date_created = fields.Datetime(
        'Create Date and Time',
        default=lambda self: fields.Datetime.now())

    # Other fields:
    image = fields.Binary('Image')

    # Relational fields
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
