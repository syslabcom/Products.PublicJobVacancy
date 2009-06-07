from zope.interface import Interface, Attribute

class IJobsListing(Interface):

    def results(obj):
        """ returns a dictionary containing 4 lists: current Jobs, ongoing Jobs,
        short-listed Jobs, past Jobs
        """

    def getAdditionalText():
        """ return the text value of a document called content lying in the same folder """