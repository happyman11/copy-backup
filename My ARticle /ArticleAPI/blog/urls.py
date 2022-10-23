from django.urls import include, path
from blog.views import add_blog_articles,get_blog_articles, subscribe_user,unsubscriber,email_stored_mailed_mass,template_email_stored_mailed_mass,user_feedback,email_collected_view,email_collected_insert
from rest_framework import routers



urlpatterns = [
   
   
path('subscribe/', subscribe_user.as_view(), name="subscribe"),
path('unsubscribe/', unsubscriber.as_view(), name="unsubscribe"), 
path('feedback/', user_feedback.as_view(), name="user_feedback"),     
path('get_info_subscriber/', email_collected_view .as_view(), name="get_info"),  
path('insert_info_collected/', email_collected_insert.as_view(), name="insert_info_collected"),
path('massmailbytemplatestored/',email_stored_mailed_mass.as_view(), name="mailbytemplate"),
path('massmailbytemplateapi/',template_email_stored_mailed_mass.as_view(), name="mailbytemplateapi"),


#Blog_APi get_blog_articles, add_blog_article
path('get_articles/',get_blog_articles.as_view(), name="view_article_list"),
path('post_articles/',add_blog_articles.as_view(), name="add_article_list"),




]