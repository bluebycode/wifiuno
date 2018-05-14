from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse

from app.models import Log

@require_http_methods(["GET"])
def all(req):
    rows = Log.objects.order_by('-id') # retrieve from database
    return render(req, 'app/all.html', {'rows': rows}) # return the attributes needed for the view

@require_http_methods(["GET"])
def add(req):
    id = req.GET.get('id', None)
    comments = req.GET.get('comments', None)
    log = Log(id=id, comments=comments)
    log.save()
    return HttpResponse(status=201)


