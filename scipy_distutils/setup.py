#!/usr/bin/env python
import os
from distutils.core import setup
from misc_util import get_path 
   
def install_package():
    """ Install the scipy_distutils.  The dance with the current directory is done
        to fool distutils into thinking it is run from the scipy_distutils directory
        even if it was invoked from another script located in a different location.
    """
    path = get_path(__name__)
    old_path = os.getcwd()
    os.chdir(path)
    try:
        setup (name = "scipy_distutils",
               version = "0.1",
               description = "Changes to distutils needed for SciPy -- mostly Fortran support",
               author = "Travis Oliphant, Eric Jones, and Pearu Peterson",
               licence = "BSD Style",
               url = 'http://www.scipy.org',
               packages = ['scipy_distutils','scipy_distutils.command'],
               package_dir = {'scipy_distutils':path}
               )
    finally:
        os.chdir(old_path)
    
if __name__ == '__main__':
    install_package()
