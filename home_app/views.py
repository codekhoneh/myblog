from django.shortcuts import render
from blog_app.models import artikle
from contactus_app.models import footer
def home(request):
    art = artikle.objects.all()
    footer1 = footer.objects.last()
    recent_articles = artikle.objects.all()[:3]
    return render(request,'home_app/index.html',{'myartikle':art,'footers':footer1,'recent_art':recent_articles})
def sidebar(request):
    data = {'name':'amir'}
    return render(request,'includes/sidebar.html',context=data)
# Create your views here.
