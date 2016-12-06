from django.test import TestCase
from main.models import Route

""" Route Model Tests """
class RouteTestCase(TestCase):
    def setUp(self):
      name = "west_side_route"  
      dur = '01:03:00'
      pointA = [40.703104, -74.016847]
      pointB = [40.850089, -73.946785]
      nearby = ["Boat Basin Cafe", "Bike Shop"]
      self.west_side_route=Route.objects.create(route_name=name, duration=dur, 
              origin=pointA, destination=pointB, waypoints=nearby)

    def tearDown(self):
        pass

    def test_route_created(self):
        """
        Asserts west side route has been created
        """
        self.assertIsNotNone(self.west_side_route)

    def test_duration(self):
        """
        Assert duration of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.duration, '01:03:00')

    def test_origin(self):
        """
        Assert origin of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.origin,[40.703104, -74.016847]) 

    def test_destination(self):
        """
        Assert destination of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.destination, [40.850089, -73.946785])
    
    def test_waypoints(self): 
        """
        Assert waypoints of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.waypoints,["Boat Basin Cafe", "Bike Shop"])
    
