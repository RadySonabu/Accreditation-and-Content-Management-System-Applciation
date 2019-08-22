from django.contrib import admin
from .models import Division, Subdivision, SubdivisionDetail, AccreditationType, Forms

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class FormsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']


admin.site.register(Division)
admin.site.register(Subdivision)
admin.site.register(SubdivisionDetail)
admin.site.register(AccreditationType)
admin.site.register(Forms, FormsAdmin)


# default: "Django Administration"
admin.site.site_header = 'Accreditation Content Management System with Analytics - Administrator Panel'
# default: "Site administration"
admin.site.index_title = 'Dynamic area'
admin.site.site_title = 'Adminsitration'
