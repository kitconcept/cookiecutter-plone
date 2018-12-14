# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from {{cookiecutter.package_name}}.testing import {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING  # noqa
from plone import api

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:  # Plone < 5.1
    HAS_INSTALLER = False
else:
    HAS_INSTALLER = True

import unittest


class TestSetup(unittest.TestCase):
    """Test that {{cookiecutter.package_name}} is properly installed."""

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal)
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if {{cookiecutter.package_name}} is installed."""
        if HAS_INSTALLER:
            self.assertTrue(
                self.installer.is_product_installed('{{cookiecutter.package_name}}')
            )
        else:
            self.assertTrue(
                self.installer.isProductInstalled(
                    '{{cookiecutter.package_name}}'
                )
            )

    def test_browserlayer(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is registered."""
        from {{cookiecutter.package_name}}.interfaces import (
            I{{cookiecutter.project_slug.capitalize()}}CoreLayer)
        from plone.browserlayer import utils
        self.assertIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = {{cookiecutter.project_slug.upper()}}FAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal)
            self.installer.uninstall_product('{{cookiecutter.package_name}}')
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
            self.installer.uninstallProducts(['{{cookiecutter.package_name}}'])

    def test_product_uninstalled(self):
        """Test if {{cookiecutter.package_name}} is cleanly uninstalled."""
        if HAS_INSTALLER:
            self.assertFalse(
                self.installer.is_product_installed('{{cookiecutter.package_name}}')
            )
        else:
            self.assertFalse(
                self.installer.isProductInstalled(
                    '{{cookiecutter.package_name}}'
                )
            )

    def test_browserlayer_removed(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is removed."""
        from {{cookiecutter.package_name}}.interfaces import I{{cookiecutter.project_slug.capitalize()}}CoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())
