.PHONY: build compile install clean uninstall dist upload recreate

package_name := dick_merger

build:
	CYTHONIZE=true ./setup.py build_ext --inplace

compile:
	CYTHONIZE=false python3.10 setup.py build_ext --inplace

install:
	python3.10 -m pip install .

clean:
	$(RM) -r build dist src/*.egg-info
	$(RM) -r src/**/*.so
	$(RM) -r src/*.so
	$(RM) -r *.so
	$(RM) -r .pytest_cache
	find . -name __pycache__ -exec rm -r {} +

uninstall:
	python3.10 -m pip uninstall -y ${package_name}

dist:
	python3.10 setup.py sdist bdist_wheel

upload:
	twine upload --repository pypi dist/*

recreate: uninstall clean build compile install
