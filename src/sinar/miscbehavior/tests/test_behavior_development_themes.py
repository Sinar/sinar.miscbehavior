# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from sinar.miscbehavior.behaviors.development_themes import IDevelopmentThemesMarker
from sinar.miscbehavior.testing import SINAR_MISCBEHAVIOR_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class DevelopmentThemesIntegrationTest(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_development_themes(self):
        behavior = getUtility(IBehavior, 'sinar.miscbehavior.development_themes')
        self.assertEqual(
            behavior.marker,
            IDevelopmentThemesMarker,
        )
