DEFAULT_SETTINGS = {
    'ADMINLTE_SITE_TITLE': 'AdminLTE 3',

    'ADMINLTE_BRAND_TEXT': 'AdminLTE 3',
    'ADMINLTE_BRAND_IMAGE_ALT': 'AdminLTE Logo',
    'ADMINLTE_LEGACY_USER_MENU': False,

    'ADMINLTE_ALLOW_REGISTRATION': True,
    'ADMINLTE_REMEMBER_ME': True,
    'ADMINLTE_PASSWORD_RESET': True,
    'ADMINLTE_MESSAGES_ENABLED': False,
    'ADMINLTE_NOTIFICATIONS_ENABLED': False,
    'ADMINLTE_TASKS_ENABLED': False,

    'ADMINLTE_REGISTRATION_ENDPOINT': 'auth.registration',
    'ADMINLTE_LOGIN_ENDPOINT': 'auth.login',
    'ADMINLTE_LOGOUT_ENDPOINT': 'auth.logout',
    'ADMINLTE_CHANGE_PASSWORD_ENDPOINT': 'auth.change_password',
    'ADMINLTE_PASSWORD_RESET_ENDPOINT': 'auth.reset_password',
    'ADMINLTE_PASSWORD_RECOVER_ENDPOINT': 'auth.recover_password',

    'ADMINLTE_PROFILE_ENDPOINT': 'user.profile',
}


# Color styles

class ThemeColor(object):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    SUCCESS = 'success'
    DANGER = 'danger'
    WARNING = 'warning'
    INFO = 'info'
    LIGHT = 'light'
    DARK = 'dark'
    MUTED = 'muted'


# Flash message levels
DEBUG = 'debug'
ERROR = 'error'
WARNING = 'warning'
INFO = 'info'
SUCCESS = 'success'
MESSAGE = 'message'


# Flash message styles
ALERTS = {
    DEBUG: (ThemeColor.SECONDARY, 'fas fa-bug'),
    ERROR: (ThemeColor.DANGER, 'fas fa-ban'),
    WARNING: (ThemeColor.WARNING, 'fas fa-exclamation-triangle'),
    INFO: (ThemeColor.INFO, 'fas fa-info'),
    MESSAGE: (ThemeColor.INFO, 'fas fa-info'),
    SUCCESS: (ThemeColor.SUCCESS, 'fas fa-check'),
}
