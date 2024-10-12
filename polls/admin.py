from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class PollsAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('question_text', 'pub_date', 'slug')


admin.site.register(Question, PollsAdmin)    
admin.site.register(Choice)
