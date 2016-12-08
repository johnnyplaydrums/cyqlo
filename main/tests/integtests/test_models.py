from django.test import TestCase
from main.models import Route

""" We omit User Model Tests because we are using Django's built-in User Model"""

""" Route Model Tests """
class RouteTestCase(TestCase):
    def setUp(self):
      name = "west_side_route"  
      dur = '01:03:00'
      pointA = [40.703104, -74.016847]
      pointB = [40.850089, -73.946785]
      nearby = ["Boat Basin Cafe", "Bike Shop"]
      img = "west_side.jpg"
      temp = "west_side_route.html" 
      self.west_side_route=Route.objects.create(route_name=name, duration=dur, 
              origin=pointA, destination=pointB, waypoints=nearby, image=img, template=temp)
        
      name = "harlem_soulfood_tour"  
      dur = '00:30:00'
      curr = [40.8200471,-73.9492724]
      dest = [40.8200471,-73.9492724]
      interests = ["Amy Ruth's", "B2 Harlem", "Sweet Mama's"]
      img = "soulfood.jpeg"
      temp = "harlem_soulfood_tour.html" 
      self.harlem_soulfood_tour=Route.objects.create(route_name=name, duration=dur, 
              origin=curr, destination=dest, waypoints=interests, image=img, template=temp)
        

    def tearDown(self):
        pass

#TestCase for West Side Route
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

    def test_image(self):
        """
        Assert image of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.image, "west_side.jpg")

    def test_template(self):
        """
        Assert template name of the west side route is the same as initially created
        """
        self.assertEqual(self.west_side_route.template, "west_side_route.html")

#TestCase for Harlem Soul Food Tour 
    def test_route_created(self):
        """
        Asserts harlem soulfood tour has been created
        """
        self.assertIsNotNone(self.harlem_soulfood_tour)

    def test_duration(self):
        """
        Assert duration of the harlem soulfood tour exists
        """
        self.assertIsNotNone(self.harlem_soulfood_tour.duration)

    def test_current(self):
        """
        Assert current locations of the harlem soulfood tour is the same as initially created
        """
        self.assertEqual(self.harlem_soulfood_tour.origin,[40.8200471,-73.9492724]) 

    def test_destination(self):
        """
        Assert current locations of the harlem soulfood tour is the same as initially created
        """
        self.assertEqual(self.harlem_soulfood_tour.destination,[40.8200471,-73.9492724]) 

    def test_waypoints(self): 
        """
        Assert waypoints of the harlem soulfood tour is the same as initially created
        """
        self.assertEqual(self.harlem_soulfood_tour.waypoints,["Amy Ruth's", "B2 Harlem", "Sweet Mama's"])

    def test_image(self):
        """
        Assert image of the harlem soulfood tour is the same as initially created
        """
        self.assertEqual(self.harlem_soulfood_tour.image, "soulfood.jpeg")

    def test_template(self):
        """
        Assert template name of the harlem soulfood tour is the same as initially created
        """
        self.assertEqual(self.harlem_soulfood_tour.template, "harlem_soulfood_tour.html")
    
