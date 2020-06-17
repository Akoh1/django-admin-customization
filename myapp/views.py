from django.shortcuts import render, redirect, get_object_or_404
from .forms import TestUserform
from .models import TestUser
from django.contrib import messages
import datetime
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin_home(request):
    one_day = datetime.datetime.now() - datetime.timedelta(days=1)
    one_week = datetime.datetime.now() - datetime.timedelta(days=7)
    past_month = datetime.datetime.now() - datetime.timedelta(days=31)

    user_one_day = TestUser.objects.filter(date_created__gte=one_day).count()
    user_week = TestUser.objects.filter(date_created__gte=one_week).count()
    user_month = TestUser.objects.filter(date_created__gte=past_month).count()
    num_of_males = TestUser.objects.filter(gender='M').count()
    num_of_female = TestUser.objects.filter(gender='F').count()
    
    users = TestUser.objects.all()
    context = {'users': users,
               'user_one_day': user_one_day,
               'user_week': user_week,
               'user_month': user_month,
               'num_of_males': num_of_males,
               'num_of_female':num_of_female}
    return render(request, 'admin_home.html', context)

def add_user(request):
    if request.method == 'POST':
        form = TestUserform(request.POST)
        if form.is_valid():

            user = form.save()
            # user.is_active = False
            user.save()
            messages.success(request, "You successfully added a user")
            return redirect('myapp:home')
    else:
        form = TestUserform()
    return render(request, 'admin_adduser.html', {'form':form})

def delete_user(request, pk):
    # users = get_object_or_404(Users, pk=pk)
    user = get_object_or_404(TestUser, pk=pk)
    if request.method=='POST':
        # users.delete()
        user.delete()
        messages.success(request, ('User was successfully deleted!'))
        return redirect('myapp:home')

    con = { 'user':user}
    return render(request, 'admin_deleteuser.html', con)

@login_required
def change_status(request, id):
    obj= get_object_or_404(TestUser, id=id)
    print(obj)
    print("Change status")  
    # form = TestUserform(request.POST or None, instance= obj)
    # context= {'form': form}
    # if obj.exists():
    if obj.status == 'inactive':
        obj.status = 'active'
        obj.save()
        messages.success(request, "The user has been activated")
        return redirect('myapp:home')
    else:
        obj.status = 'inactive'
        obj.save()
        messages.success(request, "The user has been set to inactive")
        return redirect('myapp:home')


def send_email(request):
    users = TestUser.objects.all()
    emails = [email.email for email in users]

    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.EMAIL_HOST_USER
        # from_email = request.POST.get('from_email', '')
        
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, emails)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "You successfully sent an email to all users")
            return redirect('myapp:home')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'send_mail.html')
