# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from sinar.miscbehavior.behaviors.s_d_g_goals import ISDGGoalsMarker
from sinar.miscbehavior.testing import SINAR_MISCBEHAVIOR_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class SDGGoalsIntegrationTest(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_s_d_g_goals(self):
        behavior = getUtility(IBehavior, 'sinar.miscbehavior.s_d_g_goals')
        self.assertEqual(
            behavior.marker,
            ISDGGoalsMarker,
        )
