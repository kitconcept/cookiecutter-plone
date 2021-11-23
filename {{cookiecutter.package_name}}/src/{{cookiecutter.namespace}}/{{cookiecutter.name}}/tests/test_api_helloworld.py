from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from projecttitle.projectname.testing import (
    PROJECTTITLEPROJECTNAME_CORE_FUNCTIONAL_TESTING,
)
from plone.restapi.testing import RelativeSession
from Products.CMFCore.utils import getToolByName

import unittest


class TestApiHelloWorldServiceFunctional(unittest.TestCase):

    layer = PROJECTTITLEPROJECTNAME_CORE_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        self.request = self.portal.REQUEST
        self.catalog = getToolByName(self.portal, "portal_catalog")

        self.api_session = RelativeSession(self.portal_url)
        self.api_session.headers.update({"Accept": "application/json"})
        self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)

    def tearDown(self):
        self.api_session.close()

    def test_get_system(self):
        response = self.api_session.get("/@helloworld")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Content-Type"), "application/json")
        self.assertTrue({"message": "hello world"}, response.json())
