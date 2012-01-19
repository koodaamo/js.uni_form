from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='js.uni_form',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='fanstatic',
      author='Petri Savolainen',
      author_email='petri.savolainen@koodaamo.fi',
      url='https://github.com/koodaamo/js.uni_form',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'fanstatic'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [fanstatic.libraries]
      uni_form = js.uni_form:library
      # -*- Entry points: -*-
      """,
      )
