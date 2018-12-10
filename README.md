## How to launch

```bash
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
pip install -r requirements/common.txt
# create db user, database
# grant user access to create databases for tests
./manage.py migrate
./manage.py test apps.core.tests
./manage.py runserver
```

## Tests

<p>Tests are located in apps/core/tests.py</p>