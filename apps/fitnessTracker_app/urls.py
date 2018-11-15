from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^main$', views.load_profile_builder),                               # RENDERS PROFILE BUILDER PAGE
    url(r'^build_profile$', views.build_profile),                               # BUILDS PROFILE
    url(r'^dashboard$', views.load_dashboard),                                # BUILDS DASHBOARD
    url(r'^load_workout_tree$', views.load_workout_tree),                        # RENDERS WORKOUT TREE
    url(r'^load_workout_education_base$', views.load_workout_education_base),                        # RENDERS WORKOUT TREE
]