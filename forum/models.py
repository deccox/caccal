from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import  slugify
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

class Profile(models.Model):
    bio = models.CharField(max_length=100, blank=True, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True,null=False)
    pic_profile = ResizedImageField(size=[200,200], quality=100, upload_to="forum/static/profile-img/")
    

    def get_url(self):
        return reverse("profile", kwargs={'slug':self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Perfils"

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    desc = HTMLField(blank=False, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True,null=False)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    vote_like = models.IntegerField(default=0)
    vote_Deslike = models.IntegerField(default=0)

    def get_url(self):
        return reverse("post", kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    class Meta:
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    desc = HTMLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)
    vote_like = models.IntegerField(default=0)
    vote_Deslike = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Comentarios"
        
    def __str__(self):
        return self.desc
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
