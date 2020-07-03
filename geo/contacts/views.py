from django.contrib import messages
from django.core import serializers
from django.core.serializers import serialize 
from django.shortcuts import render, redirect
from .forms import ContactA00Form, ContactA01Form, ContactA02Form, ContactA03Form, ContactA04Form, GroupA00Form, GroupA01Form
from .models import ContactContactA00, ContactContactA01, ContactContactA02, ContactContactA03, ContactContactA04, ContactGroupA00, ContactGroupA01
import requests
import json


# Create your views here.
def contact(request):
    
    if request.user.is_superuser:
        contact = ContactContactA00.objects.all()
        skill = ContactContactA01.objects.all()
        endorsement = ContactContactA02.objects.all()
        sample_work = ContactContactA03.objects.all()
        deduction = ContactContactA04.objects.all()
    else:
        contact = ContactContactA00.objects.get(contact_a00_rec = request.user.id)
        skill = ContactContactA01.objects.get(contact_id = request.user.id)
        endorsement = ContactContactA02.objects.get(contact_id = request.user.id)
        sample_work = ContactContactA03.objects.get(contact_id = request.user.id)
        deduction = ContactContactA04.objects.get(contact_id = request.user.id)
    context = {
       "contact": contact,
       "skill": skill,
       "endorsement": endorsement,
       "sample_work": sample_work,
       "deduction": deduction,

    }
    return render(request, 'contacts/contact.html', context)
def add_contact(request):
    form = ContactA00Form()
    
    #checks if the HTTP method used is POST
    if request.method == 'POST':
        form = ContactA00Form(request.POST)
        if form.is_valid():
            
            #get the inputs from the forms
            first_name = form.cleaned_data.get('first_name')
            middle_initial = form.cleaned_data.get('middle_initial')
            last_name = form.cleaned_data.get('last_name')
            address_1 = form.cleaned_data.get('address_1')
            barangay_district = form.cleaned_data.get('barangay_district')
            city_municipality = form.cleaned_data.get('city_municipality')
            postal_code = form.cleaned_data.get('postal_code')
            province = form.cleaned_data.get('province')
            phone_1 = form.cleaned_data.get('phone_1')
            phone_2 = form.cleaned_data.get('phone_2')
            email = form.cleaned_data.get('email')
            created_by_id = request.user.id
            
            #json data to be sent to the API
            data = {
                "first_name": first_name,
                "middle_initial": middle_initial,
                "last_name": last_name,
                "address_1": address_1,
                "barangay_district": barangay_district,
                "city_municipality": city_municipality,
                "postal_code":postal_code,
                "province":province,
                "phone_1":phone_1,
                "phone_2":phone_2,
                "email":email,
                "created_by": created_by_id
            }

            #api format
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact/', json=data, headers=header)
            
            #message to the UI
            messages.success(request, f'You have successfully created a contact!')
            return redirect('contact-contact')

            

    else:
        form = ContactA00Form()
    context = {
        "form":form,
        "header": 'Contact | Register Contact'
    }
    return render(request, 'contacts/add_contact.html', context)

def add_skill(request):
    form = ContactA01Form()
    if request.method == 'POST':
        form = ContactA01Form(request.POST)
        if form.is_valid():
            comments = form.cleaned_data.get('comments')
            skill_id = form.cleaned_data.get('skill_id')

            contact = ContactContactA00.objects.get(created_by_id = request.user.id)
            contact_id = contact.contact_a00_rec
            

            data = {
                "skill_id": skill_id,
                "comments": comments,
                "contact_id": contact_id
            }
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact-detail/', json=data, headers=header)
            print(r)
            
            messages.success(request, f'You have successfully added a skill!')
            return redirect('contact-contact') 
    else:
        form = ContactA01Form()
    context = {
        "form": form,
        "header": 'Contact | Add Skill'
    }
    return render(request, 'contacts/add_skill.html', context)

def add_endorsement(request):
    form = ContactA02Form()
    if request.method == 'POST':
        form = ContactA02Form(request.POST)
        if form.is_valid():
            endorsement_id = form.cleaned_data.get('endorsement_id')
            message = form.cleaned_data.get('message')
            contact = ContactContactA00.objects.get(created_by_id = request.user.id)
            contact_id = contact.contact_a00_rec



            data = {
                "endorsement_id": endorsement_id,
                "message": message,
                "contact_id": contact_id

            }
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact-endorsement/', json=data, headers=header)
            print(r)
            messages.success(request, f'You have successfully added an endorsement!')
            return redirect('contact-contact') 
    else:
        form = ContactA02Form()
    context = {
        "form": form,
        "header": 'Contact | Add Endorsement'
    }
    return render(request, 'contacts/add_endorsement.html', context)

def add_sample_work(request):
    form = ContactA03Form()
    if request.method == 'POST':
        form = ContactA03Form(request.POST)
        if form.is_valid():
            sample_work_id = form.cleaned_data.get('sample_work_id')
            file_name = form.cleaned_data.get('file_name')
            comments = form.cleaned_data.get('comments')
            contact = ContactContactA00.objects.get(created_by_id = request.user.id)
            contact_id = contact.contact_a00_rec



            data = {
                "sample_work_id": sample_work_id,
                "file_name": file_name,
                "comments": comments,
                "contact_id": contact_id
        
            }
            print(data)
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact-sample-work/', json=data, headers=header)
            print(r)
            messages.success(request, f'You have successfully added a sample work!')
            return redirect('contact-contact') 
    else:
        form = ContactA03Form()
    context = {
        "form": form,
        "header": 'Contact | Add Sample Work'
    }
    return render(request, 'contacts/add_sample_work.html', context)

def add_deductions(request):
    form = ContactA04Form()
    if request.method == 'POST':
        form = ContactA04Form(request.POST)
        if form.is_valid():
            contact_deduction_id = form.cleaned_data.get('contact_deduction_id')
            deduction_id_id = form.cleaned_data.get('deduction_id_id')
            deduction_id =deduction_id_id.ref_a01_rec
            comments = form.cleaned_data.get('comments')
            contact = ContactContactA00.objects.get(created_by_id = request.user.id)
            contact_id = contact.contact_a00_rec


            
            data = {
                "contact_deduction_id": contact_deduction_id,
                "comments": comments,
                "contact_id": contact_id,
                "deduction_id": deduction_id
        
            }
            print(data)
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact-deduction/', json=data, headers=header)
            print(r)
            messages.success(request, f'You have successfully added a deduction!')
            return redirect('contact-contact') 
    else:
        form = ContactA04Form()
    context = {
        "form": form,
        "header": 'Contact | Add Deduction'
    }
    return render(request, 'contacts/add_deduction.html', context)


def group(request):
    if request.user.is_superuser:
        group = ContactGroupA00.objects.all()
        group_role = ContactGroupA01.objects.all()
    else:
        group = ContactGroupA00.objects.all()
        group_role = ContactGroupA01.objects.all()
    context = {
        "group": group,
        "group_role": group_role
    }
    return render(request, 'contacts/group.html', context)

def add_group(request):
    form = GroupA00Form()
    if request.method == 'POST':
        form = GroupA00Form(request.POST)
        if form.is_valid():
            #get the inputs from the forms
           
            name = form.cleaned_data.get('name')
            address_1 = form.cleaned_data.get('address_1')
            barangay_district = form.cleaned_data.get('barangay_district')
            city_municipality = form.cleaned_data.get('city_municipality')
            postal_code = form.cleaned_data.get('postal_code')
            province = form.cleaned_data.get('province')
            phone_1 = form.cleaned_data.get('phone_1')
            phone_2 = form.cleaned_data.get('phone_2')
            email = form.cleaned_data.get('email')
            agent = form.cleaned_data.get('agent')
            
            print(agent)
            data = {
                "name": name,
                "address_1": address_1,
                "barangay_district": barangay_district,
                "city_municipality": city_municipality,
                "postal_code":postal_code,
                "province":province,
                "phone_1":phone_1,
                "phone_2":phone_2,
                "email":email,
                "agent":agent
            }
            print(data)
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/group/', json=data, headers=header)
            print(r)

            messages.success(request, f'You have successfully created a group!')
            return redirect('contact-group') 
    else:
        form = GroupA00Form()
    context = {
        "form": form,
        "header": 'Contact | Create Group'
    }
    return render(request, 'contacts/add_group.html', context)

def add_group_role(request):
    form = GroupA01Form()
    if request.method == 'POST':
        form = GroupA01Form(request.POST)
        if form.is_valid():
            group_role = form.cleaned_data.get('group_role')
            comments = form.cleaned_data.get('comments')
            contact = ContactContactA00.objects.get(created_by_id = request.user.id)
            contact_id = contact.contact_a00_rec
            group_data = form.cleaned_data.get('group_id')
            group = ContactGroupA00.objects.get(group_a00_rec = group.group_a00_rec)
            group_id = group_id.group_a00_rec
            
            
            data = {
                "group_role": group_role,
                "comments": comments,
                "contact_id": contact_id,
                "group_id": group_id,
                
            }
            print(data)
            header = {"Content-Type": "application/json"}
            r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/group-detail/', json=data, headers=header)
            print(r)

            messages.success(request, f'You have successfully created a group!')
            return redirect('contact-group') 
    else:
        form = GroupA01Form()
    context = {
        "form": form,
        "header": 'Contact | Add Role'
    }
    return render(request, 'contacts/add_group_role.html', context)