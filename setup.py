import sys
import os
from distutils.core import setup
prjdir = os.path.dirname(__file__)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

extra_link_args = []
libraries = []
library_dirs = []
include_dirs = []
exec(open('version.py').read())
setup(
    name='DiFF_RF',
    version=__version__,
    author='Pierre-F. Marteau, from Matias Carrasco code @ https://github.com/xhan0909/isolation_forest',
    author_email='pierre-francois.marteau@irisa.fr',
    scripts=[],
    py_modules=['DiFF_RF','version'],
    packages=[],
    license='License.txt',
    description='Distance based ensemble of random partitioning trees for anomaly detection',
    long_description=read('README.md'),
    #url='https://github.com/mgckind/iso_forest',
)
