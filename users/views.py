from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')

    form = NewUserForm()
    context={
        'form':form,
    }
    return render(request,'users/register.html',context)
@login_required
def profile(request):
    return render(request,'users/profile.html')

def create_profile(request):
    if request.method =='POST'and request.FILES.get('upload'):
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user,image=image,contact_number=contact_number)
        profile.save()
    return render(request,'users/createprofile.html')

def seller_profile(request,id):
    seller = User.objects.get(id=id)
    context ={
        'seller':seller,
    }
    return render(request, 'users/sellerprofile.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/profile.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'users/contact.html', context)
