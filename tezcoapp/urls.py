from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('about',views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path('project',views.project, name = 'project'),
    path('service',views.service, name = 'service'),
    path('team',views.team, name = 'team'),
    path('testimonials',views.testimonials, name = 'testimonials'),
    path('faq',views.faq, name = 'faq'),
    path('features',views.features, name = 'features'),
    path('subscribe',views.subscribe, name = 'subscribe'),
    # path('404',views.error, name = '404'),
    path('annotdetail',views.Annotdetail, name = 'annotdetail'),
    path('webdetail',views.webdetail, name = 'webdetail'),
    path('erpdetail',views.erpdetail, name = 'erpdetail'),
    path('mldetail',views.mldetail, name = 'mldetail'),
    path('login',views.LoginPage, name = 'login'),
    path('careers',views.Career, name = 'careers'),
    path('gallery',views.Gallery, name = 'gallery'),
    path('login',views.LoginPage, name = 'login'),










]

