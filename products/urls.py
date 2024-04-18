from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static
from .views import create_view, update_view


app_name = 'products'


urlpatterns =[
    path("", views.list_view, name="list"),
    path("<int:product_id>", views.detail_view, name="detail"),
    path("create/", views.create_view, name="create"),
    path("update/<int:product_id>", views.update_view, name="update"),
    path("delete/<int:product_id>", views.delete_view, name="delete"),
    path("choose/<int:product_id>", views.choose_view, name='choose'),
    path('product/new/', create_view, name='product_new'),
    path('product/<int:pk>/edit/', update_view, name='product_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)