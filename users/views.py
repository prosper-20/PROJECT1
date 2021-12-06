from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# EMAIL IMPORTS
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from blog.models import Post
from sendgrid.helpers.mail import SandBoxMode, MailSettings


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account has been created successfully! Kindly login below")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/main_register.html", {"form": form})


def register1(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            mydict = {'username': username}
            user.save()
            mail_settings = MailSettings()
            mail_settings.sandbox_mode = SandBoxMode(False)
            html_template = 'blog/index.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome!!!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            # YOU CHANGED IT FROM EmailMessage to send_mail
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.mail = mail_settings
            new_mail = message.send()
            # print(new_mail)
            messages.success(request, f'Account created for {username}! You can sign in below')
            return redirect("login")

    else:
        # return render(request, 'users/register2.html')
        return render(request, 'users/index.html')
        # U were using register2.html



@login_required
def profile(request):
    if request.method =="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/profile.html", context)


def send_me_mail(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']

        email_from = email
        recipient_list = ['edwardprosper001@gmail.com']
        message = EmailMessage(subject, message, email_from, recipient_list)
        message.send()
        return redirect('login')
    else:
        return render(request, 'blog/new_about.html')





