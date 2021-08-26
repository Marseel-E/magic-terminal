from setuptools import setup, find_packages

classifiers = [
    'Developement Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'Magic',
    version = '0.0.1',
    description = "A fun & friendly way to display text in your terminal",
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOGS.txt').read(),
    url = '',
    author = 'Marseel Eeso',
    author_email = 'marseeleeso@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = '',
    packages = find_packages(),
    install_required = ['']
)
