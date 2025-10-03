from blog_app.models import artikle,category
def recent_artikles(request):
    recent_art = artikle.objects.order_by('-views')[:3]
    return {'recent_art':recent_art}
def categori_artikles(request):
    categori = category.objects.all()
    return {'cati':categori}