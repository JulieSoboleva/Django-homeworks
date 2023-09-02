from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort', '')
    phones = Phone.objects.all()

    if sort_param == 'max_price':
        context = {'phones': phones.order_by('-price')}
        return render(request, template, context)
    elif sort_param == 'min_price':
        context = {'phones': phones.order_by('price')}
        return render(request, template, context)
    elif sort_param == 'name':
        context = {'phones': phones.order_by('name')}
        return render(request, template, context)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
