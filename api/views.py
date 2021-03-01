import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .forms import PostmanAPIForm
from .functions import get_access_token

sep = os.path.sep

TITLE1 = ('pe-7s-network', 'Postman App', '')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@login_required
def api(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(request.path_info)
    form = PostmanAPIForm(request.POST or None, request.FILES or None)
    return render(request, 'api/index.html', {'title': TITLE1, 'form': form, 'user': request.user})


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TITLE2 = ('pe-7s-rocket', '트래픽 분석 애플리케이션', '파일 내역을 비교하는 애플리케이션')


@login_required
def traffic(request):
    google_access_token = get_access_token()
    google_userid = os.getenv('GOOGLE_USER_ID', None)
    return render(request, 'api/traffic.html', {'google_access_token': google_access_token, 'google_userid': google_userid, 'title': TITLE2, 'user': request.user})
