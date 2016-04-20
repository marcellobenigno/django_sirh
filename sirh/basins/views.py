from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from sirh.basins.forms import BasinForm
from sirh.basins.models import Basin


def list(request):
    basins = Basin.objects.all().order_by('name')
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        basins = Basin.objects.filter(name__icontains=var_get_search)

    return render(request, 'basins/basin_listing.html', {'basins': basins})


def detail(request, pk):
    basin = get_object_or_404(Basin, pk=pk)
    return render(request, 'basins/basin_detail.html', {'basin': basin})


def create(request):
    title = "Cadastrar Bacia Hidrográfica"
    form = BasinForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Bacia higrográfica cadastrada com sucesso!')
        return redirect('basins:list')

    return render(request, 'basins/basin_form.html', {'title': title, 'form': form})


def edit(request, pk):
    title = "Editar Bacia Hidrográfica"
    basin = get_object_or_404(Basin, pk=pk)
    form = BasinForm(request.POST or None, instance=basin)
    if form.is_valid():
        form.save()
        messages.success(request, 'Bacia higrográfica editada com sucesso!')
        return redirect('basins:list')

    return render(request, 'basins/basin_form.html', {'title': title, 'form': form})


def delete(request, pk):
    basin = get_object_or_404(Basin, pk=pk)
    if request.method == 'POST':
        basin.delete()
        messages.success(request, 'Bacia higrográfica deletada com sucesso!')
        return redirect('basins:list')

    return render(request, 'basins/basin_delete.html', {'basin': basin})