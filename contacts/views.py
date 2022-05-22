from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact
from .Form import saveContact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django import poll_choice
@login_required
def index(request):
    #return HttpResponse("contacts details")
    print('login index', request,request.user)
    contacts=contact.objects.filter(contactholder=request.user)
    if request.method =="POST":
        form=saveContact(request.POST or None)
        print("form", form.errors)
        if form.is_valid():
            form.save(commit=False).contactholder=request.user
            form.save()
            for field in form:
                if field.errors:
                    print('error',field.errors)
                else:
                    print("field name", field.name)
            messages.success(request,("Contact has been addedd successfully"))
        #return render(request, "index.html", {'contacts': contacts})
        return redirect("../../contacts")
    else:
        return render(request,"index.html",{'contacts':contacts})
@login_required
def delete(request, contact_id):
    contacts = contact.objects.get(pk=contact_id)
    contacts.delete()
    messages.success(request, ("Contact has been deleted successfully"))
    return redirect('../../contacts')

@login_required
def edit(request,contact_id):
    print('edit',request)
    if request.method=="POST":
        contacts=contact.objects.get(pk=contact_id)
        form=saveContact(request.POST or None,instance=contacts)
        if form.is_valid():
            form.save()
            messages.success(request, ("Contact has been updated successfully"))
        else:
            print("Update Request Not processed")
        return redirect('../../contacts')
    else:
        contacts = contact.objects.get(pk=contact_id)
        return render(request,"edit.html",{'contacts':contacts})
# Create your views here.
