from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2


class PublicJobVacancy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import osha.policy.browser
        self.loadZCML('configure.zcml', package=osha.policy.browser)
        import Products.SimpleAttachment
        self.loadZCML('configure.zcml', package=Products.SimpleAttachment)
        import Products.RichDocument
        self.loadZCML('configure.zcml', package=Products.RichDocument)
        import Products.PublicJobVacancy
        self.loadZCML('configure.zcml', package=Products.PublicJobVacancy)

        z2.installProduct(app, 'Products.SimpleAttachment')
        z2.installProduct(app, 'Products.RichDocument')
        z2.installProduct(app, 'Products.PublicJobVacancy')

    def setUpPloneSite(self, portal):
        # Needed to make skins work
        applyProfile(portal, 'Products.CMFPlone:plone')

        applyProfile(portal, 'Products.SimpleAttachment:default')
        applyProfile(portal, 'Products.RichDocument:default')
        applyProfile(portal, 'Products.PublicJobVacancy:default')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'Products.SimpleAttachment')
        z2.uninstallProduct(app, 'Products.RichDocument')
        z2.uninstallProduct(app, 'Products.PublicJobVacancy')


PUBLICJOBVACANCY_FIXTURE = PublicJobVacancy()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(PUBLICJOBVACANCY_FIXTURE,),
    name="PublicJobVacancy:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PUBLICJOBVACANCY_FIXTURE,),
    name="PublicJobVacancy:Functional")
