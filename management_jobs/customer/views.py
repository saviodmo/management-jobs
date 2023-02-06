from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from .models import Customer, Job


def index(request):
    context = {}
    template_name = 'customer/index.html'
    return render(request, template_name, context)


def customer_list(request):
    context = {}
    template_name = 'customer/customer_list.html'
    context['customer_list'] = Customer.objects.annotate(qt_customer=Count('customer_job')).filter(qt_customer__gt=0)
    return render(request, template_name, context)


def customer_job(request, slug):
    context = {}
    customer = get_object_or_404(Customer, slug=slug)

    # Função filter, filtra os elementos de acordo com o campo que eu informar
    # joblist = customer.customer_job.filter(active=True).order_by('dtt_record', 'customer')
    joblist = customer.customer_job.order_by('dtt_record', 'customer')

    context['customer_jobs'] = joblist
    context['customer'] = customer
    template_name = 'customer/customer_job.html'

    return render(request, template_name, context)
