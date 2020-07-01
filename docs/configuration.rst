.. _configuration:


Configuration
=============

Set the required options in your configuration file that uses your framework:

=========================================    =====================================================
Option                                       Description
=========================================    =====================================================
`ADMINLTE_ACCENT_COLOR`                      The color of the hyperlinks.
                                             Defaults to ``None``.
`ADMINLTE_BACK_TO_TOP_ENABLED`               Turn on the back to top button.
                                             Defaults to ``False``.
`ADMINLTE_BODY_SMALL_TEXT`                   Set small text for the page.
                                             Defaults to ``False``.
`ADMINLTE_DEFAULT_LOCALE`                    The default locale, by default, uses the source text.
                                             Defaults to ``None``.
`ADMINLTE_FOOTER_SMALL_TEXT`                 Set small text for the footer of the page.
                                             Defaults to ``False``.
`ADMINLTE_HOME_PAGE`                         The tuple sets the URL and title of the homepage.
                                             Used in breadcrumbs.
                                             Defaults to ``('/', 'Home')``.
`ADMINLTE_LAYOUT`                            Page layout, bitmask of the available options,
                                             :ref:`see more<configuration:ThemeLayout>`.
                                             Defaults to ``ThemeLayout.DEFAULT``.
`ADMINLTE_LEGACY_USER_MENU`                  Use the user menu from AdminLTE2.
                                             Defaults to ``False``.
`ADMINLTE_SITE_TITLE`                        The title of the site.
                                             Defaults to ``'AdminLTE 3'``.
`ADMINLTE_USER_MAPPING`                      Sets the mapping of the properties and methods
                                             of the user object used in the templates
                                             to the properties and methods
                                             of the user object of your framework.
                                             :ref:`See example<configuration:ADMINLTE_USER_MAPPING>`.
                                             Defaults to ``{}``.
**Brand Logo**
--------------------------------------------------------------------------------------------------
`ADMINLTE_BRAND_COLOR`                       Background :ref:`color<configuration:ThemeColor>` for the logo.
                                             Defaults to ``None``.
`ADMINLTE_BRAND_IMAGE_ALT`                   Alternative text if the logo image is not available.
                                             Defaults to ``'AdminLTE Logo'``.
`ADMINLTE_BRAND_TEXT`                        The text displayed to the right of the logo.
                                             Defaults to ``'AdminLTE 3'``.
`ADMINLTE_BRAND_HTML`                        HTML version of the logo used on login pages and the like.
                                             Defaults to ``'<b>Admin</b>LTE 3'``.
`ADMINLTE_BRAND_SMALL_TEXT`                  Set small text for text logo.
                                             Defaults to ``False``.

**Top Navigation Bar**
--------------------------------------------------------------------------------------------------
`ADMINLTE_NAVBAR_COLOR`                      The background :ref:`color<configuration:ThemeColor>` of the top navigation bar.
                                             Defaults to ``ThemeColor.WHITE``.
`ADMINLTE_NAVBAR_NO_BORDER`                  Remove frames from the navigation bar.
                                             Defaults to ``False``.
`ADMINLTE_NAVBAR_SMALL_TEXT`                 Set small text for the navigation bar.
                                             Defaults to ``False``.

**Main and Second Sidebar**
--------------------------------------------------------------------------------------------------
`ADMINLTE_MAIN_SIDEBAR_ENABLED`              Enable or disable the main sidebar.
                                             Defaults to ``True``.
`ADMINLTE_SECOND_SIDEBAR_ENABLED`            Enable or disable the optional sidebar.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_CHILD_INDENT`              Enable left margin for children of the main sidebar.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_COLOR`                     The :ref:`color<configuration:ThemeColor>` of the active elements of the main sidebar.
                                             Defaults to ``ThemeColor.PRIMARY``.
`ADMINLTE_SIDEBAR_LIGHT`                     Light theme for the main sidebar, the default is dark.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_COMPACT`                   Remove margins between elements of the main sidebar.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_FLAT_STYLE`                Use a flat style for the main sidebar.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_LEGACY_STYLE`              Use the style of the main sidebar from AdminLTE2.
                                             Defaults to ``False``.
`ADMINLTE_SIDEBAR_SMALL_TEXT`                Set small text for the main sidebar.
                                             Defaults to ``False``.
Services
--------------------------------------------------------------------------------------------------
`ADMINLTE_ALLOW_REGISTRATION`                Allow user registration.
                                             The option only affects the display of links,
                                             the logic needs to be implemented.
                                             Requires setting the value of the dependent option ``ADMINLTE_REGISTRATION_ENDPOINT``.
                                             Defaults to ``True``.
`ADMINLTE_ALLOW_SOCIAL_AUTH`                 Allow users to log in using OAuth services.
                                             The option only affects the display of the template,
                                             the logic needs to be implemented.
                                             Defaults to ``False``.
`ADMINLTE_REMEMBER_ME`                       Allow users to remember them on the current device.
                                             The option only affects the display of the flag,
                                             the logic needs to be implemented.
                                             Defaults to ``False``.
`ADMINLTE_ALLOW_PASSWORD_RESET`              Allow users to recover a forgotten password.
                                             The option only affects the display of links,
                                             the logic needs to be implemented.
                                             Requires setting the value of the dependent options:
                                             ``ADMINLTE_PASSWORD_RESET_ENDPOINT`` and ``ADMINLTE_PASSWORD_RECOVER_ENDPOINT``.
                                             Defaults to ``True``.
`ADMINLTE_LANGUAGE_SWITCHER_ENABLED`         Allow users to select the current language.
                                             It is required to implement loading of available languages.
                                             Defaults to ``False``.
`ADMINLTE_MESSAGES_ENABLED`                  Enable the message widget in the navigation menu.
                                             It is required to implement loading of incoming messages.
                                             Defaults to ``False``.
`ADMINLTE_NOTIFICATIONS_ENABLED`             Enable the notification widget in the navigation menu.
                                             It is required to implement notification loading.
                                             Defaults to ``False``.
`ADMINLTE_SEARCH_ENABLED`                    The option allows displaying the search widget in the navigation menu and on error pages.
                                             The logic needs to be implemented.
                                             Requires setting the value of the dependent option ``ADMINLTE_SEARCH_ENDPOINT``.
                                             Defaults to ``False``.
`ADMINLTE_TASKS_ENABLED`                     Enable the the task widget in the navigation menu.
                                             Required to implement task loading.
                                             Defaults to ``False``.
**Endpoint names**
--------------------------------------------------------------------------------------------------
`ADMINLTE_CHANGE_LANGUAGE_ENDPOINT`          The name of the endpoint for changing the language.
                                             Defaults to ``'change_language'``.
`ADMINLTE_PROFILE_ENDPOINT`                  The name of the endpoint of the user profile.
                                             Defaults to ``'profile'``.
`ADMINLTE_SEARCH_ENDPOINT`                   The name of the endpoint for the search query.
                                             Defaults to ``'search'``.
`ADMINLTE_TERMS_ENDPOINT`                    The name of the endpoint to display the terms for using the service.
                                             Defaults to ``None``.
`ADMINLTE_REGISTRATION_ENDPOINT`             The name of the endpoint for user registration.
                                             Defaults to ``'auth.registration'``.
`ADMINLTE_LOGIN_ENDPOINT`                    The name of the endpoint for user login.
                                             Defaults to ``'auth.login'``.
`ADMINLTE_LOGOUT_ENDPOINT`                   The name of the endpoint for user logout.
                                             Defaults to ``'auth.logout'``.
`ADMINLTE_CHANGE_PASSWORD_ENDPOINT`          The name of the endpoint for changing the password.
                                             Defaults to ``'auth.change_password'``.
`ADMINLTE_PASSWORD_RESET_ENDPOINT`           The name of the endpoint for password reset.
                                             Defaults to ``'auth.reset_password'``.
`ADMINLTE_PASSWORD_RECOVER_ENDPOINT`         The name of the endpoint for password recovery.
                                             Defaults to ``'auth.recover_password'``.
=========================================    =====================================================


ADMINLTE_USER_MAPPING
^^^^^^^^^^^^^^^^^^^^^

ThemeColor
^^^^^^^^^^

.. csv-table::
   :header: "Code", "Hex", "From"

   `ThemeColor.PRIMARY`, ``#007bff``, Bootstrap
   `ThemeColor.SECONDARY`, ``#6c757d``, Bootstrap
   `ThemeColor.INFO`, ``#17a2b8``, Bootstrap
   `ThemeColor.SUCCESS`, ``#28a745``, Bootstrap
   `ThemeColor.WARNING`, ``#ffc107``, Bootstrap
   `ThemeColor.DANGER`, ``#dc3545``, Bootstrap
   `ThemeColor.WHITE`, ``#ffffff``, Bootstrap
   `ThemeColor.BLACK`, ``#000000``, Bootstrap
   `ThemeColor.GRAY_DARK`, ``#343a40``, Bootstrap
   `ThemeColor.GRAY`, ``#adb5bd``, Bootstrap
   `ThemeColor.LIGHT`, ``#1f2d3d``, Bootstrap
   `ThemeColor.INDIGO`, ``#6610f2``, AdminLTE
   `ThemeColor.LIGHTBLUE`, ``#3c8dbc``, AdminLTE
   `ThemeColor.NAVY`, ``#001f3f``, AdminLTE
   `ThemeColor.PURPLE`, ``#605ca8``, AdminLTE
   `ThemeColor.FUCHSIA`, ``#f012be``, AdminLTE
   `ThemeColor.PINK`, ``#e83e8c``, AdminLTE
   `ThemeColor.MAROON`, ``#d81b60``, AdminLTE
   `ThemeColor.ORANGE`, ``#ff851b``, AdminLTE
   `ThemeColor.LIME`, ``#01ff70``, AdminLTE
   `ThemeColor.TEAL`, ``#39cccc``, AdminLTE
   `ThemeColor.OLIVE`, ``#3d9970``, AdminLTE


ThemeLayout
^^^^^^^^^^^

In the application settings, set the parameter ``ADMINLTE_LAYOUT`` to:

**Top Navigation**

   ``ThemeLayout.TOP_NAV | ThemeLayout.COLLAPSED_SIDEBAR``

   Also disable sidebar: ``ADMINLTE_MAIN_SIDEBAR_ENABLED = False``

**Top Navigation + Sidebar**

   ``ThemeLayout.TOP_NAV | ThemeLayout.COLLAPSED_SIDEBAR``

**Boxed**

   ``ThemeLayout.DEFAULT | ThemeLayout.BOXED``

**Fixed Sidebar**

   ``ThemeLayout.DEFAULT | ThemeLayout.FIXED_SIDEBAR``

**Fixed Navbar**

   ``ThemeLayout.DEFAULT | ThemeLayout.FIXED_TOP_NAV``

**Fixed Footer**

   ``ThemeLayout.DEFAULT | ThemeLayout.FIXED_FOOTER``

**Collapsed Sidebar**

   ``ThemeLayout.DEFAULT | ThemeLayout.COLLAPSED_SIDEBAR``
