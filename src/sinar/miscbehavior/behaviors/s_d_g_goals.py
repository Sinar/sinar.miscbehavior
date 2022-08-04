# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from sinar.miscbehavior import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class ISDGGoalsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ISDGGoals(model.Schema):
    """
    """

    directives.widget(SDG_goals=SelectFieldWidget)
    SDG_goals = schema.List(
        title=_(u'SDG Goals'),
        description=_(u'SDG Goals applicable to content'),
        required=False,
        value_type=schema.Choice(
            vocabulary="sinar.miscbehavior.SDGGoals",
        ),
    )

    fieldset(
            'categorization',
            fields=[
                'SDG_goals',
                ],
            )

@implementer(ISDGGoals)
@adapter(ISDGGoalsMarker)
class SDGGoals(object):
    def __init__(self, context):
        self.context = context

    @property
    def SDG_goals(self):
        if safe_hasattr(self.context, 'SDG_goals'):
            return self.context.SDG_goals
        return None

    @SDG_goals.setter
    def SDG_goals(self, value):
        self.context.SDG_goals = value
