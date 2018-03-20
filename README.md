# tdi_photoUploader

This solution,  made using the Django framework, features an app allowing users to upload and view a photo


[![Build Status](https://travis-ci.org/loremIpsum1771/tdi_photoUploader.svg?branch=master)](https://travis-ci.org/loremIpsum1771/tdi_photoUploader)


## Quickstart/Setup:

1. Clone the repository/ Download the .zip file
2. Open a terminal window
3. ```cd tdi_photoUploader```

4. If other versions of Django are installed on the machine, create and activte a virtualenv to isolate the package dependencies locally

   *Installation instructions [here](https://virtualenv.pypa.io/en/stable/installation/)*
```virtualenv api_env
   source api_env/bin/activate  *For mac and linux*
```
5. Install Django/Django REST framework and dependencies into the virtualenv
```
   pip install -r requirements.txt
```
6. Change into project source and runserver
```
   cd src
   python manage.py runserver
```
7. Open your browser and navigate [to this url](http://127.0.0.1:8000/)

8. Once on the page, you will see a form where you can browse for an image to upload. Once the image is selected, it will be displayed on the page.


