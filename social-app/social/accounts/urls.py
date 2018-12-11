from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    
    #path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    #path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    #path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    #path('post/<int:pk>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    #path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    #path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    #path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    #path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    #path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
]