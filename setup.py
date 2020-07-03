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
        'local_scheme': lambda version: '',
    },
    description='A basic package to simplify the integration of AdminLTE with other frameworks.',
    long_description=readme,
    url='https://github.com/kyzima-spb/adminlte-base',
    license='MIT',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'arrow',
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
