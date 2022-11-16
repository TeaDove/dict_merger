#!/usr/bin/env python3

import os
from os.path import dirname, join, splitext
from pathlib import Path
from typing import FrozenSet, List, Optional

from setuptools import Extension, find_packages, setup

try:
    from Cython.Build import cythonize  # isort:skip
except ImportError:
    print("Warning: Cython is not installed")
    cythonize = None


# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules
def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in (".pyx", ".py"):
                if extension.language == "c++":
                    ext = ".cpp"
                else:
                    ext = ".c"
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions


def compile_module_name(file: Path):
    # src/
    return splitext(str(file))[0].replace("/", ".")[4:]


def get_ext_paths(
    directory: Path,
    exclude_files: FrozenSet[str] = frozenset(),
    paths: Optional[List[str]] = None,
) -> List[Extension]:
    if paths is None:
        paths = []

    for file in directory.iterdir():
        if file.is_dir():
            paths.extend(get_ext_paths(file, exclude_files))
            continue

        if file.suffix not in (".py", ".pyx"):
            continue

        if file.name in exclude_files:
            continue

        paths.append(Extension(compile_module_name(file), [str(file)]))
    return paths


# with open("stdout", "w") as f:
#     f.write(str(cythonize(get_ext_paths(Path("src")))))

# ext_modules = [
#     Extension(
#         name="dict_merger",
#         sources=get_ext_paths(Path("src/dict_merger")),
#         language="c",
#     ),
#     # Extension(
#     #     name="dict_merger.pure_merger",
#     #     sources=["src/dict_merger/pure_merger.py"],
#     # ),
# ]

exc_modules = get_ext_paths(Path("src"))

CYTHONIZE = (os.getenv("CYTHONIZE", "false") == "true") and (cythonize is not None)

if CYTHONIZE:
    compiler_directives = {"language_level": 3, "embedsignature": True}
    extensions = cythonize(exc_modules, compiler_directives=compiler_directives)
else:
    extensions = no_cythonize(exc_modules)

setup(
    name="dict_merger",
    version="0.0.3",
    author="Peter Ibragimov",
    description="Cython recursive dictionary merging",
    packages=find_packages("src"),
    ext_modules=exc_modules,
    package_dir={"": "src"},
    url="https://github.com/TeaDove/dict_merger",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
)
