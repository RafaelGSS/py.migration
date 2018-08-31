import sys, inspect
from migrations._29082018_example import Example

migrations = []

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        migrations.append(obj)