import json
from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


def echo(request: WSGIRequest, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json, content_type='application/json')
    return response


@ensure_csrf_cookie
def get_token_view(request: WSGIRequest, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed{request.method}')


def json_articles(request: WSGIRequest, *args, **kwargs):
    if request.method == 'GET':
        return JsonResponse(serialize('json', Article.objects.all(), safe=False))
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        try:
            article = Article.objects.create(**article)
            response = JsonResponse(article.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {'detail': 'Некоректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


def json_article_delete(request: WSGIRequest, pk=None, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponse(status=200)

# def json_articles(request: WSGIRequest, *args, **kwargs):
#     if request.method == 'GET':
#         fields = ('pk', 'title', 'author', 'text', 'status')
#         articles = Article.objects.values(*fields)
#         return JsonResponse(list(articles), safe=False)
#     if request.method == 'POST' and request.body:
#         article = json.loads(request.body)
#         try:
#             article = Article.objects.create(**article)
#             response = JsonResponse({
#                 'id': article.pk,
#                 'title': article.title,
#                 'author': article.author,
#                 'text': article.text,
#                 'status': article.status
#             })
#             response.status_code = 201
#         except Exception:
#             response_data = {'detail': 'Некоректный набор данных'}
#             response = JsonResponse(response_data)
#             response.status_code = 400
#         return response
