from django.urls import path
from .views import CursosApiView, CursoApiView, AvaliacoesApiView, AvaliacaoApiView, AvaliacaoApiViewSet, CursoApiViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoApiViewSet)
router.register('avaliacoes', AvaliacaoApiViewSet)

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('cursos/<int:curso_pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesApiView.as_view(), name='curso_avalicoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacoesApiView.as_view(), name='curso_avalicoes'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name='avaliacao')
]