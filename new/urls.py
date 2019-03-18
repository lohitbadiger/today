from django.urls import path
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views 

urlpatterns = [

    # path('', views.home, name="new-home"),
    path('', PostListView.as_view(), name="new-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    
    path('about', views.about, name="new-about"),
    path('contact', views.contact, name="new-contact"),

]
