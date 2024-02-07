from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Role,Employee,Experience,Source,Company,User,JobListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404



def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html',) 
    # return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if the user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")









def company(request):
    emp=Company.objects.all()
    items_per_page = 6 # You can adjust this value

    # Create a Paginator object
    paginator = Paginator(emp, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the page object for the given page number
        emp = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        emp = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        emp = paginator.page(paginator.num_pages)
    context={
        'emp':emp
    }
    return render(request, 'company.html',context)
def dataAdd(request):
    if request.method =="POST":
        company =request.POST.get("company")
        website =request.POST.get("website")
        address = request.POST.get("address_company")
        contact = request.POST.get("company_contact")

        emp=Company(
            company_name=company,
            company_website=website,
            company_address=address,
            company_contact=contact
        )
        emp.save() 
        return redirect('company')  
    
    


def Editcompanylist(request):
    emp = Company.objects.all()
    context = {'emp': emp}
    return render(request, 'company.html', context)



def updatecompanylist(request, id):
    emp = get_object_or_404(Company, id=id)

    if request.method == "POST":
        company = request.POST.get("company")
        website = request.POST.get("website")
        address = request.POST.get("address_company")
        contact = request.POST.get("company_contact")

        emp.company_name = company
        emp.company_website = website
        emp.company_address = address
        emp.company_contact = contact
        emp.save()

        return redirect('company')

    return render(request, 'company.html')   

def Delete2(request,id):
    emp=Company.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp
    }
    return redirect('company')


   












def joblisting(request):
    emp1=JobListing.objects.all()
    items_per_page = 6 # You can adjust this value

    # Create a Paginator object
    paginator = Paginator(emp1, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the page object for the given page number
        emp1 = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        emp1 = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        emp1 = paginator.page(paginator.num_pages)

    context = {'emp1': emp1}
    return render(request, 'joblisting.html',context)
def ADD(request):
    if request.method == "POST":
        job_title = request.POST.get("job_title")
        salary = request.POST.get("salary")
        description = request.POST.get("description")
        location = request.POST.get("location")
        type = request.POST.get("type")
        date_of_post = request.POST.get("date_of_post")
        job_description = request.POST.get("job_description")
        date_of_scrap = request.POST.get("date_of_scrap")
        source_id = request.POST.get("source_id")
        company_id = request.POST.get("company_id")
        emp1=JobListing(
            job_title=job_title,
            salary = salary,
            description = description,
            location = location,
            type = type,
            date_of_post = date_of_post,
            job_description = job_description,
            date_of_scrap = date_of_scrap,
            source_id = source_id,
            company_id = company_id,
        )
        emp1.save() 
        return redirect('joblisting') 
    
def Edit(request,id):
    emp1=JobListing.objects.all()
    context = {'emp1': emp1}
    return redirect('joblisting',context)   


# def update(request,id):
#     if request.method =="POST":
#         print("inside post")
#         job_title = request.POST.get("job_title")
#         salary = request.POST.get("salary")
#         description = request.POST.get("description")
#         location = request.POST.get("location")
#         type = request.POST.get("type")
#         date_job_post = request.POST.get("date_job_post")
#         job_description = request.POST.get("job_description")
#         date_of_scrap = request.POST.get("date_of_scrap")
#         job_id = request.POST.get("job_id")
#         # source_id = request.POST.get("source_id")
#         # company_id = request.POST.get("company_id")
#         emp1=JobListing(
#             id=id,
#             job_title=job_title,
#             salary = salary,
#             description = description,
#             location = location,
#             type = type,
#             date_job_post=date_job_post,
#             date_of_scrap = date_of_scrap,
#             job_description = job_description,
#             job_id=job_id,
#             # source_id=source_id,
#             # company_id=company_id
#         )
#         # emp_dict = {
#         #     "id":id,
#         #     "job_title":job_title,
#         #     "salary": salary,
#         #     "description" :description,
#         #     "location" :location,
#         #     "type": type,
#         #     "date_job_post":date_job_post,
#         #     "date_of_scrap": date_of_scrap,
#         #     "job_description": job_description,
#         # }
#         # print(emp_dict)
#         emp1.save()
#         return redirect('joblisting')
#     return redirect(request,'joblisting.html')
from django.shortcuts import render, redirect
from .models import JobListing  # Import your JobListing model

def update(request, id):
    if request.method == "POST":
        job_title = request.POST.get("job_title")
        salary = request.POST.get("salary")
        description = request.POST.get("description")
        location = request.POST.get("location")
        type = request.POST.get("type")
        date_job_post = request.POST.get("date_job_post")
        job_description = request.POST.get("job_description")
        date_of_scrap = request.POST.get("date_of_scrap")
        source_id = request.POST.get("source_id")  # Get the source_id from the form
        company_id = request.POST.get("company_id")  # Get the company_id from the form
        
        # Retrieve the JobListing instance by id
        job_listing = JobListing.objects.get(id=id)
        
        # Update the fields with new values
        job_listing.job_title = job_title
        job_listing.salary = salary
        job_listing.description = description
        job_listing.location = location
        job_listing.type = type
        job_listing.date_job_post = date_job_post
        job_listing.job_description = job_description
        job_listing.date_of_scrap = date_of_scrap
        job_listing.source_id_id = source_id  # Assign the source_id
        job_listing.company_id_id = company_id  # Assign the company_id
        
        # Save the updated instance
        job_listing.save()
        
        return redirect('joblisting')
    else:
        return render(request, 'joblisting.html')  # Render the template if not POST request
















     
def Delete3(request,id):
    emp1=JobListing.objects.filter(id=id)
    emp1.delete()
    context={
        'emp1':emp1    }
    return redirect('joblisting')




def role(request):
    return render(request, 'role.html')

def user(request):
    return render(request, 'user.html')

def source(request):
    return render(request, 'source.html')

def datasourceAdd(request):
    if request.method =="POST":
        id =request.POST.get("id")
        name =request.POST.get("name")
        emp0=Company(
            id=id,
            name=name,
        )
        emp0.save() 
        return redirect('source') 
    
    
def Experience(request):
    return render(request, 'Experience.html')
def Employee(request):
    return render(request, 'Employee.html')
