from Products.PublicJobVacancy.browser.interfaces import IJobsListing
from Products.CMFCore.utils import getToolByName

from zope.interface import implements
from Products.Five.browser import BrowserView
from DateTime import DateTime
from DocumentTemplate import sequence
from Acquisition import aq_base


class JobsSortedListing(BrowserView):
    implements(IJobsListing)

    def getAdditionalText(self):
        context = self.context
        text = ''
        if getattr(aq_base(context), 'content', None):
            content = getattr(context, 'content')
            if hasattr(content, 'getText') and callable(content.getText):
                text = content.getText()
        return text

    def results(self):
        context = self.context
        portal_catalog = getToolByName(context, 'portal_catalog')
        res = portal_catalog({'portal_type':'PublicJobVacancy'
                                   , 'sort_on':'effective'
                                   , 'Language': 'all'
                                   , 'sort_order':'reverse'});
        effRes = list()
        cres = list()
        ores = list()
        sres = list()
        ares = list()
        date = DateTime()

        for r in res:
            try:
                o = r.getObject()
            except:
                continue
            pastEffective = ( r.effective is None or r.effective=='' or r.effective <= date )
            beforeExpiration = ( r.expires is None or r.expires=='' or r.expires >= date )
            if r.effective is None and r.expires is None:
                continue

            if pastEffective:
                if beforeExpiration:
                    effRes.append(r)
                    if o.deadline>date:
                        cres.append(r)
                    else:
                        if not o.getShortlisted():
                            ores.append(r)
                        else:
                            sres.append(r)
                else:
                    ares.append(r)
        cres = sequence.sort(cres, (('effective', 'cmp', 'desc'), ('CreationDate', 'cmp', 'desc')))
        ores = sequence.sort(ores, (('effective', 'cmp', 'desc'), ('CreationDate', 'cmp', 'desc')))
        sres = sequence.sort(sres, (('effective', 'cmp', 'desc'), ('CreationDate', 'cmp', 'desc')))
        return dict(current=cres, 
                    ongoing=ores,
                    shortlisted=sres, 
                    archive=ares)
