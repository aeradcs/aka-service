from django.urls import path
from .views import *

urlpatterns = [
    path('jobs/<str:job_id>/', JobView.as_view()),  # get

    path('jobs/<str:job_id>/vars/', VarsView.as_view()),  # get
    path('jobs/<str:job_id>/vars/', VarsView.as_view()),  # post
    path('jobs/<str:job_id>/vars/', VarsView.as_view()),  # delete

    path('jobs/<str:job_id>/vars/<str:var_name>/', VarView.as_view()),  # get
    path('jobs/<str:job_id>/vars/<str:var_name>/', VarView.as_view()),  # delete

    path('jobs/', JobsView.as_view()),  # post

    path('jobs/<str:job_id>/operations/', OperationsView.as_view()),  # post

    path('paths/', PathsView.as_view()),  # get
]
