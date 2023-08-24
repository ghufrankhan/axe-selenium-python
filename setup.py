# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from setuptools import setup

with open("./README.rst") as f:
    readme = f.read()

setup(
    name="axe-selenium-python-nhsuk",
    version="1.0.2",
    description="Python library to integrate axe and selenium for web \
                accessibility testing.",
    long_description=open("README.rst").read(),
    url="https://github.com/ghufrankhan/axe-selenium-python",
    packages=["axe_selenium_python", "axe_selenium_python.node_modules", "axe_selenium_python.tests"],
    package_data={
        "axe_selenium_python": [
            "axe_selenium_python/node_modules/axe-core/axe.min.js",
            "axe_selenium_python/tests/test_page.html",
        ]
    },
    include_package_data=True,
    install_requires=["selenium>=4.0.0"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="axe-core axe python selenium accessibility testing automation",
)
