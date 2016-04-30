from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    template_name = 'accounts/register.html'
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(settings.LOGIN_URL)

    return render(request, template_name, {'form': form})
