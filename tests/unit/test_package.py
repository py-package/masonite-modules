from masonite.tests import TestCase


class TestMasoniteModules(TestCase):
    def test_module_route_exists(self):
        return self.get('/blogs').assertIsStatus(200)
