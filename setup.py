from setuptools import setup, find_packages


def setup_manual():
    setup(
        name='pycp2k',
        version='0.2.1',
        description='A python interface to CP2K',
        url='https://github.com/SINGROUP/pycp2k.git',
        author='Lauri Himanen',
        author_email='lauri.himanen@gmail.com',
        license='MIT',
        packages=find_packages(),
        install_requires=[
            'future',
            'numpy',
            'ase',
        ],
        zip_safe=False)

if __name__ == "__main__":
    setup_manual()
