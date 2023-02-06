from django.urls import path, re_path
from customer import views

app_name = 'customer'

urlpatterns = [
    re_path('^customer/(?P<slug>[\w_-]+)/?$', views.customer_job, name='customer'),  # essa é pra listar os dados sem editar
    path('customer-list', views.customer_list, name='customer_list'),
    path('', views.index, name='index')
]