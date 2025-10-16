from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

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
    
class Message(models.Model): 
    title=models.CharField(max_length=100) 
    text=models.TextField() 
    email=models.EmailField() 
    created_at=models.DateTimeField(auto_now_add=True,null=True) 
 
    def __str__(self): 
     return self.title
    

    
# Create your models here.
