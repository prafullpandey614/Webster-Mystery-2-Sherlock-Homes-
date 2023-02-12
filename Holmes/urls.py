from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("home",views.index,name="home"),
    path("register",views.register,name="register"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("profile",views.profile,name="profile"),
    path("jobs",views.jobs,name="jobs"),
    path("temp-signup",views.tempsign,name="temps"),
    path("edit-profile",views.edit_profile,name="edit"),
    path("apply/<int:pk>",views.applyPage,name="apply"),
    path("status",views.status,name="status"),
    # path("register",views.register),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)