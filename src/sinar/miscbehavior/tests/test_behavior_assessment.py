# -*- coding: utf-8 -*-
from sinar.miscbehavior.behaviors.assessment import IAssessmentMarker
from sinar.miscbehavior.testing import SINAR_MISCBEHAVIOR_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class AssessmentIntegrationTest(unittest.TestCase):

    layer = SINAR_MISCBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_assessment(self):
        behavior = getUtility(IBehavior, 'sinar.miscbehavior.assessment')
        self.assertEqual(
            behavior.marker,
            IAssessmentMarker,
        )
