from django.contrib import admin
from .models import Destination, Attraction, DestinationComment, AttractionComment, Recommendation

admin.site.register(Destination)
admin.site.register(Attraction)
admin.site.register(DestinationComment)
admin.site.register(AttractionComment)
admin.site.register(Recommendation)