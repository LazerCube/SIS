# Student Information System(SIS) - College Work

###     Usage

Use `python manage.py runserver` - for local machine testing.       
Use `python manage.py runserver 0.0.0.0:8000` - for local network testing.      


Use `python manage.py runserver 0.0.0.0:8000 --secure` to run test server when
`DEBUG = False` or else static files won't load. Custom 404 and 500 pages won't
show unless `DEBUG = False`.


If you want Debug information then `DEBUG = True` needs to be set in settings.py.
NOTE: This won't show custom 404 and 500 pages.

### Dependencies

*   Django-tables2
