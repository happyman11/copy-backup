from django.contrib import admin

from blog.models import (
                            Feedback,
                            Subscriber,
                            Email_collected, 
                            blog_article_data,
                            Mass_Email_detail,
                        
                        )
admin.site.register(Feedback)
admin.site.register(Subscriber)
admin.site.register(blog_article_data)
admin.site.register(Email_collected)
admin.site.register( Mass_Email_detail)

