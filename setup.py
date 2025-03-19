from setuptools import setup, find_packages

setup(
    name='cis301',
    version='0.3.0',
    license='MIT',
    description='CIS301 Projects and Examples',
    author='Ali Sazegar',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pytest-runner', 'pytest'],
    entry_points={
        'console_scripts': [
            'project3 = cis301.project3.__main__:main',
        ]
    },
)