# Student Information System(SIS) - College Work

## Usage

Use `python manage.py runserver` - for local machine testing.
Use `python manage.py runserver 0.0.0.0:8000` - for local network testing.

Use `python manage.py runserver 0.0.0.0:8000 --insecure` to run test server when
`DEBUG = False` or else static files won't load. Custom 404 and 500 pages won't
show unless `DEBUG = False`.

If you want Debug information then `DEBUG = True` needs to be set in settings.py.
NOTE: This won't show custom 404 and 500 pages.

### Admin account

- Username: Admin
- Password: adminpassword

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python-pip](https://pypi.python.org/pypi/pip) - Dependency Management
- [virtualenv](https://pypi.org/project/virtualenv/) - A tool for creating isolated ‘virtual’ python environments
