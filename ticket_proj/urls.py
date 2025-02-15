from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/', include('ticket_app.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
