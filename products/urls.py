from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # 상품
    path("", views.index, name="index"), # 상점이 있는 메인 화면(상점 리스트)
    path("create/", views.create, name="create"), # 상품 글 작성
    path("<int:product_pk>/", views.detail, name="detail"), # 상품 조회 페이지
    path("<int:product_pk>/update/", views.update, name="update"), # 상품 글 수정
    path("<int:product_pk>/delete/", views.delete, name="delete"), # 상품 글 삭제
    path("<int:product_pk>/add_cart/", views.add_cart, name="add_cart"), # 장바구니 상품 담기
    path("show_cart/<int:user_pk>/", views.show_cart, name="show_cart"), # 장바구니 조회
    path("delete_cart/<int:product_pk>", views.show_cart, name="show_cart"), # 장바구니 상품 삭제
]
