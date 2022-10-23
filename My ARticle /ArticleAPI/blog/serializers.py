from rest_framework import serializers
from .models import (
                         blog_article_data,
                         Mass_Email_detail,
                    )




class Feedback_serialiser(serializers.Serializer):
    email = serializers.EmailField()
    user_feedback=serializers.CharField(max_length = 2000)
    class Meta:
        fields = '__all__'

class unsubscriberform_serializer(serializers.Serializer):
  
    email = serializers.EmailField(required=True,label='Email')
    class Meta:
        fields = '__all__'

class subscriberform_serializer(serializers.Serializer):
  
    Name        = serializers.CharField(max_length = 20)
    phone_number=serializers.CharField(max_length = 12)
    email = serializers.EmailField()
    timestamp=serializers.DateTimeField()
    class Meta:
        fields = '__all__'

class email_stored_template(serializers.ModelSerializer):
   class Meta:
        model = Mass_Email_detail
        
        fields = ['subject','title','links_image','button_title','links_button','paragraph1','paragraph2']

class email_stored_template_mail(serializers.ModelSerializer):
   
   
   class Meta:
        model = Mass_Email_detail
        fields = ['subject','content']



#blog Article serializer



class submit_article(serializers.ModelSerializer):
   
   
   class Meta:
        model = blog_article_data
        fields = ['article_title', 'article_urls','image_url', 'links_image','publisheddate','category']




   
