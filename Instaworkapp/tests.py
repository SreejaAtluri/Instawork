import unittest

from django.test import TestCase, Client
from django.urls import reverse
from .models import Adddata

# Create your tests here.


class TestModels(TestCase):

    def setUp(self):

        Adddata.objects.create(
            firstname="Sreeja",
            lastname="Atluri",
            email="atluri1@uwindsor.ca",
            phoneNumber="+15197929790",
            role=2
        )

        Adddata.objects.create(
            firstname="Adrien",
            lastname="Olczak",
            email="adrien@instawork.com",
            phoneNumber="+14153101619",
            role=1
        )

    def test_model_str(self):
        name = Adddata.objects.create(firstname="Sreeja")
        self.assertEqual(str(name), "Sreeja")

    def test_entry(self):
        adddata = Adddata()
        adddata.firstname = "Sreeja"
        adddata.save()
        object = Adddata.objects.get(pk=adddata.id)
        self.assertEqual(adddata, object)

    def test_entry2(self):
        object = Adddata.objects.get(lastname="Olczak")
        self.assertEqual(object.firstname, "Adrien")
        self.assertEqual(object.lastname, "Olczak")

    @unittest.expectedFailure
    def test_entry_failure(self):
        object = Adddata.objects.get(firstname="Adrien")
        self.assertEqual(object.firstname, "Sreeja")



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        Adddata.objects.create(
            firstname="Sreeja",
            lastname="Atluri",
            email="atluri1@uwindsor.ca",
            phoneNumber="+15197929790",
            role=2
        )
        self.landingPageUrl = reverse('Instaworkapp:listview')
        self.addViewUrl = reverse('Instaworkapp:addview')
        self.updateUrl = reverse('Instaworkapp:updateview', args=[1])
        self.deleteUrl = reverse('Instaworkapp:deleteview', args=[1])

    def test_project_list(self):
        response = self.client.get(self.landingPageUrl)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Instaworkapp/base.html')

    def test_project_add(self):
        response = self.client.get(self.addViewUrl)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Instaworkapp/adddata_form.html')

    def test_project_update(self):
        response = self.client.get(self.updateUrl)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Instaworkapp/update.html')

    def test_project_delete(self):
        response = self.client.get(self.deleteUrl)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Instaworkapp/adddata_confirm_delete.html')