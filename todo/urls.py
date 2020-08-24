from django.urls import path
from .views import index, remove, edit


urlpatterns = [
    path('', index, name='index'),
    path('remove/<int:id>', remove, name='remove'),
    path('edit/<int:id>', edit, name='edit'),
]
