from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_data, name = "display_data"),
    path('scrape/', views.run_scraper, name = 'run_scraper')
]
