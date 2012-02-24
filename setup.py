#!/usr/bin/env python
"""This program will show m17n keymap in keyboard UI."""
from distutils.core import setup

doclines = __doc__.split("\n")
setup(name='m17n-map-image',
      version='0.5',
      description=doclines[0],
      long_description = "\n".join(doclines[:]),
      platforms = ["Linux"],
      author='Parag Nemade',
      author_email='pnemade@redhat.com',
      url='',
      license = 'http://www.gnu.org/licenses/gpl.html',
      data_files=[('/usr/bin',['m17n-map-image']),
		  ('/usr/share/m17n-map-image/',['m17n-map-image.glade'])]
      )

