# -*- coding: utf-8 -*-

# from plone import api
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer
from plone.app.vocabularies.catalog import StaticCatalogVocabulary




@implementer(IVocabularyFactory)
class DigitalRights(object):
    """
    """

    def __call__(self, context):
        return StaticCatalogVocabulary(
            {
                # possible portal_types:
                "portal_type": [
                    "Event",
                ]
            },
            # customizable title of the Choice items, by default brain.Title:
            title_template="{brain.Title}",
        )


DigitalRightsFactory = DigitalRights()
