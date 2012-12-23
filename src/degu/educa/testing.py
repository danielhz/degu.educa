from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import degu.educa


DEGU_EDUCA = PloneWithPackageLayer(
    zcml_package=degu.educa,
    zcml_filename='testing.zcml',
    gs_profile_id='degu.educa:testing',
    name="DEGU_EDUCA")

DEGU_EDUCA_INTEGRATION = IntegrationTesting(
    bases=(DEGU_EDUCA, ),
    name="DEGU_EDUCA_INTEGRATION")

DEGU_EDUCA_FUNCTIONAL = FunctionalTesting(
    bases=(DEGU_EDUCA, ),
    name="DEGU_EDUCA_FUNCTIONAL")
