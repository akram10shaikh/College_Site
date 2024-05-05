from django.shortcuts import render,redirect
from college.models import Student,StudentData
import random

# Create your views here.
def home(request):
    return render(request, 'index.html')

def apply(request):
    return render(request,'apply.html')

def login(request):
    return render(request,'login.html')

def appl_form(request):
    user = request.session.get('email')
    return render(request,'appl_form.html',{'user':user})

def details_view(request):
    user = request.session.get('email')
    return render(request,'detail.html',{'user':user})


def applyfirst(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Student.objects.filter(email=email).exists():
            error_message = "Email already exists try different name"
            return render(request,'apply.html',{'output':error_message})

        data = Student.objects.create(email=email,password=password)
        output = "Email register successfully"
        return render(request,'apply.html',{'output':output})

    return render(request,'apply.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        try:
            user = Student.objects.get(email=email,password=password)
            request.session['email'] = email
            return redirect('appl_form')
        except Student.DoesNotExist:
            error = "Invalid Email Address or Password"
            return render(request,'login.html',{'error':error})

    else:
        return render(request,'login')

def details(request):
    if request.method == 'POST':
        try:
            fname = request.POST.get('fname')
            sname = request.POST.get('sname')
            lname = request.POST.get('lname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            phone = request.POST.get('phone')
            email2 = request.session.get('email') # Email with session
            community = request.POST.get('community')
            nationality = request.POST.get('nationality')
            address = request.POST.get('address')
            city = request.POST.get('city')
            district = request.POST.get('district')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            rollno10 = request.POST.get('10rollno')
            year10 = request.POST.get('10year')
            board10 = request.POST.get('10board')
            rollno12 = request.POST.get('12rollno')
            year12 = request.POST.get('12year')
            board12 = request.POST.get('12board')
            photo = request.FILES['photo']
            sign = request.FILES['sign']

            data = StudentData.objects.create(fname=fname,sname=sname,lname=lname,gender=gender,dob=dob,phone=phone,
                                        email2=email2,community=community,nationality=nationality,address=address,city=city,
                                        district=district,state=state,pincode=pincode,rollno10=rollno10,year10=year10,
                                        board10=board10,rollno12=rollno12,year12=year12,board12=board12,photo=photo,sign=sign)
            data.save()

            data1 = StudentData.objects.get(phone=phone)
            user = request.session.get('email')
            return render(request,'details.html',{'i':data1,'user':user})

        except StudentData.MultipleObjectsReturned:
            user = request.session.get('email')
            error = "The phone number is already register by the other student"
            return render(request, 'appl_form.html', {'error': error,'user':user})



def logout(request):
    return render(request,'login.html')


def dashboard(request):
    if request.method == 'POST':
        email = request.POST.get('uuemail')
        password = request.POST.get('uupassword')
        try:
            user = Student.objects.get(email=email, password=password)
            request.session['email'] = email
            return redirect('board')
        except Student.DoesNotExist:
            errormessage = "Invalid Email Address or Password"
            return render(request, 'login.html', {'errormessage': errormessage})
    else:
        return render(request, 'login.html')


def board(request):
    user = request.session.get('email')
    return render(request,'board.html',{'user':user})


def application_form(request):
    user = request.session.get('email')
    i = StudentData.objects.filter(email2=user)
    return render(request,'application_form.html',{'i':i,'user':user})

def hall_ticket(request):
    roll = random.randint(10000,100000)
    center = ['ION Digital Zone IDZ \n Vishnupuri SSS Indira\n Institute of Technology Vishnupurti Gate No 18 & 22\n Nanded Maharashtra 431601\n',' ION Digital Zone IDZ\n Chikkalthana Aurangabad \n  Gate No 7 \nAurangabad Maharashtra 431601\n']
    exam = random.choice(center)
    user = request.session.get('email')
    i = StudentData.objects.filter(email2=user)
    return render(request, 'hallticket.html', {'i': i,'user':user,'roll':roll,'exam':exam})
