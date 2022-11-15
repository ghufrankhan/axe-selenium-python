axe-selenium-python-nhsuk
*************************

axe-selenium-python-nhsuk integrates aXe and Selenium to enable automated web accessibility testing.

**This version of axe-selenium-python-nhsuk is using axe-core v4.4.3.**

Information
===========

| This package is derived from `axe-selenium-python 2.1.6 <https://pypi.org/project/axe-selenium-python/2.1.6/>`_.
| The main purpose of creating a new package was to allow us to update the axe-core version and push to PyPi. The original package has not been updated since 2018.

Installation
============

To install axe-selenium-python-nhsuk:

.. code-block:: bash

  $ pip install axe-selenium-python-nhsuk

Usage & CHANGELOG
=================

For Usage and CHANGELOG, go to: https://pypi.org/project/axe-selenium-python/

Updating & Deployment to PyPi
=============================

Update files
------------
Create a new branch and make the following changes:

- **axe_selenium_python/axe_selenium_python/package-lock.json** - Update line 8-10 using information found `here <https://github.com/dequelabs/axe-core/blob/develop/package-lock.json>`_ - search for 'axe-core' to find the relevant info
- **axe-selenium-python/axe_selenium_python/package.json** - Update line 16 (use the same version you set in the file above on line 8)
- **axe-selenium-python/setup.py** - Increase the version number on line 13 - e.g. 1.0.1 > 1.0.2 (this new version number will also be used as a GitHub release tag)

Create a Pull Request and merge your changes to the master branch.

Deploy to PyPi
--------------
- On GitHub.com, navigate to the main page of the repository
- To the right of the list of files, click **Releases**
- Click **Create a new release**
- Click **Choose a tag**, type the same version number you set in *axe-selenium-python/setup.py*, click **Create a new tag**
- Ensure the *Target* is set to **master**
- Enter a *Release title* - e.g. Release axe-core version 4.4.3
- If required, enter additional text in the Release decription
- Click **Publish release**

If the release is successful then it should appear on PyPi in a few minutes.
