# -*- coding: utf-8 -*-
"""Setup module."""
from typing import List
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires() -> List[str]:
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description() -> str:
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''Breathing gymnastics application'''


setup(
    name='nafas',
    packages=['nafas'],
    version='1.4',
    description='Breathing gymnastics application',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Nafas Development Team',
    author_email='me@sepand.tech',
    url='https://github.com/sepandhaghighi/nafas',
    download_url='https://github.com/sepandhaghighi/nafas/tarball/v1.4',
    keywords="breath breathing meditation yoga pranayama",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/nafas',
        'Discord': 'https://discord.gg/CtZUNKJHP4',
    },
    install_requires=get_requires(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Topic :: Games/Entertainment',
        'Topic :: Utilities',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'nafas = nafas.__main__:main',
        ]}
)
