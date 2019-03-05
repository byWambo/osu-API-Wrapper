import re

import sys

from setuptools import find_packages, setup



if sys.version_info < (3, 5, 2):

    raise SystemExit('Upgrade your Python to 3.5+, you shitter!')



with open('README.md', encoding='utf-8') as f:

    readme = f.read()







with open('osu/__init__.py', 'r') as f:

    match = re.search(r'^__version__\s=\s\'(\d.\d.\d([ab])?)\'$', f.read(), re.MULTILINE)

    version = match.group(1)



extras_require = {

    'docs': ['sphinx==1.8.2', 'sphinx_rtd_theme>=0.4.2', 'sphinx-autodoc-typehints', 'sphinxcontrib-napoleon'],

    'performance': ['ujson>=0.35', 'earl-etf==2.1.2'],

}



setup(

    name='osu',

    version=version,

    author='byWambo',

    description='A framework to interact with the OSU! API.',

    long_description=readme,

    long_description_content_type='text/markdown',

    url='https://github.com/byWambo/osu-API-Wrapper',

    license='GNU General Public License v3 (GPLv3)',

    packages=find_packages(),

    include_package_data=True,

    install_requires=requirements,

    extras_require=extras_require,

    classifiers=[

        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Natural Language :: English',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.6',

        'Programming Language :: Python :: 3.7',

        'Topic :: Software Development :: Libraries',

        'Topic :: Software Development :: Libraries :: Python Modules',

        'Topic :: Utilities',

    ]

)
