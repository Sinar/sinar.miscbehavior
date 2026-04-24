# -*- coding: utf-8 -*-
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'sinar.miscbehavior:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    registry = getUtility(IRegistry)
    keys = (
        'plone.app.querystring.field.countries',
        'plone.app.querystring.field.SDG_goals',
        'plone.app.querystring.field.digital_rights_categories',
    )
    for key in keys:
        registry.records.pop(key, None)
