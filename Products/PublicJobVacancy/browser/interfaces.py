from zope.interface import Interface


class IJobsListing(Interface):

    def results(obj):
        """Returns a dictionary containing 4 lists: current Jobs, ongoing Jobs,
        short-listed Jobs, past Jobs.
        """

    def getAdditionalText():
        """Return the text value of a document called content lying in the same
        folder.
        """
