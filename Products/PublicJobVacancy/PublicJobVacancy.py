# -*- coding: utf-8 -*-
#
# File: PublicJobVacancy.py
##
# GNU General Public License (GPL)

__author__ = """Syslab.com GmbH <info@syslab.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *

try:
    from Products.LinguaPlone.public import *
except ImportError:
    HAS_LINGUAPLONE = False
else:
    HAS_LINGUAPLONE = True

from zope.interface import implements
from interfaces import IPublicJobVacancy

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.PublicJobVacancy.config import *

from Products.RichDocument.content.richdocument import RichDocument
from Products.RichDocument.content.richdocument import \
    RichDocumentSchema as BaseSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

if HAS_LINGUAPLONE:
    from Products.LinguaPlone.public import registerType
else:
    from Products.Archetypes.public import registerType

from Products.PublicJobVacancy import JobMessageFactory as _

schema = Schema((

    StringField(
        name='author',
        widget=StringWidget(
            size=80,
            label=_(u'job_author_label', default=u"Author"),
            description=_(u'job_author_description',
                          u"The author issuing the job"),
        )
    ),

    DateTimeField(
        name='deadline',
        required=True,
        widget=CalendarWidget(
            size="CalendarWidget",
            label=_(u'job_deadline_label', default="Deadline"),
            description=_(u'job_deadline_description',
                          default=u"The deadline for this job vacancy"),
        ),
        languageIndependent=True
    ),

    BooleanField(
        name='shortlisted',
        widget=BooleanField._properties['widget'](
            label=_(u'job_shortlisted_label', default=u"Shortlisted"),
            description=_(u'job_shortlisted_description',
                          default=u"Has this job vacancy been shortlisted?"),
        ),
        languageIndependent=True
    ),

),
)


PublicJobVacancy_schema = BaseSchema.copy() + schema.copy()
finalizeATCTSchema(PublicJobVacancy_schema)


class PublicJobVacancy(BrowserDefaultMixin, BaseContent, RichDocument):
    """Public Job Vacancy type"""

    security = ClassSecurityInfo()
    implements(IPublicJobVacancy)
    meta_type = 'PublicJobVacancy'
    _at_rename_after_creation = True

    schema = PublicJobVacancy_schema


registerType(PublicJobVacancy, PROJECTNAME)
