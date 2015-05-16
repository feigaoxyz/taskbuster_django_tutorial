[Taskbuster Django Tutorial](http://www.marinamele.com/taskbuster-django-tutorial)


## coverage

```sh
coverage run --source='.' manage.py test
coverage report
coverage html
```

## i18n

```python
# settings.py
LANGUAGES = (
    ('en', _('English')),
    ('zh-hans', _('Chinese (PRC)')),
    ('ca', _('Catalan')),
)
```

```sh
python manage.py makemessages -l zh_hans
# work on app/locale/lang
python manage.py compilemessages -l zh_hans
```

## testing

```sh
python manage.py test functional_tests.test_all_users.HomeNewVisitorTest.test_i18n
python manage.py test
```

## database

```sh
python manage.py check
python manage.py migrate
```


