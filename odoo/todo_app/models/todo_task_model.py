# todo_task_model.py
# noinspection PyUnresolvedReferences
from odoo import models, fields
#test de commit 2

class TodoTask(models.Model):
    _name = 'todo.task'
    type = fields.Char(required=True)
    is_done = fields.Boolean()
    active = fields.Boolean(default=True)
    date_deadline = fields.Date()
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        default=lambda self: self.env.user,
    )
    team_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Team',
    )
