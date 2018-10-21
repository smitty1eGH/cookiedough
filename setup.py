from setuptools import setup

setup(
    name='cookiedough.py',
    version='0.1',
    py_modules=['cookiedough'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cookiedough=cookiedough:cli
    ''',
)
