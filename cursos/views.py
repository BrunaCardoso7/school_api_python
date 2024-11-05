from cursos.views import AvaliacaoApiView, CursoApiView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import AvaliacaoSerializer, CursoSerializer
from rest_framework.generics import get_object_or_404, generics
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

# =========== API v1 ==============

class CursosApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesApiView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()

    
class AvaliacaoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), avaliacao_pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
# =========== API v2 ==============

class CursoApiViewSet(viewsets.ViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True, methods=['get'])
    def avaliacoes (self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        
        return Response(serializer.data)
    

# class AvaliacaoApiViewSet(viewsets.ViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer
    
    # @action(detail=True, methods=['get'])
    # def avaliacao (self, request, pk=None):
    #     curso = self.get_object()
    #     serializer = AvaliacaoSerializer(curso.avaliacao.)


class AvaliacaoApiViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer