from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [

    # Q&A
    # path("<int:user_pk>/<int:product_pk>/qna/", views.qna_index, name="qna_index"), # qna 리스트
    # path("<int:user_pk>/<int:product_pk>/qna/create/question", views.question_create, name="question_create"), # 상품 문의 작성
    # path("<int:user_pk>/<int:product_pk>/qna/create/answer", views.answer_create, name="answer_create"), # 상품 답변 작성
    # path("<int:user_pk>/<int:product_pk>/qna/<int:qna_pk>/update", views.qna_update, name="qna_update"), # 상품 문의 수정
    # path("<int:user_pk>/<int:product_pk>/qna/<int:qna_pk>/delete", views.qna_delete, name="qna_delete"), # 상품 문의 삭제
]
