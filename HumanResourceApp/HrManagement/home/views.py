from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.views import View
from .models import CustomUser, Provinces, Specialization
from django.utils.encoding import force_bytes,force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib. sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib import auth
from .utils import account_activation_token
from django.contrib import messages

# Create your views here.


from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method=="POST":
        send_mail(f"From {request.POST['name']}",request.POST['message'],request.POST['email'],[settings.EMAIL_HOST_USER])
    return render(request,'home/index.html')


def loginregister(request):
    if request.method=="POST":
        if request.POST['action']=="register":
            cuser=CustomUser.objects.create_user(email=request.POST['email'],password=request.POST['password'])
            if request.POST['password'] != request.POST['password1']:
                raise Exception("Passowrds Do not match")
            else:
                cuser.is_active=False
                cuser.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': cuser,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(cuser.id)),
                    'token': account_activation_token.make_token(cuser),
                }

                link = reverse('activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})


                activate_url = 'http://'+current_site.domain+link
                send_mail("Confirm Your email",'Hi '+cuser.email + ', Please the link below to activate your account \n'+activate_url,settings.EMAIL_HOST_USER,[request.POST['email']])
                messages.success(request, 'Account successfully created')
        else:
            user=authenticate(email=request.POST['email'],password=request.POST['password'])
            login
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("No valid credentials")
    return render(request,'home/loginregister.html')


def profile(request,id):
    if int(request.user.id)==int(id):
        states=Provinces.objects.all()
        expertiese=Specialization.objects.all()
        users=CustomUser.objects.get(id=id)

        if request.method=="POST":
            users.first_name=request.POST['f_name']
            users.last_name=request.POST['l_name']
            users.email=request.POST['email']
            prov=Provinces.objects.get(id=request.POST['state'])
            users.provinces=prov
            users.address=request.POST['address']
            expert=Specialization.objects.get(id=request.POST['exp'])

            users.specialization=expert
            if request.FILES:
                users.resume=request.FILES['cv']
            users.save()
        if users.provinces is not None:
            current_state=users.provinces.id
        else:
            current_state=None
        if users.specialization is not None:
            current_specialization=users.specialization.id
        else:
            current_specialization=None

        context={'states':states,'expertiese':expertiese,'users':users,'current_state':current_state,'current_specialization':current_specialization}
        return render(request,'home/profile.html',context)
    else:
        return redirect('home')

def log_out(request):
    logout(request)
    return redirect('home')

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('loginregister'+'?message='+'User already activated')

            if user.is_active:
                return redirect('loginregister')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('loginregister')

        except Exception as ex:
            pass

        return redirect('loginregister')
