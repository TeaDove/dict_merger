.PHONY: build dist redist install install-from-source clean uninstall

build:
	CYTHONIZE=true python3.10 ./setup.py build_ext --inplace

dist:
	python3.10 setup.py sdist bdist_wheel

upload:
	twine upload --repository pypi dist/*

redist: clean dist

install:
	python3.10 setup.py build_ext --inplace
	python3.10 -m pip install .

clean:
	$(RM) -r build dist src/*.egg-info
	$(RM) -r src/dict_merger/*.so
	$(RM) -r src/*.so
	$(RM) -r *.so
	$(RM) -r .pytest_cache
	find . -name __pycache__ -exec rm -r {} +

uninstall:
	python3.10 -m pip uninstall -y dict_merger

reinstall:
	make uninstall && make clean && make install
