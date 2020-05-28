def replace_with_include(template):
    def f(_, **kwargs):
        return 'include', (f"'{template}'", 'with'), kwargs
    return f


GENERATOR_FUNCTIONS_MAPPER = {
    'sidebar_menu': replace_with_include('adminlte_full/markup/sidebar_menu.html'),
    'navbar_dropdown': replace_with_include('adminlte_full/markup/navbar_dropdown.html'),
}

GENERATOR_TEMPLATE_TAGS = {
    r'^adminlte\.[a-z0-9_]+$': 'adminlte_full',
    r'gravatar': 'adminlte_full',
    r'humanize': 'adminlte_full',
}
