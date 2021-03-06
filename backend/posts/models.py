from django.db import models
import uuid
from author.models import Author
from django.utils import timezone


# Create your models here.

visibility_choice = (("PUBLIC","PUBLIC"), ("PRIVATE","PRIVATE"))
content_choice = (("text/markdown","text/markdown"),("text/plain","text/plain"),("application/base64","application/base64"),("image/png;base64","image/png;base64"),("image/jpeg;base64","image/jpeg;base64"))


class postsManager(models.Model):
    pass

class Post(models.Model):
    
    post_id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=100)
    author_id = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="post_author"
    )
    title = models.CharField(
        "title", max_length=100, unique=False, null=False, blank=False, default= ""
    )
    visibility = models.CharField(
        choices=visibility_choice, max_length=8, null=False, blank=False, default="PUBLIC"
    )
    description = models.CharField("description", max_length=100, blank=True)
    content = models.TextField("content", blank=True)
    contentType = models.CharField(
        choices=content_choice, max_length= 20, null=False, default="text/plain"
    )
    source = models.URLField(editable = False)
    origin = models.URLField(editable = False)
    unlisted = models.BooleanField(default = False)
    # https://www.geeksforgeeks.org/datetimefield-django-models/
    published = models.DateTimeField(default = timezone.now, editable= False)
    count = models.IntegerField(default=0)
    categories = models.CharField(max_length=200)

    def __str__(self):
        return f"post:{self.post_id}"
