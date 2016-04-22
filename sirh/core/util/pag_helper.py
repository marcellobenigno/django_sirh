from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def my_pagination(list_name, page_name):
    paginator = Paginator(list_name, 10)

    try:
        page_objects = paginator.page(page_name)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)

    return page_objects



def my_range(page_objects):
    # Get the index of the current page
    index = page_objects.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(page_objects.paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = page_objects.paginator.page_range[start_index:end_index]

    return page_range


