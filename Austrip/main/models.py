from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=30)
    bio = models.TextField()
    image = models.ImageField()
    admin = models.BooleanField(default=False)


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
    userLike = models.ManyToManyField(User,related_name="Dlike",default = None,blank=True);
    bookmark = models.ManyToManyField(User,related_name="DBookmark",default = None,blank=True);
    def __str__(self):
        return self.name


class Attraction(models.Model):
    attraction_id = models.CharField(max_length=40, primary_key=True)
    state = models.CharField(max_length=30)
    stateCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    click_count = models.IntegerField()
    userLike = models.ManyToManyField(User, related_name="ALike", default=None, blank=True);
    bookmark = models.ManyToManyField(User, related_name="ABookmark", default=None, blank=True);

    def __str__(self):
        return self.name


class DestinationComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    comment_on = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class AttractionComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    comment_on = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Recommendation(models.Model):
    recommendation_id = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=50)
    long_description = models.TextField()
    short_description = models.TextField()
    image = models.ImageField()
