from django.urls import include, path

urlpatterns = [
    path(r'', include('frontend.urls')),
    path(r'api/v1/', include('backend.urls')),
]
