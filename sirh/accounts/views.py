from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def register(request):
    template_name = 'accounts/register.html'
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(settings.LOGIN_URL)

    return render(request, template_name, {'form': form})
