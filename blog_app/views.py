from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from blog_app.models import artikle,category,Comment
from contactus_app.models import footer
from .forms import ContactUsForm 
from .models import Message

def post_detail(request, slug):
    # دریافت تمام مقالات با slug مورد نظر
    articles = artikle.objects.filter(slug=slug)

    # اگر هیچ مقاله‌ای نبود، خطا بده
    if not articles.exists():
        raise Http404("مقاله پیدا نشد")

    # گرفتن اولین مقاله از queryset
    arti = articles.first()

    # افزایش تعداد بازدید
    arti.views += 1
    arti.save()

    # Footer
    footer1 = footer.objects.last()

    # ثبت کامنت در صورت ارسال POST
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, myarticle=arti, user=request.user, parent_id=parent_id)

    return render(request, 'blog_app/artikle_details.html', {'art': arti, 'footers': footer1})

# def post_detail(request,slug):
#     arti = get_object_or_404(artikle,slug=slug)
#     footer1 = footer.objects.last()
#     arti.views+=1
#     arti.save()
#     if request.method=='POST':
#         body = request.POST.get('body')
#         parent_id = request.POST.get('parent_id')
#         Comment.objects.create(body=body,myarticle = arti , user = request.user , parent_id=parent_id)
#     return render(request,'blog_app/artikle_details.html',{'art':arti , 'footers':footer1})
def allarticle_list(request):
    article = artikle.objects.all()
    footer1 = footer.objects.last()
    page_number = request.GET.get('page')
    paginatori = Paginator(article,2)
    object_list = paginatori.get_page(page_number)
    return render(request,'blog_app/all_artikle_list.html',{'page_obj': object_list , 'footers' : footer1})
def category_detail(request,pk=None):
    categor=get_object_or_404(category,id=pk)
    arti=categor.artikle_set.all()
    return render(request,'blog_app/all_artikle_list.html',{'articli':arti})

# def search (request):
#     q=request.GET.get('q')
#     articl=artikle.objects.filter(slug__icontains=q)
#     page_number=request.GET.get('page')
#     pagin=Paginator(articl,1)
#     object_list=pagin.get_page(page_number)
#     return render(request, 'blog_app/all_artikle_list.html', {'articli': object_list})

# Create your views here.

from django.db.models import Q

def search(request):
    # دریافت query از URL و حذف فاصله‌های اضافی
    query = request.GET.get('q', '').strip()  
    # ⚡ تغییر: افزودن '' پیش‌فرض برای جلوگیری از None و خطای ValueError

    if query:
        # جستجوی همزمان در title, body و slug با icontains
        results = artikle.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(slug__icontains=query)
        )
        # ⚡ تغییر: افزودن Q برای چند فیلد و انعطاف بیشتر
    else:
        # اگر query خالی باشد، QuerySet خالی برگردان
        results = artikle.objects.none()  
        # ⚡ تغییر: جلوگیری از خطای None و نمایش صفحات خالی

    # صفحه‌بندی نتایج با 1 مقاله در هر صفحه
    paginator = Paginator(results, 1)  
    # ⚡ تغییر: نام متغیر تغییر کرده به results و تعداد هر صفحه 1 برای تست

    # دریافت شماره صفحه از URL، پیش‌فرض 1
    page_number = request.GET.get('page', 1)  
    # ⚡ تغییر: افزودن مقدار پیش‌فرض 1 برای جلوگیری از None هنگام صفحه‌بندی

    # گرفتن صفحه فعلی از paginator
    page_obj = paginator.get_page(page_number)  
    # ⚡ تغییر: استفاده از get_page برای مدیریت شماره صفحه نامعتبر

    # ارسال page_obj و query به قالب
    return render(request, 'blog_app/all_artikle_list.html', {
        'page_obj': page_obj,  
        # ⚡ تغییر: نام متغیر هماهنگ با template و شامل Page object
        'query': query,        
        # ⚡ تغییر: ارسال query برای نگهداری جستجو در لینک‌های pagination
    })
def contactus(request): 
    form = ContactUsForm(data=request.POST or None)
    message = None
    if request.method == 'POST':
        if not request.user.is_authenticated:
            message = "برای ارسال پیام باید ابتدا وارد شوید یا ثبت‌نام کنید."
        elif form.is_valid():
            Message.objects.create(
                title=form.cleaned_data.get('name'),
                text=form.cleaned_data.get('text'),
            )
            message = "پیام شما با موفقیت ثبت شد."
            form = ContactUsForm()  # خالی کردن فرم بعد ثبت موفق
    return render(request, 'blog_app/contact_us.html', {'myform': form, 'message': message})