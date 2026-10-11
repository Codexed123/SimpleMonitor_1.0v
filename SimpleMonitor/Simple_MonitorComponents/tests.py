from django.test import TestCase
from Simple_MonitorComponents.models import WebsiteConfigure
# Create your tests here.
class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data_tester = WebsiteConfigure.objects.create(web_name="Tester1", url="http://sample.com")
    def test_data(self):
        data1 = WebsiteConfigure.objects.get(id=self.data_tester.id)
        self.assertEqual(str(data1.url), "http://sample.com")
