import json
import logging
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from blog.api.serializers import PostSerializer
from rest_framework.parsers import JSONParser
from blog.models import Post


logger = logging.getLogger(__name__)

@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return JsonResponse({"data": PostSerializer(posts, many = True).data})
    elif request.method == "POST":
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    logger.debug("post_detail pk(%d) / request(%s) / data(%s)", pk, str(request), str(request.body), )

    if request.method == "GET":
        return JsonResponse(PostSerializer(post).data)
    elif request.method == "PUT":
        post_data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=post_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

