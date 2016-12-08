import unittest
from main import models

""" Simple Unittest to fields defind in the Routes Model """
class RouteTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.mock.patch.object(models.Route, 'route_name') 
    def test_route_name(self, mock_route_name):
        Route = unittest.mock.Mock(route_name="west_side_route")
        self.assertEqual(Route.route_name, "west_side_route")

    @unittest.mock.patch.object(models.Route, 'duration') 
    def test_duration(self, mock_duration):
        Route = unittest.mock.Mock(duration="01:03:00")
        self.assertEqual(Route.duration, "01:03:00")
        
    @unittest.mock.patch.object(models.Route, 'origin') 
    def test_origin(self, mock_origin):
        Route = unittest.mock.Mock(origin=[40.703104, -74.016847])
        self.assertEqual(Route.origin, [40.703104, -74.016847])

    @unittest.mock.patch.object(models.Route, 'destination') 
    def test_destination(self, mock_destination):
        Route = unittest.mock.Mock(destination=[40.850089, -73.946785])
        self.assertEqual(Route.destination, [40.850089, -73.946785])

    @unittest.mock.patch.object(models.Route, 'waypoints') 
    def test_waypoints(self, mock_waypoints):
        Route = unittest.mock.Mock(waypoints=["Boat Basin Cafe", "Bike Shop"])
        self.assertEqual(Route.waypoints, ["Boat Basin Cafe", "Bike Shop"])

    @unittest.mock.patch.object(models.Route, 'image') 
    def test_image(self, mock_image):
        Route = unittest.mock.Mock(image="west_side.jpg")
        self.assertEqual(Route.image, "west_side.jpg")

    @unittest.mock.patch.object(models.Route, 'template') 
    def test_template(self, mock_template):
        Route = unittest.mock.Mock(template='west_side_route.html')
        self.assertEqual(Route.template, "west_side_route.html")
