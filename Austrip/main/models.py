from django.db import models


class Destination(models.Model):
    destination_id = models.CharField(max_length=20, primary_key=True)
    state = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField()
    imageUrls = models.URLField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.name


class Attraction(models.Model):
    attraction_id = models.CharField(max_length=20, primary_key=True)
    city = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    imageUrls = models.URLField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.name


class DestinationComment(models.Model):
    # commentId =
    comment_on = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class AttractionComment(models.Model):
    # commentId =
    comment_on = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Recommendation(models.Model):
    title = models.CharField(max_length=50)
    long_description = models.TextField()
    short_description = models.TextField()
    imageUrls = models.URLField()
