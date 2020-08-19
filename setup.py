from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(name='webhook test',
  author='kota05217',
  version='1.0.0',
  py_modules=['test'],
  url='https://github.com/kota05217/webhook-test',
  description='A simple discord webhook.',
  long_description=long_description,
  include_package_data=True,
  license='MIT Licence',
  install_requires=["requests==2.24.0"],
  python_requires='>=3.8.0',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)