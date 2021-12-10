from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', blank=True)
    bio = models.TextField(max_length=300, default="Bio", blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Image(models.Model):
    img_name = models.CharField(max_length=80)
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=100,blank=True)
    image = CloudinaryField('images')

    def __str__(self):
        return self.img_name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_post(cls, name):
        return cls.objects.filter(img_name__img__name__icontains=name)
    
    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.user.user} Image'

    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()


class Like(models.Model):
    image = models.ForeignKey(Image,related_name='upvotes',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.image
    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['user', 'image'], name="unique_like"),
            ]