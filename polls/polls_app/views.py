from django import http


def hello(request):
    content = '<html><body>Buna, {} from {}!</body></html>'.format(
        request.user,
        request.META['REMOTE_ADDR']
    )
    return http.HttpResponse(content, status=200)
