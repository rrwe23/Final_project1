from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [

    # 리뷰
    path("<int:product_pk>/review/", views.index, name="index"), # 리뷰 목록 리스트
    # path("/<int:product_pk>/review/create", views.create, name="create"), # 상품 리뷰 작성
    # path("/review/<int:review_pk>/update", views.update, name="update"), # 상품 리뷰 수정
    # path("/review/<int:review_pk>/delete", views.delete, name="delete"), # 상품 리뷰 삭제
    # path("/review/<int:review_pk>/like", views.like, name="like"), # 상품 리뷰 좋아요 


]
