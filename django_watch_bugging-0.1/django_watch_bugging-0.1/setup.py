import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_watch_bugging',
    version='0.1',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    py_modules = ['templates'],
    license='MIT License',  # example license
    description='Django Watch Bugging is used to monitor the VBP application usages.',
    long_description=README,
    url='https://otextcity.com/9-blog/3-vtu-business-selling-airtime-data-gotv-dstv-startimes-electricity-bills.html',
    author='Olayanju A. Ajibola',
    author_email='vtubusinessportal@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
