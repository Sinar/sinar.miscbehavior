# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from sinar.miscbehavior.behaviors.marginalized_communities_malaysia import (
    IMarginalizedCommunitiesMalaysiaMarker,
)
from sinar.miscbehavior.testing import SINAR_MISCBEHAVIOR_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class MarginalizedCommunitiesMalaysiaIntegrationTest(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_marginalized_communities_malaysia(self):
        behavior = getUtility(IBehavior, 'sinar.miscbehavior.marginalized_communities_malaysia')
        self.assertEqual(
            behavior.marker,
            IMarginalizedCommunitiesMalaysiaMarker,
        )
