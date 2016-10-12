from setuptools import setup


setup(name='micropython-filedb',
      version='0.1.2',
      description="""Very simple, filesystem-based ORM (Object-Relational
Mapper) for MicroPython.
""",
      url='https://github.com/pfalcon/filedb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      py_modules=['filedb'],
      install_requires=['micropython-os'])
