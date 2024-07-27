from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email= email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)
        

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddRemoveTaskMemberView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request , pk):
        task = Task.objects.get(pk=pk)
        user = User.objects.get(pk=request.data['user_id'])
        task.members.add(user)
        return Response({'status': 'member added'})
    
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        user = User.objects.get(pk=request.data['user_id'])
        task.members.remove(user)
        return Response({'status': 'member removed'})
    

class ViewTaskMembersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        task = Task.objects.get(pk=self.kwargs['pk'])
        return task.members.all()

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def perform_create(self, serializer):
        task = Task.objects.get(pk=self.kwargs['task_pk'])
        serializer.save(task=task, user=self.request.user)

class UpdateTaskStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.status = request.data['status']
        task.save()
        return Response({'status': 'task status updated'})


