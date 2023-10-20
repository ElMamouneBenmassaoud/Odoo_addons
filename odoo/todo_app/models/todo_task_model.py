# todo_task_model.py
# noinspection PyUnresolvedReferences
from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(help="What needs to be done?")
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Deadline')

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        default=lambda self: self.env.user,
    )
    team_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Team',
    )
