from setuptools import setup, find_packages

requires = ['dateparser']

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    install_requires = requires,
    entry_points = {'scrapy': ['settings = A353949.settings']},
)
