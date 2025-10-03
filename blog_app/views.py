from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from blog_app.models import artikle,category,Comment
from contactus_app.models import footer

def post_detail(request,slug):
    arti = get_object_or_404(artikle,slug=slug)
    footer1 = footer.objects.last()
    arti.views+=1
    arti.save()
    if request.method=='POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body,myarticle = arti , user = request.user , parent_id=parent_id)
    return render(request,'blog_app/artikle_details.html',{'art':arti , 'footers':footer1})
def allarticle_list(request):
    article = artikle.objects.all()
    footer1 = footer.objects.last()
    page_number = request.GET.get('page')
    paginatori = Paginator(article,2)
    object_list = paginatori.get_page(page_number)
    return render(request,'blog_app/all_artikle_list.html',{'articli':object_list , 'footers' : footer1})
def category_detail(request,pk=None):
    categor=get_object_or_404(category,id=pk)
    arti=categor.artikle_set.all()
    return render(request,'blog_app/all_artikle_list.html',{'articli':arti})

# Create your views here.
