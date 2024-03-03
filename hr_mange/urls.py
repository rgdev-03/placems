from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'batch', views.BatchViewSet)
router.register(r'branch', views.BranchViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'certi_skills', views.Certi_SkillsViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'achievements', views.AchievementsViewSet)
router.register(r'academic_per', views.Academic_PerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stduser/', views.StudentFilterView.as_view(), name='student_filter'), 
    path('stdcert/', views.StdCertificate.as_view(), name='certificate_Filter'), 
    path('stdproj/', views.StdProjects.as_view(), name='project_Filter'), 
    path('stdacd/', views.StdAcademic.as_view(), name='academic_Filter'), 


]
