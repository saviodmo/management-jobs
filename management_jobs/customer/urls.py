from django.urls import path, re_path
from customer import views

app_name = 'customer'

urlpatterns = [
    re_path('customer/edit-job/(?P<slug>[\w_-]+)/?$', views.edit_job, name='edit_job'),
    path('customer/add-job', views.add_job, name='add_job'),
    path('customer/add-customer', views.add_customer, name='add_customer'),
    re_path('customer/edit-customer/(?P<slug>[\w_-]+)/?$', views.edit_customer, name='edit_customer'),
    re_path('^customer/(?P<slug>[\w_-]+)/?$', views.customer_job, name='customer'),  # essa é pra listar os dados sem editar
    path('job', views.job_list, name='job'),
    path('customer-list', views.customer_list, name='customer_list'),
    path('', views.index, name='index')
]