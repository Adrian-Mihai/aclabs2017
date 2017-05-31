from django.contrib import admin

from .models import Question, Poll, Choice

class PollAdmin(admin.ModelAdmin):
    list_field = ('name')

class Meta:
    name = Poll

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Poll)