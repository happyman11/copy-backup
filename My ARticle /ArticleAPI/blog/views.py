from django.shortcuts import render


import os
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.viewsets import ViewSet
from .serializers import *
import environ
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from .models import *
from django.conf import settings 
import random
from django.core.mail import send_mail
env = environ.Env()
environ.Env.read_env()
from django.core.mail import EmailMultiAlternatives
from django.template import Context
import pandas as pd


class subscribe_user(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = subscriberform_serializer

    def post(self, request, format=None):

        
        email= str(request.data.get('email'))
        phone= str(request.data.get('phone_number'))
        name=str(request.data.get('Name'))
        
        if len(email) > 0 :
            if  len(phone) > 0:
                if len( name) >0:

                    check_existance=Subscriber.objects.filter(email=email).exists()

                    if  check_existance:

                        dev = {}
                        dev["response"]="User Email Already Exists"
                        dev["Provided By:"]="RSTIWARI Api Services"
                        dev["status"]=2
                        return Response(dev)

                    else:

                        save_db=Subscriber(Name=name,
                                           phone_number=phone,
                                           email=email
                                            )
                        
                        save_db.save()  

                        data_user={"name":name,
                               
                         "button_name":"Subscribe",
                                "url_button":env('url')+"/subscribe",
                                "url_unsubscribe":env('url')+"/unsubscribe"

                                }
                        data_user={"email":email,
                        "name":name,
                        "phone":phone,
                               
                                "button_name":"Published Articles",
                               "url_button":env('url_medium'),
                                "url_unsubscribe":env('url')+"/unsubscribe"


                                }
            

                        message_user=get_template('subscribed_user.html').render(data_user)
                        subject_user="Subscribed Sucessfully - RSTiwari"
                        msg_user=EmailMessage(subject_user,message_user,env('EMAIL_HOST_USER'),[str(email)])
                        msg_user.content_subtype="html"
                        msg_user.send()

                        data_admin={"email":email,
                        "name":name,
                        "phone":phone,
                                
                                "button_name":"Admin",
                                "url_admin":env('url'),
                                "url_unsubscribe":env('url')+"/unsubscribe"


                                }
                    
                        message_admin=get_template('subscribed_admin.html').render(data_admin)
                        subject_admin="New User Added - RSTiwari"
                        msg_admin=EmailMessage(subject_admin,message_admin,env('EMAIL_HOST_USER'),[env('EMAIL_CC1')])
                        msg_admin.content_subtype="html"
                        msg_admin.send()


                        dev = {}
                        dev["response"]="User Subscribed Sucess Fully"
                        dev["Provided By:"]="RSTIWARI Api Services"
                        dev["status"]=1
                        return Response(dev)

                
                else:

                    dev = {}
                    dev["response"]="Name is Null"
                    dev["Provided By:"]="RSTIWARI Api Services"
                    dev["status"]=1.1
                    return Response(dev)


            
            else:

                dev = {}
                dev["response"]="Phone is Null"
                dev["Provided By:"]="RSTIWARI Api Services"
                dev["status"]=1.2
                return Response(dev)

        
        else:

            dev = {}
            dev["response"]=" Email is Null"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=1.3
            return Response(dev)



class  unsubscriber(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = unsubscriberform_serializer
      
    def post(self, request, format=None):

        
        email= str(request.data.get('email'))
       
        
        if len(email) > 0 :

            check_existance=Subscriber.objects.filter(email=email).exists()

            if  check_existance:

                 Subscriber.objects.filter(email=email).delete()

                 dev = {}
                 dev["response"]="Unsubscribbed Sucessfully"
                 dev["Provided By:"]="RSTIWARI Api Services"
                 dev["status"]=1
                 return Response(dev)

            else:

                dev = {}
                dev["response"]="Email does not exists"
                dev["Provided By:"]="RSTIWARI Api Services"
                dev["status"]=0
                return Response(dev)

        else:

            dev = {}
            dev["response"]=" Email is Null"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=1.3
            return Response(dev)


class  user_feedback (APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Feedback_serialiser
    
      
    def post(self, request, format=None):
        
       
            
        email= str(request.POST.get('email'))
        message= str(request.POST.get('user_feedback'))

        if len(email)>0:

            if len(message)>0:

        
                check_existance=Subscriber.objects.filter(email=email).exists()

                if  check_existance:

                    save_db=Feedback(
                            email=email,
                            user_feedback=message
                            )
                    save_db.save() 
                    
                    data_user={"email":email,
                                "feedback":message,
                                "button_name":"Subscribe",
                                "url_medium":env('url')+"/subscribe",
                                "url_unsubscribe":env('url')+"/unsubscribe"

                                }

                   
                    
                    message_user=get_template('feedback_user.html').render(data_user)
                    subject_user="Feedback Sumbition - RSTiwari"
                    msg_user=EmailMessage(subject_user,message_user,env('EMAIL_HOST_USER'),[str(email)])
                    msg_user.content_subtype="html"
                    msg_user.send()

                    data_admin={"email":email,
                                "feedback":message,
                                "button_name":"Admin",
                                "url_admin":env('url'),
                                "url_unsubscribe":env('url')+"/unsubscribe"


                                }
                    
                    message_admin=get_template('feedback_admin.html').render(data_admin)
                    subject_admin="Copy of Feedback Sumbition - RSTiwari"
                    msg_admin=EmailMessage(subject_admin,message_admin,env('EMAIL_HOST_USER'),[env('EMAIL_CC1')])
                    msg_admin.content_subtype="html"
                    msg_admin.send()  

                    dev = {}
                    dev["response"]="Feedback Sucessfully Submitted"
                    dev["Provided By:"]="RSTIWARI Api Services"
                    dev["status"]=1
                    return Response(dev)
                
                else:

                    dev = {}
                    dev["response"]="Email does not exists Please Register to submit feedback"
                    dev["Provided By:"]="RSTIWARI Api Services"
                    dev["status"]=2
                    return Response(dev)

            else:
                dev = {}
                dev["response"]="Feedback is empty"
                dev["Provided By:"]="RSTIWARI Api Services"
                dev["status"]=1.2
                return Response(dev)

        else:
            
            dev = {}
            dev["response"]="Email is empty"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=1.1
            return Response(dev)







class  email_collected_view (APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
   

    def get(self, request, format=None):
            

       
        subscriber_Data=Subscriber.objects.all()
        Name=[]
        Email=[]
        phone=[]
        
        if len(subscriber_Data) >0:
            for i in subscriber_Data:
                Name.append(i.Name)
                Email.append(i.email)
                phone.append(i.phone_number)

            Collected_email=Email_collected.objects.all()
            for i in Collected_email:
                Name.append("None")
                Email.append(i.email)
                phone.append("None")

            dev = {}
            dev["response"]="Data is Shown Below"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=1
            dev["Name"]=Name
            dev["Email"]=Email
            dev["Phone"]= phone
            return Response(dev)


        else:

            dev = {}
            dev["response"]="Database is empty"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=0
            return Response(dev)


class  email_collected_insert (APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
   

    def get(self, request, format=None):
            
  
        
        path_pandas=str(settings.BASE_DIR)+"/blog/Email-collected1.xlsx"
        names=["Emails"]
        counter=0
        dataframe=pd.read_excel(path_pandas,names=names)
        for i in dataframe["Emails"].values:
            print(i)
            counter=counter+1
            obj, created = Email_collected.objects.get_or_create(email=i)
            obj.save()

        message="Data has been inserted into database"
        data_admin={
                     "feedback":message,
                    "button_name":"Admin",
                    "url_admin":env('url'),
                    "url_unsubscribe":env('url')+"/unsubscribe",
                    "heading": "User Data Inserted",
                    "Instructions":"Please see the below file attached"
                     }
                    
        message_admin=get_template('contact_admin_custom.html').render(data_admin)
        subject_admin="Copy of Inquiry Sumbition - RSTiwari"
        msg_admin=EmailMessage(subject_admin,message_admin,env('EMAIL_HOST_USER'),[env('EMAIL_CC1')])
        msg_admin.attach_file(path_pandas)
        msg_admin.content_subtype="html"
        msg_admin.send()

         
        

        dev = {}
        dev["response"]="Data is Inserted"
        dev["Provided By:"]="RSTIWARI Api Services"
        dev["status"]=200
       
        return Response(dev)


class  email_stored_mailed_mass (APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    serializer_class=email_stored_template

   

    def post(self, request, format=None):



        subject            =  request.data.get('subject')
        title              =   request.data.get('title')
        links_image        =  request.data.get('links_image')
        button_title       =  request.data.get('button_title')
        links_button       =  request.data.get('links_button')
        paragraph1         =  request.data.get('paragraph1')
        paragraph2         =  request.data.get('paragraph2')
        
        


        if  subject and title  and links_image and button_title and links_button and paragraph1 :
            
            start=0
            Email=[]
            email_bulk=200
            sent_response=[]
            data={
                    "Title":title,
                    "Paragraph1":paragraph1,
                    "Paragraph2":paragraph2,
                    "ImageLink": links_image,
                    "ButtonLink": links_button,
                    "ButtonName": button_title
                 }
            
            
            subscriber_Data=Subscriber.objects.all()
            if len(subscriber_Data) >0:
                for i in subscriber_Data:
                    Email.append(i.email)
            

            Collected_email=Email_collected.objects.all()
            for i in Collected_email:
                Email.append(i.email)
        
 
            loop_iteration=int(len(Email)//200)
            add_extra=len(Email)%200
            print("Loop Count::::",loop_iteration)
            print("Remainder mails:::",add_extra)

                   
            
            message_admin=get_template('Broadcastmail/massmail_template.html').render(data)

            for i in range(0,loop_iteration+1):
                
                print(" Looping for round ",i, "Out of ", loop_iteration)
                recievers=Email[start:start+email_bulk]
                try:
                    
                    subject_admin=str(subject)
                    msg_admin=EmailMessage(subject,message_admin,env('EMAIL_HOST_USER'),bcc=Email)
                    msg_admin.content_subtype="html"
                    msg_admin.send()
                    resp=[[Emails],"Mail Sent Successfully",]
                    sent_response.append(resp)
                    
                    start=start+email_bulk
                    print("Mail Sent to emails",recievers,   "count:::::", start )

            
                except:
                    resp=[[Emails],"Mail Sending Failed"]
                    print("Mail Failed to emails",recievers, len(recievers) )
                    sent_response.append(resp)
                    start=start+email_bulk

            try:
                
                recievers=Email[start*email_bulk:add_extra+start*email_bulk]
                subject_admin=str(subject)
                msg_admin=EmailMessage(subject,message_admin,env('EMAIL_HOST_USER'),bcc=Emails)
                msg_admin.content_subtype="html"
                msg_admin.send()
                resp=[[Emails],"Mail Sent Successfully",]
                sent_response.append(resp)
                    
                print("Mail Sent to emails",recievers,   "count:::::", start )
                    
            
            except:
                
                resp=[[Emails],"Mail Sending Failed"]
                print("Mail Failed to emails",recievers, len(recievers) )
                sent_response.append(resp)

                    
            
 
            dev                  =   {}
            dev["Provided By:"]  =  "RSTIWARI Api Services"
            dev["response"]      =   sent_response
            dev["status"]        =   200

            save_info            =   Mass_Email_detail(
                                                        subject=subject
                                                       )
            save_info.save()
            return Response(dev)
                   
                    
        else:
               
            dev                  =   {}
            dev["Provided By:"]  =  "RSTIWARI Api Services"
            dev["response"]      =   "Input Arguments is empty"
            dev["status"]        =   400
            return Response(dev)



class  template_email_stored_mailed_mass (APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    serializer_class=email_stored_template_mail

   

    def post(self, request, format=None):



        subject            =  request.data.get('subject')
        context            =  request.data.get('content')
        
        
    
        if  subject and context :
            
            start=0
            Email=[]
            email_bulk=200
            sent_response=[]
            
            
            subscriber_Data=Subscriber.objects.all()
            if len(subscriber_Data) >0:
                for i in subscriber_Data:
                    Email.append(i.email)
            

            Collected_email=Email_collected.objects.all()
            for i in Collected_email:
                Email.append(i.email)
        
 
            loop_iteration=int(len(Email)//200)
            add_extra=len(Email)%200
            print("Loop Count::::",loop_iteration)
            print("Remainder mails:::",add_extra)

                   
            
           
            for i in range(0,loop_iteration+1):
                
                print(" Looping for round ",i, "Out of ", loop_iteration)
                recievers=Email[start:start+email_bulk]
                try:
                    
                    subject_admin=str(subject)
                    msg_admin=EmailMessage(subject,str(context),env('EMAIL_HOST_USER'),bcc=Email)
                    msg_admin.content_subtype="html"
                    msg_admin.send()
                    resp=[[Emails],"Mail Sent Successfully",]
                    sent_response.append(resp)
                    
                    start=start+email_bulk
                    print("Mail Sent to emails",recievers,   "count:::::", start )

            
                except:
                    resp=[[Emails],"Mail Sending Failed"]
                    print("Mail Failed to emails",recievers, len(recievers) )
                    sent_response.append(resp)
                    start=start+email_bulk

            try:
                
                recievers=Email[start*email_bulk:add_extra+start*email_bulk]
                subject_admin=str(subject)
                msg_admin=EmailMessage(subject,str(context),env('EMAIL_HOST_USER'),bcc=Emails)
                msg_admin.content_subtype="html"
                msg_admin.send()
                resp=[[Emails],"Mail Sent Successfully",]
                sent_response.append(resp)
                    
                print("Mail Sent to emails",recievers,   "count:::::", start )
                    
            
            except:
                
                resp=[[Emails],"Mail Sending Failed"]
                print("Mail Failed to emails",recievers, len(recievers) )
                sent_response.append(resp)

                    
            
 
            dev                  =   {}
            dev["Provided By:"]  =  "RSTIWARI Api Services"
            dev["response"]      =   sent_response
            dev["status"]        =   200

            save_info            =   Mass_Email_detail(
                                                        subject=subject
                                                       )
            save_info.save()
            return Response(dev)
                   
                    
        else:
               
            dev                  =   {}
            dev["Provided By:"]  =  "RSTIWARI Api Services"
            dev["response"]      =   "Input Arguments is empty"
            dev["status"]        =   400
            return Response(dev)




####BLog Article API




class  get_blog_articles(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
   

    def get(self, request, format=None):
            

       
        blog_Data           =  blog_article_data.objects.all()

        Title               =  []
        article_link        =  []
        image_url           =  []
        links_image         =  []
        publisheddate       =  []
        category            =  []
        timestamp           =  []
        
        if len(blog_Data) >0:

            count=len(blog_Data)


            for i in blog_Data:


                Title.append(i.article_title)
                category.append(i.category)
                timestamp.append(i.timestamp)
                image_url.append(i.image_url)
                links_image.append(i.links_image)
                article_link.append(i.article_urls)
                publisheddate.append(i.publisheddate)
                

           

            dev = {}
            dev["response"]="Data is Shown Below"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=200
            dev["data count"]=count
            dev["Title"]=Title
            dev["category"]=category
            dev["timestamp"]=timestamp
            dev["image_url"]=image_url
            dev["links_image"]= links_image
            dev["article_link"]=article_link
            dev["publisheddate"]=publisheddate
            
            return Response(dev)


        else:

            dev = {}
            dev["response"]="Database is empty"
            dev["Provided By:"]="RSTIWARI Api Services"
            dev["status"]=200
            return Response(dev)



class  add_blog_articles(APIView):

    authentication_classes    = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes        = [IsAuthenticated]
    serializer_class        = submit_article
   

    def post(self, request, format=None):
            

       
       

        Title               =  request.data.get("article_title")
        article_url         =  request.data.get("article_urls")
        image_url           =  request.data.get("image_url")
        links_image         =  request.data.get("links_image")
        publisheddate       =  request.data.get("publisheddate")
        category            =  request.data.get("category")



       
        
        if Title  and image_url and links_image and publisheddate and category:

            print(Title)
            print(article_url)
            print(image_url)
            print(links_image)
            print(publisheddate)
            print(category)
           
            


            article_data,created  =  blog_article_data.objects.get_or_create( article_title=Title,
                                                                         article_urls=article_url,
                                                                         image_url=image_url,
                                                                         category=category,
                                                                         links_image=links_image,
                                                                         publisheddate=publisheddate
                                                                        )
                                                                       
           

            if created:

                dev                 = {}
                dev["response"]     = "Database Updated Sucessfully"
                dev["Provided By:"] = "RSTIWARI Api Services"
                dev["status"]       = 200
                return Response(dev)

            else:


                dev                 = {}
                dev["response"]     = "Information is already existing"
                dev["Provided By:"] = "RSTIWARI Api Services"
                dev["status"]       = 200
                return Response(dev)




        else:

            dev                 =   {}
            dev["response"]     =   "Invalid Payloadss"
            dev["Provided By:"] =   "RSTIWARI Api Services"
            dev["status"]       =   200
            return Response(dev)




          
            


            

       

        
       

       
        


            
           
            

        
                

                

    




    
 

        