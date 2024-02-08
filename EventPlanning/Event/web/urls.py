from django.urls import path
from web.views import profile_view, RegisterView, add_event_view, event_view

app_name = "web"

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    path('add/', add_event_view, name="add"),
    path('add/<title>/', add_event_view, name='add1'),
    path('event/<title>/', event_view, name='event'),
    path('add/<title>/<name>', add_event_view, name='add2'),
]
