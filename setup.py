from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()



readme = ''
with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'voice': ['PyNaCl>=1.3.0,<1.5'],
    'docs': [
        'sphinx==4.0.2',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
    ],
    'speed': [
        'orjson>=3.5.4',
    ]
}

packages = [
    'discord',
    'discord.types',
    'discord.ui',
    'discord.webhook',
    'discord.ext.commands',
    'discord.ext.tasks',
]

setup(name='echo-discord.py',
      author='culanndog3',
      url='https://github.com/cbrown7752/echo-discord.py',
      project_urls={
        "Documentation": "https://github.com/cbrown7752/echo-discord.py",
        "Issue tracker": "https://github.com/cbrown7752/echo-discord.py/issues",
      },
      version='1.2.6',
      packages=packages,
      license='MIT',
      description='A Python wrapper for the Discord API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]
)


