from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Transpollis Admin"
admin.site.site_title = "Inec officer area"
admin.site.index_title = "Dont be a corrput officer, You have millions of lives to save"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes':
                ['collapse']}), ]
    inlines = [ChoiceInline]

# admin.site.register(Question),
admin.site.register(Question, QuestionAdmin)