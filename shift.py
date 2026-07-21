# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.i18n import gettext
from trytond.model import ModelSQL, ModelView, fields
from trytond.model.exceptions import ValidationError


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
        cls._order.insert(0, ('start_time', 'ASC'))

    @staticmethod
    def default_active():
        return True

    @classmethod
    def validate(cls, shifts):
        super().validate(shifts)
        for shift in shifts:
            if shift.start_time == shift.end_time:
                raise ValidationError(gettext(
                    'working_shift_definition.msg_different_start_end'))
