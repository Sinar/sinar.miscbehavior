# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
# from plone import api
from sinar.miscbehavior import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class DevelopmentThemes(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'agriculture', _(u'Agriculture')),
            VocabItem(u'childrights', _(u'Child Rights')),
            VocabItem(u'crime', _(u'Crime')),
            VocabItem(u'environment', _(u'Environment')),
            VocabItem(u'economy', _(u'Economy')),
            VocabItem(u'education', _(u'Education')),
            VocabItem(u'energy', _(u'Energy')),
            VocabItem(u'health', _(u'Health')),
            VocabItem(u'humanrights', _(u'Human Rights')),
            VocabItem(u'indigenous', _(u'Indigenous Affairs')),
            VocabItem(u'labourrights', _(u'Labour Rights')),
            VocabItem(u'migrants', _(u'Migrants and Refugees')),
            VocabItem(u'procurement', _(u'Procurement and Contracts')),
            VocabItem(u'religion', _(u'Religious Affairs')),
            VocabItem(u'water', _(u'Water and Santitation')),
            VocabItem(u'women', _(u'Women and Gender')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


DevelopmentThemesFactory = DevelopmentThemes()
