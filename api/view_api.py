from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users, UsersManager, Conta
from .serializers import ApiSerializer, AccountSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class UserListViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = ApiSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    
    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example"] = 'this is in context now'
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()

        user = self.request.query_params.get('id', '')

        if user != '' and user.isnumeric():
            qs = qs.filter(category_id=user)

        return qs

    def get_object(self):
        pk = self.kwargs.get('pk', '')

        obj = get_object_or_404(
            self.get_queryset(),
            pk=pk,
        )
        return obj

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        ) 
    
    def partial_update(self, request, *args, **kwargs):
        users = self.get_object()
        serializer = ApiSerializer(
            instance=users,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )
    
    
    
    
"""@api_view(http_method_names=['get', 'post'])
def api_list(request):
        if request.method == 'GET':
            api = Users.objects.all()
            serializer = ApiSerializer(
                instance=api,
                many=True,
                context={'request':request}
            )
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = ApiSerializer(
                data=request.data,
                context={'request': request},
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
   """
            

@api_view()
def conta_api_detail(request, pk):
    conta = get_object_or_404(
        Conta.objects.all(),
        pk=pk
    )
    serializer = AccountSerializer(
        instance=conta,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)


@api_view(http_method_names=['GET', 'POST'])
def conta_api(request):
    if request.method == 'GET':
        conta = Conta.objects.all()
        serializer = AccountSerializer(
            instance=conta,
            many=True,
            context={'request':request},
        )
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AccountSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(ativa=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

