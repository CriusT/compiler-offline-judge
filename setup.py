from setuptools import setup

setup(name='hello',
      license='MIT',
      packages=['compiler_oj'],
      entry_points = {
        'console_scripts': ['compiler-oj=compiler_oj.command_line:main'],
    })