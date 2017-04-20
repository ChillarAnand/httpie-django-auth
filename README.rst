httpie-django-auth
=====================

django auth plugin for HTTPie.


Installation
==============

.. code-block:: shell

    $ pip install httpie-django-auth


You should now see ``django`` under ``--auth-type`` in ``$ http --help`` output.


Usage
=========

By default httpie-django-auth uses `/admin/login` to login. If you need to use some other url for logging, set `HTTPIE_DJANGO_AUTH_URL` environment variable.

.. code-block:: shell

    export HTTPIE_DJANGO_AUTH_URL='/accounts/login/'


Make requests to your site

.. code-block:: shell

    $ http --auth-type=django --auth='username:password' example.org
    $ http -A=django --auth='username:password' example.org
    $ http -A=django --auth='username:password' example.org/profile
    $ http -A=django --auth='username:password' http://127.0.0.1:8000/profile


License
=========

See LICENSE.txt
