from django.urls import reverse_lazy
from django.views import generic

from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import SignupForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})