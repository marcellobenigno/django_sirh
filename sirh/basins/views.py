from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from sirh.basins.forms import BasinForm
from sirh.basins.models import Basin
from sirh.core.util.pag_helper import my_pagination, my_range


def list(request):
    basin_list = Basin.objects.all().order_by('name')
    selection = request.GET.get('search_box') or None
    result = None
    page = request.GET.get('page')

    if selection is not None:
        basin_list = Basin.objects.filter(name__icontains=selection)
        result = basin_list.count()

    page_objects = my_pagination(basin_list, page)

    page_range = my_range(page_objects)

    context = {
        'page_objects': page_objects,
        'page_range': page_range,
        'result': result,
        'selection': selection
    }

    return render(request, 'basins/basin_listing.html', context)


def detail(request, pk):
    basin = get_object_or_404(Basin, pk=pk)
    return render(request, 'basins/basin_detail.html', {'basin': basin})


@login_required
def create(request):
    title = "Cadastrar Bacia Hidrográfica"
    form = BasinForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Bacia higrográfica cadastrada com sucesso!')
        return redirect('basins:list')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'basins/basin_form.html', context)


@login_required
def edit(request, pk):
    title = "Editar Bacia Hidrográfica"
    basin = get_object_or_404(Basin, pk=pk)
    form = BasinForm(request.POST or None, instance=basin)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Bacia higrográfica editada com sucesso!')
        return redirect('basins:list')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'basins/basin_form.html', context)


@login_required
def delete(request, pk):
    basin = get_object_or_404(Basin, pk=pk)

    if request.method == 'POST':
        basin.delete()
        messages.success(request,
                         'Bacia higrográfica deletada com sucesso!')
        return redirect('basins:list')

    return render(request, 'basins/basin_delete.html', {'basin': basin})
