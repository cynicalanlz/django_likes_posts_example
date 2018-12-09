from django.contrib.auth import login, authenticate
from core.forms import UserCreateForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('front')
    else:
        form = UserCreateForm()
    return render(request, 'core/login.html', {'form': form})


def front(request):
    return render(request, 'core/front.html')