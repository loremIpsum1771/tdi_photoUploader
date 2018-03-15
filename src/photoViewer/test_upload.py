# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

class FileUploadTestClass(TestCase):

    def test_uploaded_file(self):
        c = Client()
        originalFilePath = '../static_cdn/Keep-Calm-and-Carry-On.jpg'
        image_data = open(originalFilePath, "rb")
        with open(originalFilePath, "rb") as fp:
            response = c.post('/', {'image': fp})
            self.assertEqual(image_data,response)

