from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.request import Empty, Request
from rest_framework.decorators import (
    api_view,
)
from rest_framework import status
from rest_framework.permissions import (
    NOT,
    IsAuthenticatedOrReadOnly,
)


from author.models import Author
from author.serializers import AuthorSerializer

from .models import Post

from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@swagger_auto_schema(method="get",tags=['posts'])
@swagger_auto_schema(method="post",tags=['posts'])
@api_view(["GET","POST"])
def getAllPosts(request: Request, author_id):
    # if request.method == "GET":
    #     try:
    #         #pagination
    #         post = posts.objects.filter(author_id=author_id)
    #         s = PostsSerializer(post, context={"request": request}, many=True)
    #         return Response(s.data)
            
    #     except posts.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
      
    if request.method == "GET":
        try:

            params: dict = request.query_params

            post = Post.objects.filter(author_id=author_id)
            if (
                "page" in params and "size" in params
            ):  # make sure param has both page and size in order to paginate
                try:
                    paginator = Paginator(
                        post, int(params["size"]), allow_empty_first_page=True
                    )  # create paginator with size
                    s = PostsSerializer(
                        paginator.page(int(params["page"])), many=True
                    )  # get requested page and serialize
                except (ValueError, EmptyPage, PageNotAnInteger) as e:
                    return Response(str(e), status=status.HTTP_404_NOT_FOUND)
            else:
                s = PostsSerializer(post, context={"request": request}, many=True)
            return Response(s.data)  
        except Post.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        
        try:
            author = Author.objects.get(pk = author_id)
        except Author.DoesNotExist:
            return Response("no author under this id", status=status.HTTP_404_NOT_FOUND)

        try:
            if not request.data["title"]:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:    
                new_post = Post.objects.create(
                author_id= author,
                title=request.data["title"],
                visibility= request.data.get("visibility", "PU"),
                description= request.data.get("description", ""),
                content= request.data.get("content",""),
                contentType= request.data.get("contentType", "plain")
                )
                new_post.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
