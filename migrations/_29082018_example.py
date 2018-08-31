from migrations.base.model import Model
from migrations.base.fields import *


class Example(Model):
    def __init__(self):
        super().__init__(table='example')

    def up(self):
        return [
            FieldInt('id').auto_increment().primary_key(),
            FieldVarchar('type').not_null(),
            FieldVarchar('request').nullable(),
            FieldTimestamp('created_at').default('CURRENT_TIMESTAMP'),
        ]
