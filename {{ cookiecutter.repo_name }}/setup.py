from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name='{{ cookiecutter.repo_name }}',
    version=VERSION,
    author='{{ cookiecutter.author}}',
    discription='A cool CLI tool',
    include_package_data=True,
    packages=find_packages(exclude=('tests*', 'venv')),
    entry_points={'console_scripts': ['{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.__main__:main']},
    python_requires='>=3'
)
