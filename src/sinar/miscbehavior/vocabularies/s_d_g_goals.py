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
            VocabItem(u'No poverty', _(u'No poverty')),
            VocabItem(u'Zero hunger', _(u'Zero hunger')),
	VocabItem(u'Good health and well-being', _(u'Good Health and well-being')),
	VocabItem(u'Quality education', _(u'Quality education')),
	VocabItem(u'Gender Equality', _(u'Gender Equality')),
	VocabItem(u'Clean Water and Sanitation', _(u'Clean Water and Sanitation')),
	VocabItem(u'Affordable and Clean Energy', _(u'Affordable and Clean Energy')),
	VocabItem(u'Decent Work and Economic Growth', _(u'Decent Work and Economic Growth')),
	VocabItem(u'Industry,Innovation and Infrastructure', _(u'Industry,Innovation and Infrastructure')),
	VocabItem(u'Reduced Inequalities', _(u'Reduced Inequalities')),
	VocabItem(u'Sustainable Cities and Communities', _(u'Sustainable Cities and Communities')),
	VocabItem(u'Responsible Consumption and Production', _(u'Responsible Consumption and Production')),
	VocabItem(u'Climate Action', _(u'Climate Action')),
	VocabItem(u'Life Below Water', _(u'Life Below Water')),
	VocabItem(u'Life on Land', _(u'Life on Land')),
	VocabItem(u'Peace, Justice and Strong Institution', _(u'Peace, Justice and Strong Institution')),_
	VocabItem(u'Partnerships for the Goals', _(u'Partnerships for the Goals'))
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
