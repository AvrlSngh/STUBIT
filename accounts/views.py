from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView

from .forms import SignUpForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)

            if user.is_teacher:
                if user.is_teacher:
                    return redirect('teachers:teacher_dashboard')
                elif 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('teachers:teacher_dashboard')

            # elif 'next' in request.POST:
            #     return redirect(request.POST.get('next'))

            else:
                return redirect('students:student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_view.html', {'form':form})


class signup_view(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup_view.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:student_dashboard')

def profile(request):
    return render(request, 'accounts/profile.html', {'user':request.user})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
