#!/usr/bin/env python3

from os.path import dirname, join
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name="dict_merger",
        sources=["src/dict_merger/__init__.pyx"],
        language="c",
    ),
    # Extension(
    #     name="dict_merger.pure_merger",
    #     sources=["src/dict_merger/pure_merger.py"],
    # ),
]

compiler_directives = {"language_level": 3, "embedsignature": True}
setup(
    name="dict_merger",
    version="0.0.1",
    packages=find_packages(),
    ext_modules=cythonize(ext_modules, compiler_directives=compiler_directives),
    install_requires=[],
    long_description=open(join(dirname(__file__), "README.md")).read(),
)
