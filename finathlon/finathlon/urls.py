from django.urls import include, path

urlpatterns = [
    # Другие маршруты вашего проекта
    path('api/', include('registration.urls')),
]