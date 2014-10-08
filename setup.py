from setuptools import setup
import inputparser


#===============================================================================
# START SETUP
print "================================================================================"
print "Parsing the cp2k input structure..."
print "================================================================================"

if inputparser.main():
    print "\n================================================================================"
    print "Installing package..."
    print "================================================================================"

    setup(name='pycp2k',
          version='0.1',
          description='A python interface to CP2K',
          url='https://github.com/lauri-codes/pycp2k.git',
          author='Lauri Himanen',
          author_email='lauri.himanen@gmail.com',
          license='GPL3',
          packages=['pycp2k'],
          zip_safe=False)

    print "\n================================================================================"
    print "Installation completed succesfully!"
    print "================================================================================"

else:
    print "\n================================================================================"
    print "Installation failed."
    print "================================================================================"
