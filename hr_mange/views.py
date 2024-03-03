from rest_framework import viewsets,generics
from .models import Batch, Branch, Student, Staff, Certi_Skills, Projects, Achievements, Academic_Per
from .serializers import BatchSerializer, BranchSerializer, StudentSerializer, StaffSerializer, Certi_SkillsSerializer, ProjectsSerializer, AchievementsSerializer, Academic_PerSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    

class Certi_SkillsViewSet(viewsets.ModelViewSet):
    queryset = Certi_Skills.objects.all()
    serializer_class = Certi_SkillsSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class Academic_PerViewSet(viewsets.ModelViewSet):
    queryset = Academic_Per.objects.all()
    serializer_class = Academic_PerSerializer


# Filters

class StudentFilterView(generics.ListAPIView):
    serializer_class = StudentSerializer

    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']  # Define fields for filtering

# get the student certificate by the std_id
class StdCertificate(generics.ListAPIView):
    serializer_class = Certi_SkillsSerializer

    queryset = Certi_Skills.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['std_id'] 

# get the student Projects by the std_id

class StdProjects(generics.ListAPIView):
    serializer_class = ProjectsSerializer

    queryset = Projects.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['std_id'] 


class StdAcademic(generics.ListAPIView):
    serializer_class = Academic_PerSerializer

    queryset = Academic_Per.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['std_id']  

