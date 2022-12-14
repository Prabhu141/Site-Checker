from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('csvform/', views.csv_upload, name='csv_upload'),
    path('csv/', views.csvs, name='csvs'),
    path('csv/<int:id>/',views.delete_document,name='delete_document'),
    path('sitemapurl/', views.sitemap_upload, name='sitemap_upload'),
    path('sitemapxml/', views.sitemap, name='sitemap'),
]