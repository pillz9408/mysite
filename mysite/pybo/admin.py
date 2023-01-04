from django.contrib import admin
#추가
from .models import Question
# Register your models here.
# 추가
class QusetionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QusetionAdmin)