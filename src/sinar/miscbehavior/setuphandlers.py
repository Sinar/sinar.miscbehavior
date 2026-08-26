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
    prefixes = (
        'plone.app.querystring.field.countries',
        'plone.app.querystring.field.SDG_goals',
        'plone.app.querystring.field.digital_rights_categories',
    )
    for prefix in prefixes:
        # <records> elements store one entry per value key: "<prefix>.<key>".
        # Delete everything under the prefix using a range scan — iterating
        # the whole registry fails on sites with mixed str/int record keys.
        for key in registry.records.keys(min=prefix, max=prefix + '\x7f'):
            if key == prefix or key.startswith(prefix + '.'):
                del registry.records[key]
