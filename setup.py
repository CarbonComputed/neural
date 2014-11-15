from setuptools import setup, find_packages


setup(
    name="neural",
    version="0.1",
    description="Neural Networks",
    license="BSD",
    keywords="Neural Networks",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    test_suite='neural.tests.runtests.make_test_suite',
    install_requires = [],
)