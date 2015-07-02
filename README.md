# DjangoBug

When the default manager returns a queryset with a deferred field, the dumpdata
command fails to produce importable data.

## Steps to reproduce

1. Setup the environment

    $ git clone https://github.com/cecedille1/DjangoBug.git .
    $ virtualenv . --python python3
    $ source bin/activate
    $ pip install -r requirements.txt
    $ bug migrate
    $ bug loaddata initial

2. Reproduce the bug

    $ bug dumpdata
    [{"model": "my_bug.mymodel_deferred_an_expensive_value", "fields": {"value": "abc", "an_expensive_value": "dGhpcw=="}, "pk": 1}]>>


The name of the model is ``mymodel_deferred_an_expensive_value`` and Django wont be able to load it later.
