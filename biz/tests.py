from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class HostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_host(self):
        for idc_id, city_id in {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 2,
            8: 2,
            9: 2,
            10: 2,
            11: 2,
            12: 2,
            13: 3,
            14: 3,
            15: 3,
            16: 3,
            17: 3,
            18: 3,
            19: 3,
            20: 4,
            21: 4,
            22: 4,
            23: 4,
            24: 4,
            25: 4,
            26: 4,
        }:
            for k in range(13):
                response = self.client.post(reverse('host-list'), {
                    'name': f"Host {city_id}-{idc_id}-{k}",
                    'root_password': 'initial_password',
                    'idc_id': idc_id
                })
                self.assertEqual(response.status_code, 201)
