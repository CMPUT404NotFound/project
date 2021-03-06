from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import views
from author.models import *
from Followers.models import *
from posts.models import *
from comment.models import *
from logging import exception
from django.http import response
from django.http import request
from django.http.request import HttpRequest

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class PostTestCase(TestCase):
    def setUp(self):
        response = self.client.get("")
        self.request = response.wsgi_request
        self.usr1 = self.create_author("test_user1", "test_user1",
                                       "test_user1@github", "", "test_password1")
        self.usr2 = self.create_author("test_user2", "test_user2",
                                       "test_user2@github", "", "test_password2")
        self.usr3 = self.create_author("test_user3", "test_user3",
                                       "test_user3@github", "", "test_password3")
        self.post = self.create_post(self.usr1, "test_title", "test_content")
        self.comment = self.create_comment(self.usr2, self.post, "test_content")

    def create_author(self, username, display_name, github, profile_image, password):
        author = Author.objects.create_superuser(userName=username, displayName=display_name, github=github,
                                                 profileImage=profile_image, password=password)
        author.save()
        return author

    def get_author_inbox(self):
        str_id1 = str(self.usr1.id)
        response = self.client.get(f"/api/author/{str_id1}/inbox")
        assert 100 < response.status_code < 300

    def get_recent_post(self):
        str_id1 = str(self.usr1.id)
        post_id = str(self.post.id)
        response = self.client.get(f"/api/author/{str_id1}/posts/{post_id}")
        assert 100 < response.status_code < 300

    def delete_post(self):
        str_id1 = str(self.usr1.id)
        post_id = str(self.post.id)
        response = self.client.delete(f"/api/author/{str_id1}/posts/{post_id}")
        assert 100 < response.status_code < 300

    def create_post(self):
        str_id1 = str(self.usr1.id)
        data = {
                    "type":"post",
                    # title of a post
                    "title":"A post title about a post about web dev",
                    # id of the post
                    "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
                    # where did you get this post from?
                    "source":"http://lastplaceigotthisfrom.com/posts/yyyyy",
                    # where is it actually from
                    "origin":"http://whereitcamefrom.com/posts/zzzzz",
                    # a brief description of the post
                    "description":"This post discusses stuff -- brief",
                    "contentType":"text/plain",
                    "content":"???? w??s on burgum B??owulf Scyldinga, l??of l??od-cyning, longe ??r??ge folcum gefr??ge (f??der ellor hwearf, aldor of earde), o?? ????t him eft onw??c h??ah Healfdene; h??old ??enden lifde, gamol and g????-r??ow, gl??de Scyldingas. ????m f??ower bearn for??-ger??med in worold w??cun, weoroda r??swan, Heorog??r and Hr????g??r and H??lga til; hy??rde ic, ??at Elan cw??n Ongen????owes w??s Hea??oscilfinges heals-gebedde. ???? w??s Hr????g??re here-sp??d gyfen, w??ges weor??-mynd, ????t him his wine-m??gas georne hy??rdon, o?? ????t s??o geogo?? gew??ox, mago-driht micel. Him on m??d bearn, ????t heal-reced h??tan wolde, medo-??rn micel men gewyrcean, ??one yldo bearn ??fre gefr??non, and ????r on innan eall ged??lan geongum and ealdum, swylc him god sealde, b??ton folc-scare and feorum gumena. ???? ic w??de gefr??gn weorc gebannan manigre m??g??e geond ??isne middan-geard, folc-stede fr??twan. Him on fyrste gelomp ??dre mid yldum, ????t hit wear?? eal gearo, heal-??rna m??st; sc??p him Heort naman, s?? ??e his wordes geweald w??de h??fde. H?? b??ot ne ??l??h, b??agas d??lde, sinc ??t symle. Sele hl??fade h??ah and horn-g??ap: hea??o-wylma b??d, l????an l??ges; ne w??s hit lenge ???? g??n ????t se ecg-hete ????um-swerian 85 ??fter w??l-n????e w??cnan scolde. ???? se ellen-g??st earfo??l??ce ??r??ge ge??olode, s?? ??e in ??y??strum b??d, ????t h?? d??gora gehw??m dr??am gehy??rde hl??dne in healle; ????r w??s hearpan sw??g, swutol sang scopes. S??gde s?? ??e c????e frum-sceaft f??ra feorran reccan",
                    # the author has an ID where by authors can be disambiguated
                    "author":{
                        "type":"author",
                        # ID of the Author
                        "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                        # the home host of the author
                        "host":"http://127.0.0.1:5454/",
                        # the display name of the author
                        "displayName":"Lara Croft",
                        # url to the authors profile
                        "url":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                        # HATEOS url for Github API
                        "github": "http://github.com/laracroft",
                        # Image from a public domain (optional, can be missing)
                        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
                    },
                    # categories this post fits into (a list of strings
                    "categories":["web","tutorial"],
                    # comments about the post
                    # return a maximum number of comments
                    # total number of comments for this post
                    "count": 1023,
                    # the first page of comments
                    "comments":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
                    "commentsSrc":{
                        "type":"comments",
                        "page":1,
                        "size":5,
                        "post":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
                        "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
                        "comments":[
                            {
                                "type":"comment",
                                "author":{
                                    "type":"author",
                                    # ID of the Author (UUID)
                                    "id":"http://127.0.0.1:5454/author/1d698d25ff008f7538453c120f581471",
                                    # url to the authors information
                                    "url":"http://127.0.0.1:5454/author/1d698d25ff008f7538453c120f581471",
                                    "host":"http://127.0.0.1:5454/",
                                    "displayName":"Greg Johnson",
                                    # HATEOS url for Github API
                                    "github": "http://github.com/gjohnson",
                                    # Image from a public domain
                                    "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
                                },
                                "comment":"Sick Olde English",
                                "contentType":"text/markdown",
                                # ISO 8601 TIMESTAMP
                                "published":"2015-03-09T13:07:04+00:00",
                                # ID of the Comment (UUID)
                                "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments/f6255bb01c648fe967714d52a89e8e9c",
                            }
                        ]
                    }
                    # ISO 8601 TIMESTAMP
                    "published":"2015-03-09T13:07:04+00:00",
                    # visibility ["PUBLIC","FRIENDS"]
                    "visibility":"PUBLIC",
                    "unlisted":false
                    # unlisted means it is public if you know the post name -- use this for images, it's so images don't show up in timelines
                }
        response = self.client.put(f"/api/author/{str_id1}/posts/")
        assert 100 < response.status_code < 300

    def get_all_post(self):
        str_id1 = str(self.usr1.id)
        response = self.client.get(f"/api/author/{str_id1}/posts/")
        assert 100 < response.status_code < 300
                            
