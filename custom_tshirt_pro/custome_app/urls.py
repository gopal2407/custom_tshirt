from django.urls import path
from .views import LoginView, AdminView, CustomerView, OwnerView, LogoutView
from .views import SizeView, ColorView, CategoryView, SubcategoryView, CouponView, FontView
from .views import AddItemView, BuyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view_url'),
    path('home-admin/', AdminView.as_view(), name='admin_view_url'),
    path('home-customer/', CustomerView.as_view(), name='customer_view_url'),
    path('home-owner/', OwnerView.as_view(), name='owner_view_url'),
    path('logout/', LogoutView.as_view(), name='logout_view_url'),
    # Admin functionality url
    # size
    path('size/', SizeView.as_view(), name='size_view_url'),
    path('size/<int:pk>/', SizeView.as_view(), name='size_view_edit_url'),
    path('size/<int:pk>/delete/', SizeView.as_view(), name='size_view_delete_url'),
    # color
    path('color/', ColorView.as_view(), name='color_view_url'),
    path('color/<int:pk>/', ColorView.as_view(), name='color_view_edit_url'),
    path('color/<int:pk>/delete/', ColorView.as_view(), name='color_view_delete_url'),
    # category
    path('category/', CategoryView.as_view(), name='category_view_url'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_view_edit_url'),
    path('category/<int:pk>/delete/', CategoryView.as_view(), name='category_view_delete_url'),
    # subcategory
    path('subcategory/', SubcategoryView.as_view(), name='subcategory_view_url'),
    path('subcategory/<int:pk>/', SubcategoryView.as_view(), name='subcategory_view_edit_url'),
    path('subcategory/<int:pk>/delete/', SubcategoryView.as_view(), name='subcategory_view_delete_url'),

    # coupon
    path('coupon/', CouponView.as_view(), name='coupon_view_url'),
    path('coupon/<int:pk>/', CouponView.as_view(), name='coupon_view_edit_url'),
    path('coupon/<int:pk>/delete/', CouponView.as_view(), name='coupon_view_delete_url'),
    # font
    path('font/', FontView.as_view(), name='font_view_url'),
    path('font/<int:pk>/', FontView.as_view(), name='font_view_edit_url'),
    path('font/<int:pk>/delete/', FontView.as_view(), name='font_view_delete_url'),
    # Admin functionality url ended


    # Owner Functionality url
    path('add_item/', AddItemView.as_view(), name='add_item_url'),
    path('add_item/<int:pk>/', AddItemView.as_view(), name='item_view_edit_url'),
    path('add_item/<int:pk>/delete/', AddItemView.as_view(), name='item_view_delete_url'),

    # customer functionality url
    path('cust_home/', CustomerView.as_view(), name='cust_home_url'),
    path('buy/<int:item_id>/', BuyView.as_view(), name='buy_url')

]
