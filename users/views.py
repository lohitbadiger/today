from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # form=UserCreationForm()
    # return render(request, 'users/register.html', {'form':form})
    if request.method=='POST':

        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account creatd For {username}! Now you can Login ')
            return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
