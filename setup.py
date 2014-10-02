from setuptools import setup
import inputparser


#===============================================================================
# START SETUP
print "Parsing the cp2k input structure:"
inputparser.main()

setup(name='cp2kase',
      version='0.1',
      description='An ASE interface to CP2K',
      url='https://github.com/lauri-codes/cp2kase.git',
      author='Lauri Himanen',
      author_email='lauri.himanen@aalto.fi',
      license='GPL3',
      packages=['cp2kase'],
      zip_safe=False)
