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
class SDGGoals(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'sdg01', _(u'SDG 1 - No Poverty')),
            VocabItem(u'sdg02', _(u'SDG 2 - Zero Hunger')),
            VocabItem(u'sdg03', _(u'SDG 3 - Good Health and Well-Being')),
            VocabItem(u'sdg04', _(u'SDG 4 - Quality Education')),
            VocabItem(u'sdg05', _(u'SDG 5 - Gender Equality')),
            VocabItem(u'sdg06', _(u'SDG 6 - Clean Water and Sanitation')),
            VocabItem(u'sdg07', _(u'SDG 7 - Affordable and Clean Energy')),
            VocabItem(u'sdg08', _(u'SDG 8 - Decent Work and Economic Growth')),
            VocabItem(u'sdg09', _(u'SDG 9 - Industry, Innovation and Infrastructure')),
            VocabItem(u'sdg10', _(u'SDG 10 - Reduced Inequalities')),
            VocabItem(u'sdg11', _(u'SDG 11 - Sustainable Cities and Communities')),
            VocabItem(u'sdg12', _(u'SDG 12 - Responsible Consumption and Production')),
            VocabItem(u'sdg13', _(u'SDG 13 - Climate Action')),
            VocabItem(u'sdg14', _(u'SDG 14 - Life Below Water')),
            VocabItem(u'sdg15', _(u'SDG 15 - Life on Land')),
            VocabItem(u'sdg16', _(u'SDG 16 - Peace, Justice and Strong Institutions')),
            VocabItem(u'sdg17', _(u'SDG 17 - Partnerships for the Goals'))
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


SDGGoalsFactory = SDGGoals()
