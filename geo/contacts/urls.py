from django.urls import path, include
from .views import contact, add_contact, add_skill, add_endorsement,add_sample_work, add_deductions, group, add_group, add_group_role
urlpatterns = [
    path('contact/', contact, name='contact-contact'),
    path('contact/add/', add_contact, name='contact-add'),
    path('contact/skill/add/', add_skill, name='contact-skill-add'),
    path('contact/endorsement/add/', add_endorsement, name='contact-endorsement-add'),
    path('contact/sample/add/', add_sample_work, name='contact-sample-add'),
    path('contact/deduction/add/', add_deductions, name='contact-deduction-add'),

    path('group/', group, name='contact-group'),
    path('group/add/', add_group, name='contact-group-add'),
    path('group/role/add/', add_group_role, name='contact-group-role-add'),

]
