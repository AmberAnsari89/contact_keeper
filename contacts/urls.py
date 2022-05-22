from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('delete/<contact_id>',views.delete,name='delete'),
    path('edit/<contact_id>', views.edit,name="edit")
]