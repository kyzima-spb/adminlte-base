Flask-AdminLTE-Full
===================

.. module:: flask_adminlte_full

Flask-AdminLTE-Full is an extension for `Flask`_ that integrates the `AdminLTE`_ template with most of the features.

Installation
------------

Install the latest stable version::

    $ pip install flask-adminlte-full

or install development version (bugs are possible)::

    $ pip install https://github.com/kyzima-spb/flask-adminlte-full/archive/dev-master.zip

Configuration
-------------

To get started all you need to do is to instantiate a :class:`AdminLTE` object after configuring the application::

    from flask import Flask
    from flask_adminlte_full import AdminLTE

    app = Flask(__name__)
    # read config
    adminlte = AdminLTE(app)

A list of all available configuration parameters can be found in the :ref:`configuration` section.

i18n
----

To enable internationalization, install one of the `Flask-Babel`_ or `Flask-BabelEx`_ extension::

    $ pip install Flask-Babel
    # or
    $ pip install Flask-BabelEx

API
---

.. autoclass:: AdminLTE
   :members:
   :undoc-members:

HTML Forms
^^^^^^^^^^

.. autoclass:: flask_adminlte_full.forms.LoginForm
   :members: email, password, remember_me
   :show-inheritance:
   :undoc-members:

   Login form.

.. autoclass:: flask_adminlte_full.forms.ResetPasswordForm
   :members: email
   :show-inheritance:
   :undoc-members:

   Password reset form.

.. _Flask: http://flask.pocoo.org/
.. _AdminLTE: https://adminlte.io/
.. _Flask-Babel: https://pythonhosted.org/Flask-Babel/
.. _Flask-BabelEx: https://pythonhosted.org/Flask-BabelEx/
