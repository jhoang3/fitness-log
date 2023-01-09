from django.urls import path
from . import views

# these pattersn will look like .../item/...
urlpatterns = [
    path('user', views.user, name='user'),
    path('<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete')
]