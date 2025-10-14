from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from blog_app.models import artikle,category,Comment
from contactus_app.models import footer
from .forms import ContactUsForm
from django.shortcuts import redirect
from django.contrib import messages
from .models import ContactMessage  # مطمئن شوید این مدل را ایمپورت کرده‌اید


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
    paginatori = Paginator(article,1)
    object_list = paginatori.get_page(page_number)
    return render(request,'blog_app/all_artikle_list.html',{'articli':object_list , 'footers' : footer1})
def category_detail(request,pk=None):
    categor=get_object_or_404(category,id=pk)
    arti=categor.artikle_set.all()
    return render(request,'blog_app/all_artikle_list.html',{'articli':arti})
def search(request):
    q = request.GET.get('q')
    articl = artikle.objects.filter(slug__icontains = q)
    page_number = request.GET.get('page')
    pagin = Paginator(articl,1)
    object_list=pagin.get_page(page_number)
    return render(request,'blog_app/all_artikle_list.html',{'articli':object_list})
# Create your views here.









def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره مستقیم در مدل

            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
            return redirect('blog:contact_us')
    else:
        form = ContactUsForm()

    return render(request, 'blog_app/contact_us.html', {'myform': form})




