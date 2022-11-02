from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [

    # 리뷰
    path("<int:user_pk>/<int:product_pk>/review/", views.review_index, name="review_index"), # 리뷰 목록 리스트
    path("<int:user_pk>/<int:product_pk>/review/create", views.review_create, name="review_create"), # 상품 리뷰 작성
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/update", views.review_update, name="review_update"), # 상품 리뷰 수정
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/delete", views.review_delete, name="review_delete"), # 상품 리뷰 삭제
    path("<int:user_pk>/<int:product_pk>/review/<int:review_pk>/like", views.like, name="like"), # 상품 리뷰 좋아요 


]
