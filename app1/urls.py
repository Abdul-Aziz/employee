from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.employee_list,name='employee_list'),
    path('employee_detail/<int:id>',views.employee_detail,name='employee_detail')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
