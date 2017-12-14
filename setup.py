from setuptools import setup

INSTALL_REQUIRES = ['simplejson']

EXTRAS_REQUIRE = {'xml': ['xmltodict']}

setup(
    name='nested-setup-top',
    version='',
    packages=['hello_world'],
    url='',
    license='',
    author='Gabriel Curio',
    author_email='',
    description='',
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE
)
