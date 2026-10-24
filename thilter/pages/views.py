from django.shortcuts import render
from .models import Watch, PageBanner
from .forms import FilterForm, SearchForm


# Create your views here.
def index(request):
    banners = PageBanner.index_page()
    return render(request, 'pages/index.html', {'banners': banners})


def watches(request):
    filters = request.session.get('filters', {})
    search_text = request.session.get('search_text')

    filter_form = FilterForm(request.POST or None, initial=filters)
    search_form = SearchForm(request.POST or None, initial={'text': search_text})

    if 'filter_form' in request.POST and filter_form.is_valid() and filter_form.has_changed():
        filters = filter_form.cleaned_data
        request.session.update({'filters': filters})

    if 'search_form' in request.POST and search_form.is_valid() and search_form.has_changed():
        search_text = search_form.cleaned_data['text']
        request.session.update({'search_text': search_text})

    watches_list = Watch.apply_filters(filters, search_text)

    context = {
        'watches': watches_list,
        'colours': watches_list.values_list('colour__url_key', 'colour__name').distinct().exclude(colour__name=None),
        'brands': watches_list.values_list('brand__url_key', 'brand__name').distinct().exclude(brand__name=None),
        'deliveries': watches_list.values_list('delivery', flat=True).distinct().exclude(delivery=None),
        'functions': [],
        'filters': filters
    }
    return render(request, 'pages/product_page.html', context)
