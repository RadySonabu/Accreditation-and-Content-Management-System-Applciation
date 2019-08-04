from django.contrib import admin
from .models import BasicInfo, Division, Subdivision, SubdivisionDetail, AccreditationType, Forms


class FormsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']
    filter_horizontal = ('subdivision_detail',)


admin.site.register(BasicInfo)
admin.site.register(Division)
admin.site.register(Subdivision)
admin.site.register(SubdivisionDetail)
admin.site.register(AccreditationType)
admin.site.register(Forms, FormsAdmin)
