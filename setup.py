from setuptools import setup
import optimize_upip


setup(name='pycopy-filedb',
      version='0.4',
      description="""Very simple, filesystem-based ORM (Object-Relational \
Mapper) for Pycopy (https://github.com/pfalcon/pycopy).
""",
      url='https://github.com/pfalcon/pycopy-filedb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      py_modules=['filedb'])
