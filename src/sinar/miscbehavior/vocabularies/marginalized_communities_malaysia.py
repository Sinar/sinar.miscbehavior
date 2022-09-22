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
class MarginalizedCommunitiesMalaysia(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'orang-asal-sabah', _(u'Orang Asal in Sabah')),
            VocabItem(u'orang-asal-sarawak', _(u'Orang Asal in Sarawak')),
            VocabItem(u'sex-workers', _(u'Sex Workers')),
            VocabItem(u'refugees', _(u'Refugees')),
            VocabItem(u'contract-labour', _(u'Contract Labour')),
            VocabItem(u'domestic-violence', _(u'Victims of Domestic Violence')),
            VocabItem(u'disabled', _(u'Persons with Disabilities')),
            VocabItem(u'rural-communities', _(u'Rural Communities')),
            VocabItem(u'stateless-persons', _(u'Stateles Persons')),
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


MarginalizedCommunitiesMalaysiaFactory = MarginalizedCommunitiesMalaysia()
