from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('profile/learning_sets/', # urls list all and create new one
        views.get_post_learning_sets.as_view(),
        name='get_post_learning_sets'
    ),
    path('profile/class_sets/', # urls list all and create new one
        views.get_post_class_sets.as_view(),
        name='get_post_class_sets'
    )
]