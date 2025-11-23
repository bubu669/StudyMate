from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.user_type == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('teacher_dashboard')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


from django.contrib.auth import authenticate, login

def login_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.user_type == "student":
                return redirect("student_dashboard")
            else:
                return redirect("teacher_dashboard")
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})





