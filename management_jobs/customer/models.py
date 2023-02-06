from django.db import models
from django.db.models import signals
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField("Cliente", max_length=200)
    dtt_record = models.DateTimeField("Data de Inserção", auto_now_add=True, blank=True)
    email = models.EmailField("E-mail", max_length=50)
    phone = models.CharField("Telefone", max_length=15)
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True,
                            help_text='Adicione uma slug com palavras separadas por hifens para ou deixe em branco para preenchimento automático.')
    active = models.BooleanField("Ativo", default=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer:customer', args=[self.slug])


class Job(models.Model):
    name = models.CharField("Serviço", max_length=200)
    price = models.DecimalField("Valor Cobrado", max_digits=10, decimal_places=2)
    slug = models.SlugField('Slug', max_length=200, unique=True, blank=True,
                            help_text='Adicione uma slug com palavras separadas por hifens para ou deixe em branco para preenchimento automático.')
    dtt_record = models.DateTimeField("Data de Inserção", auto_now_add=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job:job', args=[self.slug])


class CustomerJob(models.Model):
    customer = models.ForeignKey(Customer, related_name="customer_job", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='job_type', on_delete=models.PROTECT)
    recurrent = models.BooleanField("Recorrente")
    dtt_start = models.DateField("Data de Inicio")
    dtt_end = models.DateField("Data de Termino")
    dtt_record = models.DateTimeField("Data de Inserção", auto_now_add=True, blank=True)

    objects = models.Manager()


from libs.signals import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Customer)
signals.pre_save.connect(slug_pre_save, sender=Job)
