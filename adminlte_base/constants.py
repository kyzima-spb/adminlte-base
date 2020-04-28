DEFAULT_SETTINGS = {
    'ADMINLTE_SITE_TITLE': 'AdminLTE 3',

    'ADMINLTE_BRAND_TEXT': 'AdminLTE 3',
    'ADMINLTE_BRAND_IMAGE_ALT': 'AdminLTE Logo',

    'ADMINLTE_ALLOW_REGISTRATION': True,
    'ADMINLTE_REGISTRATION_ENDPOINT': 'auth.registration',
    'ADMINLTE_LOGIN_ENDPOINT': 'auth.login',
    'ADMINLTE_LOGOUT_ENDPOINT': 'auth.logout',

    'ADMINLTE_PROFILE_ENDPOINT': 'user.profile',
    'ADMINLTE_PASSWORD_RESET': True,
    'ADMINLTE_PASSWORD_RESET_ENDPOINT': 'user.reset_password',
}


# Flash message levels
DEBUG = 'debug'
ERROR = 'error'
WARNING = 'warning'
INFO = 'info'
SUCCESS = 'success'
MESSAGE = 'message'


# Flash message styles
ALERTS = {
    DEBUG: ('debug', 'fas fa-bug'),
    ERROR: ('danger', 'fas fa-ban'),
    WARNING: ('warning', 'fas fa-exclamation-triangle'),
    INFO: ('info', 'fas fa-info'),
    MESSAGE: ('info', 'fas fa-info'),
    SUCCESS: ('success', 'fas fa-check'),
}
