# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.model import Check, ModelSQL, ModelView, fields


class WorkingShiftDefinition(ModelSQL, ModelView):
    'Working Shift Definition'
    __name__ = 'working.shift.definition'

    name = fields.Char('Name', required=True)
    start_time = fields.Time('Start Time', required=True)
    end_time = fields.Time('End Time', required=True)
    active = fields.Boolean('Active')

    @classmethod
    def __setup__(cls):
        super().__setup__()
        table = cls.__table__()
        cls._sql_constraints += [
            ('different_start_end', Check(table, table.start_time != table.end_time),
                'Start and end time must be different.'),
        ]
        cls._order.insert(0, ('start_time', 'ASC'))

    @staticmethod
    def default_active():
        return True
