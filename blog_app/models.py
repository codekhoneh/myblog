from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
class category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
 
class artikle(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='images/artikels')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    catg = models.ManyToManyField(category)
    slug = models.SlugField(null=True,unique=False,blank=True)
    views = models.PositiveIntegerField(default=0)
    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        self.slug = slugify(self.title)
        super(artikle,self).save()
    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs={'slug':self.slug})
    def __str__(self):
        return f'{self.title}-{self.body[:30]}'
    class Meta:
        ordering = ('-views',)
    class Meta:
        ordering = ('-created',)
class Comment(models.Model):
    myarticle = models.ForeignKey(artikle,on_delete=models.CASCADE,related_name='commentss')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[:50]
<<<<<<< HEAD
    


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=300, blank=False)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    birth_year=models.CharField(max_length=4,verbose_name='year of birth',default='1400',blank=True,null=True)
    intro_method=models.CharField(max_length=10,verbose_name='How to get to know the site',default='search')

    def __str__(self):
        return f"پیام از -{self.name or 'ناشناس'}   -در تاریخ {self.created_at.strftime('%y-%m-%d')}"

    class Meta:
        verbose_name = "پیام کاربر"
        verbose_name_plural = "پیام‌های کاربران"
        ordering = ['-created_at']
    

# class Contact(models.Model):
#     name=models.CharField(max_length=100,blank=True)
#     email=models.EmailField(blank=True)
#     subject=models.CharField(max_length=300,blank=True)
#     message=models.TextField(blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.name}-{self.subject[:30]}'
 
=======
class Message(models.Model): 
    name=models.CharField(max_length=100,blank=True) 
    text=models.TextField(blank=True) 
    email=models.EmailField() 
    created_at=models.DateTimeField(auto_now_add=True)
    birth_year=models.CharField(max_length=4,verbose_name='سال تولد',default='1400',blank=True)
    INTRO_METHOD_CHOICES = [
        ('search','از طریق جست و جو در اینترنت'),
        ('friend','از طریق دوستان'),
    ]
    intro_method = models.CharField(
        max_length=10,
        choices=INTRO_METHOD_CHOICES,
        verbose_name='نحوه آشنایی با سایت',
        default='serach',
        blank=True
    )
    def __str__(self): 
     return f'پیام از {self.name or 'ناشناس'} در {self.created_at.strftime('%Y-%m-%d')}'
# Create your models here.
>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
