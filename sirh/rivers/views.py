from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from sirh.rivers.forms import RiverForm
from sirh.rivers.models import River


def list(request):
    rivers_list = River.objects.all().order_by('name')
    selection = request.GET.get('search_box')

    page = request.GET.get('page')

    if selection is not None:
        rivers_list = River.objects.filter(name__icontains=selection)

    paginator = Paginator(rivers_list, 10)

    try:
        page_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)

    return render(request, 'rivers/river_listing.html', {'page_objects': page_objects})


def detail(request, pk):
    river = get_object_or_404(River, pk=pk)
    return render(request, 'rivers/river_detail.html', {'river': river})


def create(request):
    title = "Cadastrar Rio"
    form = RiverForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Rio cadastrada com sucesso!')
        return redirect('rivers:list')

    return render(request, 'rivers/river_form.html', {'title': title, 'form': form})

def edit(request, pk):
    title = "Editar Rio"
    river = get_object_or_404(River, pk=pk)
    form = RiverForm(request.POST or None, instance=river)
    if form.is_valid():
        form.save()
        messages.success(request, 'Rio editado com sucesso!')
        return redirect('rivers:list')

    return render(request, 'rivers/river_form.html', {'title': title, 'form': form})


def delete(request, pk):
    basin = get_object_or_404(River, pk=pk)
    if request.method == 'POST':
        basin.delete()
        messages.success(request, 'Rio deletado com sucesso!')
        return redirect('rivers:list')

    return render(request, 'basins/basin_delete.html', {'basin': basin})
