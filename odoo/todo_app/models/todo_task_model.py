# todo_task_model.py
# noinspection PyUnresolvedReferences
from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)
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

    def do_clear_done(self):
        for task in self:
            if task.active:
                task.active = False
                _logger.info('Mamoun TodoTask do_clear_done set active to false')
            else:
                raise exceptions.UserError("La tache est déjà inactive")
        return True

    def write(self, values):
        # Before write logic
        if 'active' not in values:
            _logger.info('Mamoun TodoTask write set active to true')
            values['active'] = True
        return super(TodoTask, self).write(values)

