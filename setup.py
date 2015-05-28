
from setuptools import setup, find_packages, Command

from distutils.core import setup, Command
# you can also import from setuptools

class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name = 'bype',
    packages = find_packages(),
    version = '0.1a',
    description = 'Python Fluent DSL',
    author = 'Maxim Yaskevich',
    author_email = 'yaskevichmaxim@gmail.com',
    license='MIT',
    tests_require=['pytest'],
    test_suite='test',
    cmdclass = {'test': PyTest},
    url = 'https://github.com/myaskevich/python-bype',
    keywords = ['dsl', 'fluent', 'test'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
    ],
)
