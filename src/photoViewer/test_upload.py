# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client
import unittest

class FileUploadTestClass(unittest.TestCase):

    def test_uploaded_file(self):
        c = Client()
        originalFilePath = '../static_cdn/Keep-Calm-and-Carry-On.jpg'
        #image_data = open(originalFilePath, "rb")
        with open(originalFilePath, "rb") as fp:
            response = c.post('/', {'image': fp})
            fp.seek(0)
            self.assertEqual( fp.read(),response.content)

