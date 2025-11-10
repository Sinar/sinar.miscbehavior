# -*- coding: utf-8 -*-

# from plone import api
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value

@implementer(IVocabularyFactory)
class DigitalRights(object):
    """
    """

    def __call__(self, context):
        # List of digital rights related items for our vocabulary.
        # https://github.com/Sinar/sinar.miscbehavior/issues/14
        # create a list of SimpleTerm items:

        items = [
            VocabItem('ai', 'Artificial Intelligence'),
            VocabItem('algorithms', 'Algorithmic Accountability'),
            VocabItem('cloud', 'Cloud Computing and Data Centres'),
            VocabItem('consumer', 'Consumer Safety and Protection'),
            VocabItem('ipr', 'Intellectual Property Rights'),
            VocabItem('ogv', 'Online Gender Violence'),
            VocabItem('opendata', 'Open Data'),
            VocabItem('radiofreq', 'Radio Frequency Spectrum Management'),
            VocabItem('usp', 'Universal Services Provision'),
            VocabItem('platform', 'Platform Accountability'),
            VocabItem('igov', 'Inteternet Governance'),
            VocabItem('privacy', 'Privacy and Surveillance'),
            VocabItem('opendatastandards', 'Open Data Standards'),
            VocabItem('internetstandards', 'Open Internet Standards'),
        ]

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


DigitalRightsFactory = DigitalRights()
