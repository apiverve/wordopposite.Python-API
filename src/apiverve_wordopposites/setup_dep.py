from setuptools import setup, find_packages

setup(
    name='apiverve_wordopposites',
    version='1.1.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Word Opposites is a simple tool for getting the opposites of a word. It returns a list of opposites for the given word.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
