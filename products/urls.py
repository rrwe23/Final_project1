from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [

    # 상품

    path("", views.main, name="main"), # 상점이 있는 메인 화면
    path("<int:user_pk>", views.index, name="index"), # 상품 리스트
    path("<int:user_pk>/create/", views.create, name="create"), # 상품 글 작성
    path("<int:user_pk>/<int:product_pk>/", views.detail, name="detail"), # 상품 조회 페이지
    path("<int:user_pk>/<int:product_pk>/update/", views.update, name="update"), # 상품 글 수정
    path("<int:user_pk>/<int:product_pk>/delete/", views.delete, name="delete"), # 상품 글 삭제
    path("<int:user_pk>/<int:product_pk>/cart/", views.cart, name="cart"), # 장바구니 담기
   
]
