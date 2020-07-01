from django.contrib import admin

# Register your models here.
# from .models import Reporter, Article

# admin.site.register(Article)
# admin.site.register(Reporter)

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)