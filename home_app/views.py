from django.shortcuts import render
from blog_app.models import artikle, category
from contactus_app.models import footer
def home(request):
    art = artikle.objects.all()
    footer1 = footer.objects.last()
    recent_articles = artikle.objects.all()[:3]
    return render(request,'home_app/index.html',{'myartikle':art,'footers':footer1,'recent_art':recent_articles})
def sidebar(request):
    # provide recent articles and categories to the sidebar partial
    cati = category.objects.all()
    recent_art = artikle.objects.all()[:3]
    context = {'cati': cati, 'recent_art': recent_art}
    return render(request,'includes/sidebar.html',context=context)
# Create your views here.
