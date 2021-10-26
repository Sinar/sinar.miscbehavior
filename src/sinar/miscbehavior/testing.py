# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.miscbehavior


class SinarMiscbehaviorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.miscbehavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.miscbehavior:default')


SINAR_MISCBEHAVIOR_FIXTURE = SinarMiscbehaviorLayer()


SINAR_MISCBEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_MISCBEHAVIOR_FIXTURE,),
    name='SinarMiscbehaviorLayer:IntegrationTesting',
)


SINAR_MISCBEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_MISCBEHAVIOR_FIXTURE,),
    name='SinarMiscbehaviorLayer:FunctionalTesting',
)


SINAR_MISCBEHAVIOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_MISCBEHAVIOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarMiscbehaviorLayer:AcceptanceTesting',
)
