from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from sirh.basins.forms import BasinForm
from sirh.basins.models import Basin


def list(request):
    basin_list = Basin.objects.all().order_by('name')
    selection = request.GET.get('search_box')

    page = request.GET.get('page')

    if selection is not None:
        basin_list = Basin.objects.filter(name__icontains=selection)

    paginator = Paginator(basin_list, 10)

    try:
        page_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)

    return render(request, 'basins/basin_listing.html', {'page_objects': page_objects})


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
