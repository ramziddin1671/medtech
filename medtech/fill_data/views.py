from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from polls.models import (
    CategoryReagents,
    CategoryConsumables,
    CategoryService,
    Reagents,
    Consumables,
    Parts
)

from .excel import read_excel

import datetime

from django.contrib.admin.views.decorators import staff_member_required


def get_models():
    return [
        {
            'name': _("Reagent qo'shish"),
            'slug': 'add-reagent',
            'fields': ['model_uz', 'model_ru', 'title_uz', 'title_ru', 'releasedate', 'manufacturer_uz', 'manufacturer_ru', 'tests', 'supplier_uz', 'supplier_ru', 'price', 'phone']
        },
        {
            'name': _("Rasxodni material"),
            'slug': 'add-consumable',
            'fields': ['model_uz', 'model_ru', 'title_uz', 'title_ru', 'unit', 'manufacturer_uz', 'manufacturer_ru', 'organization_uz', 'organization_ru', 'price', 'phone']
        },
        {
            'name': _("Servis qo'shish"),
            'slug': 'add-part',
            'fields': ['title_uz', 'title_ru', 'unit', 'manufacturer_uz', 'manufacturer_ru',
                       'organization_uz', 'organization_ru', 'price', 'phone']
        }
    ]


def get_categories(model_name):
    if model_name == 'add-reagent':
        return CategoryReagents.objects.all()
    elif model_name == 'add-consumable':
        return CategoryConsumables.objects.all()
    elif model_name == 'add-part':
        return CategoryService.objects.all()


def get_create_model(model_name):
    if model_name == 'add-reagent':
        return Reagents
    elif model_name == 'add-consumable':
        return Consumables
    elif model_name == 'add-part':
        return Parts


@staff_member_required
def index(request):
    return render(request, 'fill_data/index.html', {
        'models': get_models(),
        'success': request.GET.get('success', False)
    })


@staff_member_required
def fill_data(request, model_slug):
    model = [model for model in get_models() if model['slug'] == model_slug][0]
    if request.method == 'GET':
        return render(request, 'fill_data/fill_data.html', {
            'categories': get_categories(model_slug),
            'model': model,
            'error': request.GET.get('error', None)}
        )

    category = request.POST.get('category')

    file = request.FILES.get('file')
    data = read_excel(file)

    return render(request, 'fill_data/fill_data.html', {
        'categories': get_categories(model_slug),
        'model': model,
        'data': data,
        'category': category,
    })


@staff_member_required
def save_data(request, model_slug):
    data = eval(request.POST.get('data'))
    category = request.POST.get('category')
    model = [field for field in get_models() if field['slug'] == model_slug][0]
    model_fields = model['fields']
    creation_model = get_create_model(model_slug)

    objects = []
    for row in data:
        kwargs = {'category_id': category}
        for index, field_name in enumerate(model_fields):
            kwargs[field_name] = row[index]
        objects.append(creation_model(**kwargs))
    last_obj = creation_model.objects.order_by('-id').first()
    try:
        creation_model.objects.bulk_create(objects)
        if last_obj is not None:
            creation_model.objects.filter(id__lte=last_obj.id).delete()
    except Exception as e:
        return redirect(f'/fill-data/{model_slug}/?error={e}')

    return redirect(reverse('fill_data_index') + '?success=true')

