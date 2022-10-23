from django.db import models
from django.utils import timezone
# Create your models here.

class Subscriber(models.Model):

    Name = models.CharField(max_length = 20,blank=False)
    phone_number=models.CharField(max_length = 12,blank=False)
    email = models.EmailField(blank=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Subscriber: {}".format(self.email)
    

class Feedback(models.Model):

    
    email = models.EmailField(blank=False)
    user_feedback=models.TextField(blank=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Subscriber: {}".format(self.email)


class Email_collected(models.Model):

    
    email = models.EmailField(blank=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Subscriber: {}".format(self.email)


class Mass_Email_detail(models.Model):

  content            =  models.TextField(blank=True,null=True)
  subject            =  models.CharField(max_length=300,blank=False,null=False)
  title              =  models.CharField(max_length=300,blank=True,null=True)
  links_image        =  models.CharField(max_length=300,blank=True,null=True)
  button_title       =  models.CharField(max_length=300,blank=True,null=True)
  links_button       =  models.CharField(max_length=300,blank=True,null=True)
  paragraph1         =  models.CharField(max_length=300,blank=True,null=True)
  paragraph2         =  models.CharField(max_length=300,blank=True,null=True)
  sent_at            =  models.DateTimeField(default=timezone.now ,null=False, blank=False)

  def __str__(self):
        
      return "Subject : {}|| Sent_at : {}".format(self.subject,self.sent_at)
  def save(self, *args, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        return super(Mass_Email_detail, self).save(*args, **kwargs)



class blog_article_data(models.Model):

  article_title               =  models.CharField(max_length=300,blank=False,null=False)
  article_urls                =  models.CharField(max_length=300,blank=False,null=False)
  image_url                   =  models.CharField(max_length=300,blank=True,null=True)
  links_image                 =  models.CharField(max_length=300,blank=True,null=True)
  publisheddate               =  models.DateTimeField(blank=True,null=True)
  category                    =  models.TextField(blank=True,null=True)
  timestamp                   =  models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        
      return "Title : {}  || Published Date : {}".format(self.article_title,self.publisheddate)


  def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        return super(blog_article_data, self).save(*args, **kwargs)

