from django.contrib import admin

# Register your models here.
from .models import Teamer, Choice

#admin.site.register(Teamer)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class TeamerAdmin(admin.ModelAdmin):
    list_display = ('dayily_voice', 'english_name', 'Birthday', 'was_birthday_recently')
    list_filter = ['Birthday']
    search_fields = ['dayily_voice']
    fieldsets = [
        (None, {'fields': ['dayily_voice']}),
        ('Birthdy', {'fields': ['Birthday'], 'classes': ['collapse']}),
        (None, {'fields': ['english_name', 'Chinese_name', 'sex', 'phone', 'position', 'hobby']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Teamer, TeamerAdmin)
