# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.miscbehavior.testing import (  # noqa: E501,,,,,,,,,,
    SINAR_MISCBEHAVIOR_INTEGRATION_TESTING,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that sinar.miscbehavior is properly installed."""

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.miscbehavior is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'sinar.miscbehavior'))

    def test_browserlayer(self):
        """Test that ISinarMiscbehaviorLayer is registered."""
        from plone.browserlayer import utils
        from sinar.miscbehavior.interfaces import ISinarMiscbehaviorLayer
        self.assertIn(
            ISinarMiscbehaviorLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('sinar.miscbehavior')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.miscbehavior is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'sinar.miscbehavior'))

    def test_browserlayer_removed(self):
        """Test that ISinarMiscbehaviorLayer is removed."""
        from plone.browserlayer import utils
        from sinar.miscbehavior.interfaces import ISinarMiscbehaviorLayer
        self.assertNotIn(
            ISinarMiscbehaviorLayer,
            utils.registered_layers())
