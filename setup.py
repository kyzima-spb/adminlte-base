import os

from setuptools import setup, find_packages


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


readme = read_file('README.rst')


setup(
    name='adminlte-base',
    use_scm_version={
        'relative_to': __file__,
    },
    url='https://github.com/kyzima-spb/adminlte-base',
    description='A basic package to simplify the integration of AdminLTE with other frameworks.',
    long_description=readme,
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            # 'adminlte=adminlte_base.cli:cli',
        ],
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'arrow',
        'Click>=7.1,<8',
        'colorama',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
