from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('profile/learning_sets/', 
        views.get_post_learning_sets.as_view(),
        name='get_post_learning_sets'
    ),
    path('profile/class_sets/', 
        views.get_post_class_sets.as_view(),
        name='get_post_class_sets'
    ),
    path('profile/mail_lists/', 
        views.get_post_mail_lists.as_view(),
        name='get_post_mail_lists'
    ),
    path('profile/last_learn/', 
        views.get_last_learn.as_view(),
        name='get_last_learn'
    ),


    
    path('profile/sys_mail_lists/', 
        views._sys_get_mail_lists.as_view(),
        name='_sys_get_mail_lists'
    ),
    path('profile/sys_last_learn/', 
        views.post_last_learn.as_view(),
        name='post_last_learn'
    ),

]
