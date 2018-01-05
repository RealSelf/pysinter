from setuptools import setup

setup(
	name="pysinter",
	version=1.0.1,
	description="Python 3 wrapper for the Sinter API",
	url="https://github.com/rsmichaeldunn/pysinter",
	author="Michael Dunn",
	author_email="michael.dunn@realself.com",
	license="MIT",
	install_requires=['requests', 'json'],
	packages=['pysinter'],
	keywords=['sinter', 'business intelligence', 'bi', 'etl', 'dbt']
	)
