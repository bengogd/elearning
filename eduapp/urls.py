from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.course_view, name='courses'),
    path('single-course/', views.single_course_view, name='single-course'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)