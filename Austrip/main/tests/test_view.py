from django.urls import reverse, resolve
from main.views import *
from django.test import TestCase, SimpleTestCase,Client
from main.models import *
from django.core.exceptions import ObjectDoesNotExist


class TestUrls(SimpleTestCase):

    def test_destination_url(self):
        url = reverse("destination_list")
        self.assertEqual(resolve(url).func, destination_list)

    def test_attraction_url(self):
        url = reverse("attraction_list")
        self.assertEqual(resolve(url).func, attraction_list)

    def test_destination_details_url(self):
        url = reverse("destination_details", args=["sydney-NSW"])
        self.assertEqual(resolve(url).func, detailed_destination)

    def test_attraction_details_url(self):
        url = reverse("attraction_details", args=["sydney-NSW"])
        self.assertEqual(resolve(url).func, detailed_attraction)

    def test_recommendations_url(self):
        url = reverse("recommendation_details", args=["sydney-NSW"])
        self.assertEqual(resolve(url).func, detailed_recommendation)

    def test_recommendations_edit_url(self):
        url = reverse("edit", args=["sydney-NSW"])
        self.assertEqual(resolve(url).func, edit)

    def test_attraction_delete_url(self):
        url = reverse("delete_comment_attraction", args=["sydney-NSW", "1"])
        self.assertEqual(resolve(url).func, delete_comment_attraction)

    def test_attraction_edit_url(self):
        url = reverse("edit_comment_attraction", args=["sydney-NSW", "1"])
        self.assertEqual(resolve(url).func, edit_comment_attraction)

    def test_destination_delete_url(self):
        url = reverse("delete_comment_destination", args=["sydney-NSW", "1"])
        self.assertEqual(resolve(url).func, delete_comment_destination)

    def test_destination_edit_url(self):
        url = reverse("edit_comment_destination", args=["sydney-NSW", "1"])
        self.assertEqual(resolve(url).func, edit_comment_destination)

    def test_search_result_url(self):
        url = reverse("search_result")
        self.assertEqual(resolve(url).func, search_result)

    def test_destination_result_url(self):
        url = reverse("destination_result")
        self.assertEqual(resolve(url).func, filter_state)

    def test_attraction_result_url(self):
        url = reverse("attraction_result")
        self.assertEqual(resolve(url).func, filter_city)

    def test_profile_url(self):
        url = reverse("profile")
        self.assertEqual(resolve(url).func, profile)

    def test_change_profile_url(self):
        url = reverse("change_profile")
        self.assertEqual(resolve(url).func, profile_change)

    def test_sign_up_url(self):
        url = reverse("signup")
        self.assertEqual(resolve(url).func, signup)

    def test_login_url(self):
        url = reverse("login_user")
        self.assertEqual(resolve(url).func, login_user)

    def test_log_out_url(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout_user)

    def test_change_password_url(self):
        url = reverse("change_password")
        self.assertEqual(resolve(url).func, change_password)

    def test_attraction_dislike_url(self):
        url = reverse("dislike", args=["id"])
        self.assertEqual(resolve(url).func, dislike_post)

    def test_attraction_like_url(self):
        url = reverse("like", args=["id"])
        self.assertEqual(resolve(url).func, like_post)

    def test_destination_dislike_url(self):
        url = reverse("d_dislike", args=["id"])
        self.assertEqual(resolve(url).func, d_dislike_post)

    def test_destination_like_url(self):
        url = reverse("d_like", args=["id"])
        self.assertEqual(resolve(url).func, d_like_post)

    def test_attraction_check_dislike_url(self):
        url = reverse("a_check_dislike", args=["id"])
        self.assertEqual(resolve(url).func, a_check_dislike)

    def test_attraction_check_like_url(self):
        url = reverse("a_check_like", args=["id"])
        self.assertEqual(resolve(url).func, a_check_like)

    def test_destination_check_dislike_url(self):
        url = reverse("d_check_dislike", args=["id"])
        self.assertEqual(resolve(url).func, d_check_dislike)

    def test_destination_check_like_url(self):
        url = reverse("d_check_like", args=["id"])
        self.assertEqual(resolve(url).func, d_check_like)

    def test_attraction_check_bookmark_url(self):
        url = reverse("a_check_bookmark", args=["id"])
        self.assertEqual(resolve(url).func, a_check_bookmark)

    def test_attraction_bookmark_url(self):
        url = reverse("a_bookmark", args=["id"])
        self.assertEqual(resolve(url).func, a_bookmark)

    def test_destination_check_bookmark_url(self):
        url = reverse("d_check_bookmark", args=["id"])
        self.assertEqual(resolve(url).func, d_check_bookmark)

    def test_destination_bookmark_url(self):
        url = reverse("d_bookmark", args=["id"])
        self.assertEqual(resolve(url).func, d_bookmark)


class SignUpViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)


class DestinationModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/destination/')
        self.assertEqual(response.status_code, 200)
        print(response.context)


class AttractionModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/attraction/')
        self.assertEqual(response.status_code, 200)


class UserModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/user/')
        self.assertEqual(response.status_code, 200)


class DestinationCommentModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/destinationComment/')
        self.assertEqual(response.status_code, 200)


class AttractionCommentModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/attractionComment/')
        self.assertEqual(response.status_code, 200)


class RecommendationModelViewSetTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/viewset/recommendation/')
        self.assertEqual(response.status_code, 200)


class GeneralViewTest(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username="tester123", password="tester123")
        self.client.post(reverse('signup'), {
            'username': 'test_user',
            'first_name': 'user_first',
            'last_name': 'user_last',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })
        # test_destination = Destination.objects.create(Destination.objects.create(destination_id=1,
        #                                                                          state="New South Wales",
        #                                                                          stateCode="NSW",
        #                                                                          name="Sydney",
        #                                                                          description="Noice place",
        #                                                                          image="abcd",
        #                                                                          likes=1,
        #                                                                          dislikes=1,
        #                                                                          click_count=1,
        #                                                                          ))
        # test_userInfo = UserInfo.objects.create(user=test_user1, bio="lol")
        # test_userInfo.destination_bookmark.add(test_destination)
        # test_userInfo.save()


    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'jae',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login_user"))
        self.assertEqual(User.objects.get(username="jae").first_name, "doe")

    def test_false_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'bad',
            'first_name': 'bad',
            'last_name': 'log',
            'password1': '1',
            'password2': '1'
        })
        user = None
        try:
            user = User.objects.get(username="bad")
        except ObjectDoesNotExist:
            self.assertEqual(user, None)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.client.post(reverse('signup'), {
            'username': 'jae',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })
        self.client.get("/logout/")
        response = self.client.post(reverse("login_user"), {
            'username': 'jae',
            'password': 'superstrong123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_false_login(self):
        self.client.post(reverse('signup'), {
            'username': 'jae',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })
        response = self.client.post(reverse("login_user"), {
            'username': 'test_user',
            'password': 'superstrong123'
        })
        self.assertEqual(response.status_code, 200)
        message = list(response.context.get('messages'))[1]
        self.assertEqual(message.message, "Invalid username or password :(")
        response = self.client.post(reverse("login_user"), {
            'username': 'jae',
            'password': 'superstrong123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_logout(self):
        self.client.post(reverse('signup'), {
            'username': 'jae',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })
        self.client.post(reverse("login_user"), {
            'username': 'jae',
            'password': 'superstrong123'
        })
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_edit_recommendation(self):
        Recommendation.objects.create(recommendation_id="Brisbane",
                                      title="Beautiful Brisbane",
                                      long_description="Brisbane, capital of Queensland, is a large city on the "
                                                       "Brisbane River. Clustered in its South Bank cultural precinct "
                                                       "are the Queensland Museum and Sciencentre, with noted "
                                                       "interactive exhibitions. Another South Bank cultural "
                                                       "institution is Queensland Gallery of Modern Art, "
                                                       "among Australia's major contemporary art museums. Looming "
                                                       "over the city is Mt. Coot-tha, site of Brisbane Botanic "
                                                       "Gardens.",
                                      short_description="Brisbane is good",
                                      image="brisbane.png")
        self.assertEqual(Recommendation.objects.get(recommendation_id="Brisbane").title, "Beautiful Brisbane")
        response = self.client.post(reverse("edit", args=["Brisbane"]), {
            'title': "Sydney",
            "long_description": "123",
            "short_description": "1",
            "image": "123.png"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recommendation.objects.get(recommendation_id="Brisbane").title, "Sydney")
        self.assertEqual(Recommendation.objects.get(recommendation_id="Brisbane").long_description, "123")
        self.assertEqual(Recommendation.objects.get(recommendation_id="Brisbane").short_description, "1")
        self.assertEqual(Recommendation.objects.get(recommendation_id="Brisbane").image, "123.png")

    def test_filter_destination_nsw(self):
        Destination.objects.create(destination_id=1,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Sydney",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1,)
        Destination.objects.create(destination_id=2,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Penrith",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1,)
        response = self.client.get(reverse("destination_result"),{'state':"NSW"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["cities"][1].name,"Sydney")
        self.assertEqual(response.context["cities"][0].name,"Penrith")
        response = self.client.get(reverse("destination_result"), {'state': "QLD"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cities"].count(),0)

    def test_filter_destination_all(self):
        Destination.objects.create(destination_id=1,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Sydney",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1, )
        Destination.objects.create(destination_id=2,
                                   state="New South Wales",
                                   stateCode="QLD",
                                   name="Melbourne",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1, )
        response = self.client.get(reverse("destination_result"), {'state': "STATE"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cities"][1].name, "Sydney")
        self.assertEqual(response.context["cities"][0].name, "Melbourne")
        response = self.client.get(reverse("destination_result"), {'state': "NSW"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cities"][0].name, "Sydney")

    def test_filter_attraction_sydney(self):
        sydney = Destination.objects.create(destination_id=1,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Sydney",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1, )
        Attraction.objects.create(attraction_id=1,
                                  city=sydney,
                                  name="Surrey Hills",
                                  description="Noice place",
                                  image="abcd",
                                  likes=1,
                                  dislikes=1,
                                  click_count=1,
                                  )
        Attraction.objects.create(attraction_id=2,
                                  city=sydney,
                                  name="Opera house",
                                  description="Noice place",
                                  image="abcd",
                                  likes=1,
                                  dislikes=1,
                                  click_count=1,
                                  )
        response = self.client.get(reverse("attraction_result"), {'city': sydney})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["places"][1].name, "Surrey Hills")
        self.assertEqual(response.context["places"][0].name, "Opera house")

    def test_filter_attraction_all(self):
        sydney = Destination.objects.create(destination_id=1,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Sydney",
                                   description="Noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1, )
        melbourne = Destination.objects.create(destination_id=2,
                                            state="Queens land",
                                            stateCode="QLD",
                                            name="Melbourne",
                                            description="Noice place",
                                            image="abcd",
                                            likes=1,
                                            dislikes=1,
                                            click_count=1, )
        Attraction.objects.create(attraction_id=1,
                                  city=sydney,
                                  name="Surrey Hills",
                                  description="Noice place",
                                  image="abcd",
                                  likes=1,
                                  dislikes=1,
                                  click_count=1,
                                  )
        Attraction.objects.create(attraction_id=2,
                                  city=melbourne,
                                  name="Flinders Street",
                                  description="Noice place",
                                  image="abcd",
                                  likes=1,
                                  dislikes=1,
                                  click_count=1,
                                  )
        response = self.client.get(reverse("attraction_result"), {'city': "CITY"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["places"][1].name, "Surrey Hills")
        self.assertEqual(response.context["places"][0].name, "Flinders Street")




