# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from {{cookiecutter.package_name}}.testing import {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING  # noqa
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that {{cookiecutter.package_name}} is properly installed."""

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if {{cookiecutter.package_name}} is installed."""
        self.assertTrue(
            self.installer.is_product_installed('{{cookiecutter.package_name}}')
        )

    def test_plone_restapi_installed(self):
        self.assertTrue(
            self.installer.is_product_installed(
                "plone.restapi"
            )
        )

    def test_browserlayer(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is registered."""
        from {{cookiecutter.package_name}}.interfaces import (
            I{{cookiecutter.project_slug.capitalize()}}CoreLayer)
        from plone.browserlayer import utils
        self.assertIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)
        self.installer.uninstall_product('{{cookiecutter.package_name}}')

    def test_product_uninstalled(self):
        """Test if {{cookiecutter.package_name}} is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed('{{cookiecutter.package_name}}')
        )

    def test_browserlayer_removed(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is removed."""
        from {{cookiecutter.package_name}}.interfaces import I{{cookiecutter.project_slug.capitalize()}}CoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())
