from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer

from .models import Task

# Create your views here.

#api views create a interface permitting manipulation of data through CRUD methods, and depending on the request method

@api_view(['GET', 'POST'])
def task_list(request):
    #GET request
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)

    #POST request
    elif request.method == 'POST':
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
        return Response(task_serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    #We check if the Task we are looking for actually exists
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'message': 'tuto does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #GET request
    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data)

    #PUT request
    elif request.method == 'PUT':
        task_serializer = TaskSerializer(instance=task, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
        return Response(task_serializer.data)

    #DELETE request
    elif request.method == 'DELETE':
        task.delete()
        return Response({'message': 'tuto successfully deleted'}, status=status.HTTP_200_OK)
