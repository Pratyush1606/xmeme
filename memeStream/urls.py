from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from memeStream import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# url patterns containing the apis used between the frontend and backend
urlpatterns = [
    # paths for getting requests memes/ or memes
    # these two are pointing to the same class but have to be implemented as it gives error while getting requests because of slash(default)
    path('memes', views.meme_list.as_view()),
    path('memes/', views.meme_list.as_view()),
    # paths pointing to the views for getting, deleting and editing memes through GET, DELETE, PATCH requests
    path('memes/<int:pk>', views.meme_detail.as_view()),
    path('memes/<int:pk>/', views.meme_detail.as_view()),
    
    # for renderring the html pages and posting memes
    path('',views.meme_list_1.as_view(), name="meme_detail"),
    path("meme_list",views.meme_list_2.as_view(), name="meme_list"),

    # for updating(editing) and deleting the memes from meme_list.html
    path("del_meme/<int:pk>/", views.delete_meme, name="delete_meme"),
    path("update_meme/<int:pk>/", views.update_meme.as_view(), name="update_meme"),
    
    # for swagger-ui view
    path('openapi/', get_schema_view(
        title="XMEME",
        description="Get the meme apis"
    ), name='openapi-schema'),
    path('swagger-ui/',TemplateView.as_view(
        template_name="documentation.html",
        extra_context={'schema_url':'openapi-schema'}
    ), name="swagger-ui"),
]