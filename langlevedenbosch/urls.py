from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

def error404(request):
    return render(request, '404.html', {})
def error500(request):
    return render(request, '500.html', {})

admin.site.site_header = settings.PROJECT_NAME.capitalize()
admin.site.site_title = settings.PROJECT_NAME.capitalize()
urlpatterns = staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', RedirectView.as_view(url='/accounts/login/')),
    path('logout/', RedirectView.as_view(url='/accounts/logout/')),
    path('404/', error404),
    path('500/', error500),
    path('', include('cms.urls', namespace='cms')),
]
