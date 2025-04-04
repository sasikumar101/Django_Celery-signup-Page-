from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set hashed password
            user.save()
            login(request, user)
            messages.success(request, f"Signup successful! Welcome, {user.username} 🎉")
            return redirect("home")
        else:
            messages.error(request, "Signup failed! Please check the form and try again.")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {"form": form})

# ✅ Only allow logged-in users to access home
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "home.html")
