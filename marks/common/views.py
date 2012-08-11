# Create your views here.
from common.models import Userinfo
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response

#login
def login(request):
    username = request.GET['username']
    password = request.GET['password']
    if(username != '' and password != ''):
        qset = (
                Q(username=username)&Q(password=password)
                )
        userinfo = Userinfo.objects.filter(qset).distinct()
        if userinfo:
            request.session['cuserinfo'] = userinfo
            request.session['haha'] = "haha"
            return render_to_response('index.html', {'session':request.session})
        else:
            return render_to_response('index.html')
    else:
        return render_to_response('index.html')  
    
