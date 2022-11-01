from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [

    # 상품
    path("", views.index, name="index"), # 상점이 있는 메인 화면
    path("<int:user_pk>", views.index, name="index"), # 상품 리스트
    path("<int:user_pk>/create/", views.create, name="create"), # 상품 글 작성
    path("<int:user_pk>/<int:product_pk>/", views.detail, name="detail"), # 상품 조회 페이지
    path("<int:user_pk>/<int:product_pk>/update/", views.update, name="update"), # 상품 글 수정
    path("<int:user_pk>/<int:product_pk>/delete/", views.delete, name="delete"), # 상품 글 삭제
    path("<int:user_pk>/<int:product_pk>/cart/", views.cart, name="cart"), # 장바구니 담기

    # 리뷰
    path("<int:user_pk>/<int:product_pk>/review/", views.review_index, name="review_index"), # 리뷰 목록 리스트
    path("<int:user_pk>/<int:product_pk>/review/create", views.review_create, name="review_create"), # 상품 리뷰 작성
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/update", views.review_update, name="review_update"), # 상품 리뷰 수정
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/delete", views.review_delete, name="review_delete"), # 상품 리뷰 삭제
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/like", views.like, name="like"), # 상품 리뷰 좋아요 

    # Q&A
    path("<int:user_pk>/<int:product_pk>/qna/", views.qna_index, name="qna_index"), # qna 리스트
    path("<int:user_pk>/<int:product_pk>/qna/create/question", views.question_create, name="question_create"), # 상품 문의 작성
    path("<int:user_pk>/<int:product_pk>/qna/create/answer", views.answer_create, name="answer_create"), # 상품 답변 작성
    path("<int:user_pk>/<int:product_pk>/qna/<int:qna_pk>/update", views.qna_update, name="qna_update"), # 상품 문의 수정
    path("<int:user_pk>/<int:product_pk>/qna/<int:qna_pk>/delete", views.qna_delete, name="qna_delete"), # 상품 문의 삭제
]
