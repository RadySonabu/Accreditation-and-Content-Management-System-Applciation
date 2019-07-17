from import_export import resources
from .models import MyUser


class Members(resources.ModelResource):
    class Meta:
        model = MyUser
