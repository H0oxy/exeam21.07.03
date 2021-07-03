from django.urls import path, include
import mainapp.views as mainapp
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('about_us/', mainapp.about_us, name='about_us'),
    path('login/', mainapp.login, name='login'),
]