from PIL import Image
from django.db import models
from django.contrib.auth.models import User



class Destination(models.Model):
    destination_id = models.CharField(max_length=40, primary_key=True)
    state = models.CharField(max_length=30)
    stateCode = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    click_count = models.IntegerField()
    userLike = models.ManyToManyField(User, related_name="Dlike", default=None, blank=True)
    userDislike = models.ManyToManyField(User, related_name="DDislike", default=None, blank=True)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    attraction_id = models.CharField(max_length=40, primary_key=True)
    city = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    click_count = models.IntegerField()
    userLike = models.ManyToManyField(User, related_name="ALike", default=None, blank=True)
    userDislike = models.ManyToManyField(User, related_name="ADislike", default=None, blank=True)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField()
    attraction_bookmark = models.ManyToManyField(Attraction, related_name="Abook", default=None, blank=True)
    destination_bookmark = models.ManyToManyField(Destination, related_name="Dbook", default=None, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class DestinationComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class AttractionComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Recommendation(models.Model):
    recommendation_id = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=50)
    long_description = models.TextField()
    short_description = models.TextField()
    image = models.ImageField()