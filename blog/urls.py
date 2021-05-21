from django.urls import path
from .views import BlogList,BlogLogin,RegisterView,BlogDetail,BlogCreate,BlogDelete,BlogUpdate
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',BlogList.as_view(),name = 'blogs'),
    path('login/',BlogLogin.as_view(),name = 'login'),
    path('blog-detail/<int:pk>/',BlogDetail.as_view(),name='blog'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('blog-create/',BlogCreate.as_view(),name = 'blog-create'),
    path('blog-delete/<int:pk>/',BlogDelete.as_view(),name = 'blog-delete'),
    path('blog-update/<int:pk>/',BlogUpdate.as_view(),name = 'blog-update'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name = 'logout')

]