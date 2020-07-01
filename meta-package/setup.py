import os

from setuptools import setup


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


readme = read_file('README.rst')

setup(
    name='adminlte-full',
    version='0.1.0',
    # use_scm_version={
    #     'relative_to': __file__,
    #     'local_scheme': lambda version: '',
    # },
    description='A metapackage',
    long_description=readme,
    license='MIT',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    # setup_requires=['setuptools_scm'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
