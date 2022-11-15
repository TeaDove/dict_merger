.PHONY: build dist redist install install-from-source clean uninstall

build:
	./setup.py build

dist:
	./setup.py sdist bdist_wheel

redist: clean dist

install:
	python3 setup.py build_ext --inplace
	pip install .

install-from-source: dist
	pip install dist/cython-package-example-0.1.6.tar.gz

clean:
	$(RM) -r build dist src/*.egg-info
	$(RM) -r src/dict_merger/*.so
	$(RM) -r src/*.so
	$(RM) -r *.so
	$(RM) -r .pytest_cache
	find . -name __pycache__ -exec rm -r {} +
	#git clean -fdX

uninstall:
	pip uninstall -y dict_merger

reinstall:
	make uninstall && make clean && make install
