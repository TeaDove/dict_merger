#!/usr/bin/env python3

from os.path import dirname, join
from pathlib import Path
from typing import FrozenSet, List, Optional

from Cython.Build import cythonize

from setuptools import find_packages, setup


def get_ext_paths(
    directory: Path,
    exclude_files: FrozenSet[str] = frozenset(),
    paths: Optional[List[str]] = None,
) -> List[str]:
    if paths is None:
        paths = []

    for file in directory.iterdir():
        if file.is_dir():
            paths.extend(get_ext_paths(file, exclude_files))

        if file.suffix not in (".py", ".pyx"):
            continue

        if file.name in exclude_files:
            continue

        paths.append(str(file))
    return paths


# with open("stdout", "w") as f:
#     f.write("\n".join(get_ext_paths(Path("src/dict_merger"))))

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

compiler_directives = {"language_level": 3, "embedsignature": True}
setup(
    name="dict_merger",
    version="0.0.1",
    packages=find_packages("src"),
    ext_modules=cythonize(get_ext_paths(Path("src")), compiler_directives=compiler_directives),
    install_requires=[],
    package_dir={"": "src"},
    long_description=open(join(dirname(__file__), "README.md")).read(),
)
