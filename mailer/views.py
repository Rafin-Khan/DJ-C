from django.shortcuts import render
from django.db.models import Count
# Create your views here.
from django.views.generic import ListView
from mailer.models import Company


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

    def get_queryset(self):
        return super().get_queryset().prefetch_related('contacts__orders').annotate( num_orders=Count('orders') ).order_by('-id')