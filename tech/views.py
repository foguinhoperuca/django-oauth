from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'tech/index.html')


@login_required
def members(request):
    return render(request, 'tech/members.html')
