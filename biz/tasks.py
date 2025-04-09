from django.db.utils import IntegrityError
from django.db.models import Count
from celery import shared_task
from django.utils.crypto import get_random_string
from .models import Host, PasswordHistory, HostStatistic


@shared_task
def change_passwords():
    for host in Host.objects.all():
        old_password = host.root_password
        new_password = get_random_string(16)
        host.root_password = new_password
        try:
            host.save(update_fields=['root_password'])
            PasswordHistory.objects.create(host=host, password=old_password)
        except IntegrityError:
            # todo
            pass


@shared_task
def generate_statistics():
    stats = Host.objects.values('city_id', 'idc_id').annotate(count=Count('id'))
    for stat in stats:
        HostStatistic.objects.create(
            city_id=stat['city_id'],
            idc_id=stat['idc_id'],
            count=stat['count'])

