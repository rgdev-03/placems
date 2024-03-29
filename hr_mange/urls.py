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
    path('staffuser/', views.StaffFilterView.as_view(), name='staff_Filter'),
    path('stddata/', views.StudentDataFilter.as_view(), name='studnetData_Filter'),
    path('std2data/', views.StudentData2Filter.as_view(), name='studnetData2_Filter'),  
    path('stdcertspec/', views.StdCertificateSpec.as_view(), name='studnet_certificate_spec'),  
    path('stdacadsgpa/', views.StdAcademicSgpa.as_view(), name='studnet_sgpa_filter'),  
]
