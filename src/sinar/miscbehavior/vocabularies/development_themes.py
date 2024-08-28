# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
# from plone import api
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
            VocabItem('accessibility', 'Accessibility'),
            VocabItem('accountability', 'Accountability and Transparency'),
            VocabItem('agriculture', 'Agriculture'),
            VocabItem('childrights', 'Child Rights'),
            VocabItem('crime', 'Crime'),
            VocabItem('environment', 'Environment'),
            VocabItem('economy', 'Economy'),
            VocabItem('education', 'Education'),
            VocabItem('energy', 'Energy'),
            VocabItem('health', 'Health'),
            VocabItem('humanrights', 'Human Rights'),
            VocabItem('indigenous', 'Indigenous Affairs'),
            VocabItem('infrastructure', 'I'),
            VocabItem('labourrights', 'Labour Rights'),
            VocabItem('migrants', 'Migrants and Refugees'),
            VocabItem('legislative', 'Legislative Assemblies and Parliament'),
            VocabItem('procurement', 'Procurement and Contracts'),
            VocabItem('religion', 'Religious Affairs'),
            VocabItem('transportation', 'Transportation'),
            VocabItem('water', 'Water and Santitation'),
            VocabItem('women', 'Women and Gender'),
            VocabItem('accessibility', 'Accessibility'),
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
