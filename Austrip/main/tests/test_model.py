from django.test import TestCase

from main.models import *


# Destination Model Test
class DestinationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        destination = Destination.objects.create(destination_id=1,
                                                 state="New South Wales",
                                                 stateCode="NSW",
                                                 name="Sydney",
                                                 description="Noice place",
                                                 image="abcd",
                                                 likes=1,
                                                 dislikes=1,
                                                 click_count=1,
                                                 )

    def test_state_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_state_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.state, 'New South Wales')

    def test_lowercase_state_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.state, 'new south wales')

    def test_uppercase_state_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.state, 'NEW SOUTH WALES')

    def test_state_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('state').max_length
        self.assertEqual(max_length, 30)

    def test_state_code_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('stateCode').verbose_name
        self.assertEqual(field_label, 'stateCode')

    def test_state_code_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.stateCode, 'NSW')

    def test_lowercase_state_code_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.stateCode, 'nsw')

    def test_uppercase_state_code_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.stateCode, 'Nsw')

    def test_state_code_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('stateCode').max_length
        self.assertEqual(max_length, 10)

    def test_name_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(str(destination), 'Sydney')

    def test_lowercase_name_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(str(destination), 'sydney')

    def test_uppercase_name_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(str(destination), 'SYDNEY')

    def test_name_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_description_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.description, 'Noice place')

    def test_lowercase_description_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.state, 'noice place')

    def test_uppercase_description_input_label(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertNotEqual(destination.state, 'NOICE PLACE')

    def test_likes_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field("likes").verbose_name
        self.assertEqual(field_label, "likes")

    def test_likes(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.likes, 1)

    def test_dislikes_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field("dislikes").verbose_name
        self.assertEqual(field_label, "dislikes")

    def test_dislikes(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.dislikes, 1)

    def test_click_count_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field("click_count").verbose_name
        self.assertEqual(field_label, "click count")

    def test_click_count(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.click_count, 1)

    def test_user_likes_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field("userLike").verbose_name
        self.assertEqual(field_label, "userLike")

    def test_user_like_input(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.userLike.count(), 0)

    def test_more_than_one_user_like(self):
        destination = Destination.objects.get(destination_id=1)
        destination.userLike.add(User.objects.create(id=12, username="abc"))
        destination.userLike.add(User.objects.create(id=22, username="bbc"))
        self.assertEqual(destination.userLike.count(), 2)

    def test_user_dislikes_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field("userDislike").verbose_name
        self.assertEqual(field_label, "userDislike")

    def test_more_than_one_user_dislike(self):
        destination = Destination.objects.get(destination_id=1)
        destination.userDislike.add(User.objects.create(id=12, username="abc"))
        destination.userDislike.add(User.objects.create(id=22, username="bbc"))
        self.assertEqual(destination.userDislike.count(), 2)

    def test_user_dislike_input(self):
        destination = Destination.objects.get(destination_id=1)
        self.assertEqual(destination.userDislike.count(), 0)


# Attraction Model Test
class AttractionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        a = Destination.objects.create(destination_id=1,
                                       state="New South Wales",
                                       stateCode="NSW",
                                       name="Sydney",
                                       description="Noice place",
                                       image="abcd",
                                       likes=1,
                                       dislikes=1,
                                       click_count=1,
                                       )
        # Set up non-modified objects used by all test methods
        Attraction.objects.create(attraction_id=1,
                                  city=a,
                                  name="Surrey Hills",
                                  description="Noice place",
                                  image="abcd",
                                  likes=1,
                                  dislikes=1,
                                  click_count=1,
                                  )

    def test_attraction_id_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field('attraction_id').verbose_name
        self.assertEqual(field_label, 'attraction id')

    def test_attraction_id_max_length(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field('attraction_id').max_length
        self.assertEqual(field_label, 40)

    def test_city_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(str(attraction.city), 'Sydney')

    def test_attraction_name_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_attraction_name_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(str(attraction), 'Surrey Hills')

    def test_attraction_lowercase_name_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertNotEqual(str(attraction), 'surrey hills')

    def test_attraction_uppercase_name_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertNotEqual(str(attraction), 'SURREY HILLS')

    def test_attraction_name_max_length(self):
        attraction = Attraction.objects.get(attraction_id=1)
        max_length = attraction._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_attraction_description_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_attraction_description_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.description, 'Noice place')

    def test_attraction_lowercase_description_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertNotEqual(attraction.description, 'noice place')

    def test_attraction_uppercase_description_input_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertNotEqual(attraction.description, 'NOICE PLACE')

    def test_likes_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field("likes").verbose_name
        self.assertEqual(field_label, "likes")

    def test_likes(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.likes, 1)

    def test_dislikes_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field("dislikes").verbose_name
        self.assertEqual(field_label, "dislikes")

    def test_dislikes(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.dislikes, 1)

    def test_click_count_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field("click_count").verbose_name
        self.assertEqual(field_label, "click count")

    def test_click_count(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.click_count, 1)

    def test_user_likes_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field("userLike").verbose_name
        self.assertEqual(field_label, "userLike")

    def test_user_like_input(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.userLike.count(), 0)

    def test_more_than_one_user_like(self):
        attraction = Attraction.objects.get(attraction_id=1)
        attraction.userLike.add(User.objects.create(id=12, username="abc"))
        attraction.userLike.add(User.objects.create(id=22, username="bbc"))
        self.assertEqual(attraction.userLike.count(), 2)

    def test_user_dislikes_label(self):
        attraction = Attraction.objects.get(attraction_id=1)
        field_label = attraction._meta.get_field("userDislike").verbose_name
        self.assertEqual(field_label, "userDislike")

    def test_more_than_one_user_dislike(self):
        attraction = Attraction.objects.get(attraction_id=1)
        attraction.userDislike.add(User.objects.create(id=12, username="abc"))
        attraction.userDislike.add(User.objects.create(id=22, username="bbc"))
        self.assertEqual(attraction.userDislike.count(), 2)

    def test_user_dislike_input(self):
        attraction = Attraction.objects.get(attraction_id=1)
        self.assertEqual(attraction.userDislike.count(), 0)


# User Model test
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(id=1);
        test_user_info = UserInfo.objects.create(user=test_user,
                                                 bio="Testing")
        a = Destination.objects.create(destination_id=1,
                                       state="New South Wales",
                                       stateCode="NSW",
                                       name="Sydney",
                                       description="Noice place",
                                       image="abcd",
                                       likes=1,
                                       dislikes=1,
                                       click_count=1,
                                       )
        test_user_info.attraction_bookmark.add(Attraction.objects.create(attraction_id=1,
                                                                         city=a,
                                                                         name="Surrey Hills",
                                                                         description="Noice place",
                                                                         image="abcd",
                                                                         likes=1,
                                                                         dislikes=1,
                                                                         click_count=1, ))
        test_user_info.attraction_bookmark.add(Attraction.objects.create(attraction_id=2,
                                                                         city=a,
                                                                         name="Surrey Hills",
                                                                         description="Noice place",
                                                                         image="abcd",
                                                                         likes=1,
                                                                         dislikes=1,
                                                                         click_count=1, ))
        test_user_info.destination_bookmark.add(a)
        test_user_info.destination_bookmark.add(Destination.objects.create(destination_id=2,
                                                                           state="New South Wales",
                                                                           stateCode="NSW",
                                                                           name="Sydney",
                                                                           description="Noice place",
                                                                           image="abcd",
                                                                           likes=1,
                                                                           dislikes=1,
                                                                           click_count=1,
                                                                           ))

    def test_user_label(self):
        user = UserInfo.objects.get(user=1)
        field_label = user._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_bio_label(self):
        user = UserInfo.objects.get(user=1)
        field_label = user._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")

    def test_bio_input_label(self):
        user = UserInfo.objects.get(user=1)
        self.assertEqual(user.bio, "Testing")

    def test_lowercase_bio_input_label(self):
        user = UserInfo.objects.get(user=1)
        self.assertNotEqual(user.bio, "testing")

    def test_uppercase_bio_input_label(self):
        user = UserInfo.objects.get(user=1)
        self.assertNotEqual(user.bio, "TESTING")

    def test_image_label(self):
        user = UserInfo.objects.get(user=1)
        field_label = user._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_attraction_bookmark_label(self):
        user = UserInfo.objects.get(user=1)
        field_label = user._meta.get_field("attraction_bookmark").verbose_name
        self.assertEqual(field_label, "attraction bookmark")

    def test_destination_bookmark_label(self):
        user = UserInfo.objects.get(user=1)
        field_label = user._meta.get_field("destination_bookmark").verbose_name
        self.assertEqual(field_label, "destination bookmark")

    def test_default_img(self):
        user = UserInfo.objects.get(user=1)
        self.assertEqual(user.image, "image.png")

    def test_change_img(self):
        user = UserInfo.objects.get(user=1)
        user.image = "abc"
        self.assertNotEqual(user.image, "image.png")

    def test_more_than_one_attraction_bookmark(self):
        user = UserInfo.objects.get(user=1)
        self.assertEqual(user.attraction_bookmark.count(), 2)

    def test_more_than_one_destination_bookmark(self):
        user = UserInfo.objects.get(user=1)
        self.assertEqual(user.destination_bookmark.count(), 2)


class DestinationCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(id=10)
        test_destination = Destination.objects.create(destination_id=1,
                                                      state="New South Wales",
                                                      stateCode="NSW",
                                                      name="Sydney",
                                                      description="Noice place",
                                                      image="abcd",
                                                      likes=1,
                                                      dislikes=1,
                                                      click_count=1,
                                                      )
        DestinationComment.objects.create(
            commentId=1,
            user=test_user,
            comment_on=test_destination,
            comment_content="Testing Comment")

    def test_comment_id_label(self):
        comment = DestinationComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("commentId").verbose_name
        self.assertEqual(field_label, "commentId")

    def test_user_label(self):
        comment = DestinationComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_comment_on_label(self):
        comment = DestinationComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("comment_on").verbose_name
        self.assertEqual(field_label, "comment on")

    def test_comment_on_destination(self):
        comment = DestinationComment.objects.get(commentId=1)
        self.assertEqual(str(comment.comment_on), "Sydney")

    def test_comment_content_label(self):
        comment = DestinationComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("comment_content").verbose_name
        self.assertEqual(field_label, "comment content")

    def test_comment_content_input(self):
        comment = DestinationComment.objects.get(commentId=1)
        self.assertEqual(comment.comment_content, "Testing Comment")

    def test_lowercase_comment_content_input(self):
        comment = DestinationComment.objects.get(commentId=1)
        self.assertNotEqual(comment.comment_content, "testing comment")

    def test_uppercase_comment_content_input(self):
        comment = DestinationComment.objects.get(commentId=1)
        self.assertNotEqual(comment.comment_content, "TESTING COMMENT")


class AttractionCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(id=1)
        a = Destination.objects.create(destination_id=1,
                                       state="New South Wales",
                                       stateCode="NSW",
                                       name="Sydney",
                                       description="Noice place",
                                       image="abcd",
                                       likes=1,
                                       dislikes=1,
                                       click_count=1,
                                       )

        test_attraction = Attraction.objects.create(attraction_id=1,
                                                    city=a,
                                                    name="Surrey Hills",
                                                    description="Noice place",
                                                    image="abcd",
                                                    likes=1,
                                                    dislikes=1,
                                                    click_count=1,
                                                    )

        AttractionComment.objects.create(
            commentId=1,
            user=test_user,
            comment_on=test_attraction,
            comment_content="Testing Comment")

    def test_comment_id_label(self):
        comment = AttractionComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("commentId").verbose_name
        self.assertEqual(field_label, "commentId")

    def test_user_label(self):
        comment = AttractionComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_comment_on_label(self):
        comment = AttractionComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("comment_on").verbose_name
        self.assertEqual(field_label, "comment on")

    def test_comment_on_attraction(self):
        comment = AttractionComment.objects.get(commentId=1)
        self.assertEqual(str(comment.comment_on), "Surrey Hills")

    def test_comment_content_label(self):
        comment = AttractionComment.objects.get(commentId=1)
        field_label = comment._meta.get_field("comment_content").verbose_name
        self.assertEqual(field_label, "comment content")

    def test_comment_content_input(self):
        comment = AttractionComment.objects.get(commentId=1)
        self.assertEqual(comment.comment_content, "Testing Comment")

    def test_lowercase_comment_content_input(self):
        comment = AttractionComment.objects.get(commentId=1)
        self.assertNotEqual(comment.comment_content, "testing comment")

    def test_uppercase_comment_content_input(self):
        comment = AttractionComment.objects.get(commentId=1)
        self.assertNotEqual(comment.comment_content, "TESTING COMMENT")


class RecommendationCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recommendation.objects.create(recommendation_id=1,
                                      title="Good place",
                                      long_description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
                                      short_description="short lpsum lorem",
                                      image="abc.png")

    def test_recommendation_id_label(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        field_label = recommendation._meta.get_field("recommendation_id").verbose_name
        self.assertEqual(field_label, "recommendation id")

    def test_recommendation_id_max_length(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        max_length = recommendation._meta.get_field("recommendation_id").max_length
        self.assertEqual(max_length, 40)

    def test_title_label(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        field_label = recommendation._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_title_max_length(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        max_length = recommendation._meta.get_field("title").max_length
        self.assertEqual(max_length, 50)

    def test_long_description_label(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        field_label = recommendation._meta.get_field("long_description").verbose_name
        self.assertEqual(field_label, "long description")

    def test_long_description(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        self.assertEqual(recommendation.long_description,
                         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")

    def test_short_description_label(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        field_label = recommendation._meta.get_field("short_description").verbose_name
        self.assertEqual(field_label, "short description")

    def test_short_description(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        self.assertEqual(recommendation.short_description, "short lpsum lorem")

    def test_image_label(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        field_label = recommendation._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_image_inpu(self):
        recommendation = Recommendation.objects.get(recommendation_id=1)
        self.assertEqual(recommendation.image, "abc.png")
