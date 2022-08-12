from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_dashboard, name='dashboard_view'),
    path('orders/', views.manage_orders, name='manage_orders'),
    path('blog/', views.manage_blog, name='manage_blog'),
    path('products/', views.manage_products, name='manage_products'),
    path('customrequests/', views.manage_requests, name='manage_requests'),
    path('order_details/<order_number>', views.order_details, name='order_details'),
    path('orders/markshipped/<id>', views.mark_order_shipped, name='mark_order_shipped'),
    # path('products/', views.BlogCategoryList.as_view(), name='manage_products'),
    # path('blog/', views.BlogCategoryList.as_view(), name='manage_blog'),
    # path('requests/', views.BlogCategoryList.as_view(), name='manage_requests'),
]