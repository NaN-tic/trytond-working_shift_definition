# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.pool import Pool

from . import shift


def register():
    Pool.register(
        shift.WorkingShiftDefinition,
        module='working_shift_definition', type_='model')
