
from django.urls import path
from . import views




app_name='shopapp1'


urlpatterns = [
    path('',views.apcategory,name='apcategory'),
    path('<slug:c_slug>/',views.apcategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodcatdetail')

    ]
