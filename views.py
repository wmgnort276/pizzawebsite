import django
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully!")
            return redirect('home:index1')
    else:
        form = RegisterForm()
    return render(request, "profiles/register.html", {"form": form})