from django.db import models
from django.conf import settings  

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    batch_code = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return f"{self.batch_code}"

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255, unique=True, null=False)
    
    def __str__(self):
        return f"{self.branch_code} - {self.branch_name}"

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile', null=True)

    std_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    USN = models.CharField(max_length=20, unique=True, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sec = models.CharField(max_length=1, null=True)
    sem = models.CharField(max_length=1, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100)
    

   

    def save(self, *args, **kwargs):
        self.USN = self.USN.upper() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.USN}"

class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='staff_profile',null=True)

    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
 
    mobile = models.CharField(max_length=15, null=True)
    staff_type = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}  {self.branch}"

class Certi_Skills(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    certi_e_date = models.DateField()
    image_upload = models.ImageField(upload_to='certification_images/', null=True)
    org = models.CharField(max_length=255,default="aa")


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=50, null=False)
    project_name = models.CharField(max_length=255, null=False)
    # project_specification = models.TextField(null=False)
    project_repo_url = models.CharField(max_length=255,null=True)
    certificate = models.ImageField(upload_to='project_certificates/', null=True)

class Achievements(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    event_name = models.CharField(max_length=255, null=False)
    certification = models.ImageField(upload_to='achievement_certificates/', null=True)

class Academic_Per(models.Model):
    id = models.AutoField(primary_key=True)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    acad_sem = models.CharField(max_length=255, null=False)
    acad_sgpa = models.CharField(max_length=255, null=False)
    # sem10th = models.CharField(max_length=255, null=False)
    # sem12th_diploma = models.CharField(max_length=255, null=False)
    
