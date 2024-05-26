from setuptools import setup, find_packages

setup(
    name='flask_app',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.1',
    ],
    entry_points={
        'console_scripts': [
            'flask_app=app:main',
        ],
    },
)

