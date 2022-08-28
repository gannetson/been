from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from users.views import UserDetailApiView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('users/',  include('users.urls')),
    path('', RedirectView.as_view(url='/users/loek')),
    path('api/user/<username>', UserDetailApiView.as_view(), name='api-user')
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)