# noinspection PyUnresolvedReferences
from odoo import models, fields


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', translate=True)

    # Many2many inverse relationship
    task_ids = fields.Many2many('todo.task', string='Tags')

    #name must be unique
    _sql_constraints = [
        ('todo_task_tag_name_unique',
         'UNIQUE(name)',
         "Tag name already exists!"),
    ]