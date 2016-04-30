from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from sirh.core.util.pag_helper import my_pagination, my_range
from sirh.rivers.forms import RiverForm
from sirh.rivers.models import River


def list(request):
    rivers_list = River.objects.all().order_by('name')
    selection = request.GET.get('search_box') or None
    result = None
    page = request.GET.get('page')

    if selection is not None:
        rivers_list = River.objects.filter(name__icontains=selection)
        result = rivers_list.count()

    page_objects = my_pagination(rivers_list, page)

    page_range = my_range(page_objects)

    context = {
        'page_objects': page_objects,
        'page_range': page_range,
        'result': result,
        'selection': selection
    }

    return render(request, 'rivers/river_listing.html', context)


def detail(request, pk):
    river = get_object_or_404(River, pk=pk)
    return render(request, 'rivers/river_detail.html', {'river': river})


@login_required
def create(request):
    title = "Cadastrar Rio"
    form = RiverForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Rio cadastrado com sucesso!')
        return redirect('rivers:list')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'rivers/river_form.html', context)


@login_required
def edit(request, pk):
    title = "Editar Rio"
    river = get_object_or_404(River, pk=pk)
    form = RiverForm(request.POST or None, instance=river)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Rio editado com sucesso!')
        return redirect('rivers:list')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'rivers/river_form.html', context)


@login_required
def delete(request, pk):
    river = get_object_or_404(River, pk=pk)

    if request.method == 'POST':
        river.delete()
        messages.success(request,
                         'Rio deletado com sucesso!')
        return redirect('rivers:list')

    return render(request, 'rivers/river_delete.html', {'river': river})
