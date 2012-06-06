from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from Products.PublicJobVacancy.tests.base import INTEGRATION_TESTING

import unittest2 as unittest


class TestPublicJobVacancy(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        # Login as manager
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def test_create(self):
        """Ensure that we can create a PublicJobVacancy without errors"""

        self.portal.invokeFactory(
            'PublicJobVacancy', 'job-vacancy', title=u"Public Job vacancy")


def test_suite():
    """This sets up a test suite that actually runs the tests in
    the class(es) above.
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
