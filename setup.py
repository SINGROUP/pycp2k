from setuptools import setup
import inputparser


#===============================================================================
# START SETUP
print "Parsing the cp2k input structure:"
inputparser.main()

setup(name='pycp2k',
      version='0.1',
      description='A python interface to CP2K',
      url='https://github.com/lauri-codes/pycp2k.git',
      author='Lauri Himanen',
      author_email='lauri.himanen@gmail.com',
      license='GPL3',
      packages=['pycp2k'],
      zip_safe=False)
