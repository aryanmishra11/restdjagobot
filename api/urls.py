
from django.urls import path
from api.views import UserView,TokenView,CodeExplainView

urlpatterns = [
    path('users/',UserView.as_view(),name='users'),
    # path('tokens/',TokenView.as_view(),name='tokens')
    path('code-explain/',CodeExplainView.as_view(),name='code-explain' )
]