'''
    MARKS app
'''
from django.shortcuts import render_to_response
from webmarks.models import Marks, Tags

# Create your views here.
def markindex(request):
    hotTagList = Tags.objects.order_by('-marksNum')[:2]
    lastMarkList = Marks.objects.order_by('-id')[:2]
    return render_to_response('index.html',{'lastMarkList':lastMarkList,'hotTagList':hotTagList})