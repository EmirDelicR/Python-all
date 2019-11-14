from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from rest_auth.views import LogoutView, PasswordChangeView
from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

router = routers.DefaultRouter()
urlpatterns = router.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path('', views.home, name='home'),
    path('admin/login/', obtain_auth_token),
    # path('login/', views.CustomLoginView.as_view()),
    # path('registration/', views.RegistrationView.as_view()),
    path('logout/', csrf_exempt(LogoutView.as_view())),
    # path('password/set/', views.SetPasswordView.as_view()),
    path('password/change/', PasswordChangeView.as_view()),
    # path('password/reset/', views.ResetPasswordView.as_view()),
    # path('token/validation/', views.TokenValidationView.as_view()),
    # path('caterer/<str:caterer_id>', views.CatererDetails.as_view()),
    path('todo/', views.ListCreateTodoView.as_view(), name="todo-all-create"),
    path('todo/<uuid:id>', views.TodoDetailView.as_view(), name="todo-detail"),
    
    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]