from django.test import TestCase
from main.models import User, Route

""" User Model Tests """
class UserTestCase(TestCase):
    def setUp(self):
        self.mBanks=User.objects.create(first_name ="Melissa", last_name="Banks", email="mbanks@email.com",
                password="mbanks123")
        self.tBarnett=User.objects.create(first_name="Tom", last_name="Barnett", email="tbarnett@email.com",
                password="tbarnett123")
        self.mLee=User.objects.create(first_name="Mark", last_name="Lee", email="mlee@email.com",
                password="mlee123")

    def tearDown(self):
        pass

    def test_user_created(self):
        """
        Asserts that User Melissa Banks was created
        """
        self.assertIsNotNone(self.mBanks)

    def test_username_exists(self):
        """
        Asserts that user Tom Barnett exists in the database
        """
        tBarnett = User.objects.get(email="tbarnett@email.com")
        self.assertEqual(self.tBarnett, tBarnett) 
        
    def test_password_length(self):

        """
        Asserts that password length is less than the limit '256'
        """
        self.assertLess(len(self.mBanks.password), 256)
        self.assertLess(len(self.tBarnett.password), 256)
        self.assertLess(len(self.mLee.password), 256)

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
    
