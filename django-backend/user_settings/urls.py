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
    ),
    path('profile/mail_lists/', # urls list all and create new one
        views.get_post_mail_lists.as_view(),
        name='get_post_mail_lists'
    ),
    path('profile/sys_mail_lists/', # urls list all and create new one
        views._sys_get_mail_lists.as_view(),
        name='_sys_get_mail_lists'
    )
]
