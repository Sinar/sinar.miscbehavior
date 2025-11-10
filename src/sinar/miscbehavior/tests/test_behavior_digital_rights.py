# -*- coding: utf-8 -*-
from sinar.miscbehavior.behaviors.digital_rights import IDigitalRightsMarker
from sinar.miscbehavior.testing import SINAR_MISCBEHAVIOR_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DigitalRightsIntegrationTest(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_digital_rights(self):
        behavior = getUtility(IBehavior, 'sinar.miscbehavior.digital_rights')
        self.assertEqual(
            behavior.marker,
            IDigitalRightsMarker,
        )
