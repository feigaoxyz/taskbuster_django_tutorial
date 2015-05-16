[Taskbuster Django Tutorial](http://www.marinamele.com/taskbuster-django-tutorial)


## coverage

```sh
coverage run --source='.' manage.py test
coverage report
coverage html
```

## i18n

```sh
python manage.py makemessages -l cn
# work on app/locale/lang
python manage.py compilemessages -l cn
```

## testing

```sh
python manage.py test functional_tests.test_all_users.HomeNewVisitorTest.test_i18n
python manage.py test
```
