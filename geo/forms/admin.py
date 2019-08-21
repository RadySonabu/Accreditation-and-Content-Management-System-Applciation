from django.contrib import admin
from .models import Division, Subdivision, SubdivisionDetail, AccreditationType, Forms


class FormsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']


admin.site.register(Division)
admin.site.register(Subdivision)
admin.site.register(SubdivisionDetail)
admin.site.register(AccreditationType)
admin.site.register(Forms, FormsAdmin)
