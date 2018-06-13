'''
This python command line interface, executes calls to the Aptly server
remotely, without blocking the Aptly database. All functionality from here
http://www.aptly.info/doc/api/ is extended by even more useful features, like
showing or cleaning out snapshots, packages for couple of repos or mirrors.

You can make either use of the aptly_api_request.py as a starting point for
your own application or just use the cli (aptly_api_cli.py) bundled with this
repository to execute your requests via command line or run scripts, calling
the cli, integrated into a CI Workflow.
'''

from distutils.core import setup

setup(
    name='Aptly-Api-Cli',
    version='0.3',
    install_requires=[
      'requests >= 2.6.0',
      'simplejson >= 3.3.2',
    ],
    url='https://github.com/TimSusa/aptly_api_cli',
    license='MIT',
    keywords="aptly aptly-server debian",
    author='Tim Susa',
    author_email='timsusa@gmx.de',
    description='This cli executes remote calls to the Aptly server, without blocking the Aptly database.',
    long_description=__doc__,
    packages=['aptly_cli', 'aptly_cli.api', 'aptly_cli.cli', 'aptly_cli.util'],
    scripts=['./aptly_api_cli'],
    platforms='any'
)
