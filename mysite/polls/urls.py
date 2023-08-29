from django.urls import path

from . import views

# URLconf 이름공간 추가
app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name= "index"),
    # name으로 url template태그로 연결
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/5/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]