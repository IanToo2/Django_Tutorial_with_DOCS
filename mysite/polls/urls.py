from django.urls import path

from . import views

# URLconf 이름공간 추가
app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.index, name= "index"),
    # name으로 url template태그로 연결
    path("<int:question_id>/", views.detail, name="detail"),
    # /polls/5/results
    path("<int:question_id>/results/", views.results, name="results"),
    # /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
]