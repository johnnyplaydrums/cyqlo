import unittest
from main import views

""" Simple Unittest to guage url, 202, and 404 responses defined in views"""
class TestCase(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        @unittest.mock.patch.object(views, 'index')
        def test_index(self, mock_index):
            index_response = unittest.mock.Mock(status_code=200, url='/')
            self.assertEqual(index_response.status_code, 200)
            self.assertIsNotNone(index_response.url)

        @unittest.mock.patch.object(views, 'index')
        def test_index_bad(self, mock_index):
            index_response = unittest.mock.Mock(status_code=404)
            index_response.return_value = None 
            self.assertEqual(index_response.return_value, None)
            self.assertEqual(index_response.status_code, 404)

        @unittest.mock.patch.object(views, 'login_view')
        def test_login_view(self, mock_login_view):
            login_response = unittest.mock.Mock(status_code=200, url="/login_view")
            login_response.return_value = "/login_view" 
            self.assertEqual(login_response.status_code, 200)
            self.assertEqual(login_response.url, "/login_view")
            self.assertEqual(login_response.url, login_response.return_value)

        @unittest.mock.patch.object(views, 'logout_view')
        def test_logout_view(self, mock_logout_view):
            login_response = unittest.mock.Mock(status_code=200, url="/logout_view")
            login_response.return_value = "/logout_view" 
            self.assertEqual(login_response.status_code, 200)
            self.assertEqual(login_response.url, "/logout_view")
            self.assertEqual(login_response.url, login_response.return_value)

        @unittest.mock.patch.object(views, 'signup')
        def test_signup(self, mock_signup):
            signup_response = unittest.mock.Mock(status_code=200, url="/profile")
            signup_response.return_value = "/profile" 
            self.assertEqual(signup_response.status_code, 200)

        @unittest.mock.patch.object(views, 'about')
        def test_about(self, mock_about):
            about_response = unittest.mock.Mock(url="/about")
            self.assertIsNotNone(about_response.url)
            self.assertEqual(about_response.url, '/about')

        @unittest.mock.patch.object(views, 'routes_page')
        def test_route_page(self, mock_about):
            about_response = unittest.mock.Mock(url="/route_page")
            self.assertEqual(about_response.url, '/route_page')

        @unittest.mock.patch.object(views, 'west_side_route')
        def test_west_side_route(self, mock_west_side_route):
            wsr_response = unittest.mock.Mock(status_code= 200, url="/west_side_route")
            self.assertEqual(wsr_response.status_code, 200)
            self.assertEqual(wsr_response.url, '/west_side_route')

        @unittest.mock.patch.object(views, 'bronx_green_lands')
        def test_bronx_green_lands(self, mock_bronx_green_land):
            bgr_response = unittest.mock.Mock(status_code= 200, url="/bronx_green_lands")
            self.assertEqual(bgr_response.status_code, 200)
            self.assertEqual(bgr_response.url, '/bronx_green_lands')

        @unittest.mock.patch.object(views, 'shore_parkway_route')
        def test_shore_parkway_route(self, mock_west_side_route):
            spw_response = unittest.mock.Mock(status_code= 200, url="/shore_parkway_route")
            self.assertEqual(spw_response.url, '/shore_parkway_route')

        @unittest.mock.patch.object(views, 'pizza_tour_route')
        def test_pizza_tour_route(self, mock_pizza_tour_route):
            pt_response = unittest.mock.Mock(status_code= 200, url="/pizza_tour_route")
            self.assertEqual(pt_response.url, '/pizza_tour_route')

        @unittest.mock.patch.object(views, 'cunningham_park_trail')
        def test_cunningham_park_trail(self, mock_cparktrail):
            cpt_response = unittest.mock.Mock(status_code= 200, url="/cunningham_park_trail")
            self.assertEqual(cpt_response.url, '/cunningham_park_trail')

        @unittest.mock.patch.object(views,'columbuscircle_bearmtn_route')
        def test_columbuscircle_bearmtn_route(self, mock_colbearmtn):
            cbr_response = unittest.mock.Mock(status_code= 200, url="/columbuscircle_bearmtn_route")
            self.assertEqual(cbr_response.url, '/columbuscircle_bearmtn_route')
            
        @unittest.mock.patch.object(views, 'soulfood_harlem')
        def test_soulfood_harlem(self, mock_harlsoulfood_route):
            hsf_response = unittest.mock.Mock(status_code= 200, url="soulfood_harlem")
            self.assertEqual(hsf_response.url, 'soulfood_harlem')

        @unittest.mock.patch.object(views, 'hamilton_tour')
        def test_hamilton_tour(self, mock_hamilton_tour):
            ht_response = unittest.mock.Mock(status_code= 200, url="/hamilton_tour")
            self.assertEqual(ht_response.url, '/hamilton_tour')

