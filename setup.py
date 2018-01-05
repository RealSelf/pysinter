from setuptools import setup

setup(
	name="pysinter",
	version=1.0,
	description="Python 3 wrapper for the Sinter API",
	url="https://github.com/rsmichaeldunn/pysinter",
	download_url='https://github.com/rsmichaeldunn/pysinter/archive/1.0.tar.gz',
	author="Michael Dunn",
	author_email="michael.dunn@realself.com",
	license="MIT",
	install_requires=['requests', 'json'],
	packages=['pysinter'],
	keywords=['sinter', 'business intelligence', 'bi', 'etl', 'dbt']
	)
