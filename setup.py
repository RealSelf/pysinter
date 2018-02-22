from setuptools import setup

setup(
	name="pysinter",
	version="1.0.5",
	description="Python 3 wrapper for the Sinter API",
	url="https://github.com/RealSelf/pysinter",
	author="Michael Dunn",
	author_email="michael.dunn@realself.com",
	classifiers=['Programming Language :: Python :: 3 :: Only'],
	license="BSD-3-Clause",
	install_requires=['requests'],
	packages=['pysinter'],
	keywords=['sinter', 'business intelligence', 'bi', 'etl', 'dbt']
	)
