========
teamInfo
========

teamInfo is a simple Django app, just a rudiment of teamer information test 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "teamInfo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'teamInfo',
    )

2. Include the teamInfo URLconf in your project urls.py like this::

    url(r'^teamInfo/', include('teamInfo.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a teamInfo (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/teamInfo/ to participate in the poll.
