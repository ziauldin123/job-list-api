from django.db import models
from django.contrib .auth.models import User
# Create your models here.


EXP_TYPE = (
    ('1', "None"),
    ('2', "1 Year"),
    ('3', "2 Year"),
    ('4', "3 Year"),
    ('5', "4 Year"),
    ('6', "5 Year"),
    ('7', "6 Year"),
    ('8', "7 Year"),
    ('9', "8 Year"),
    ('10', "9 Year"),
    ('11', "10 Year")
)
JOB_TYPE = (
    ('1', "Govt Job"),
    ('2', "FPSC"),
    ('3', "PPSC"),
    ('4', "NTS"),
    ('5', "PAK ARMY"),
    ('6', "PAK NAVY"),
    ('7', "PAK AIR FORCE")    
)

class Job(models.Model):     
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    jtype = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(choices=JOB_TYPE, max_length=10)
    post_image=models.ImageField(upload_to='jobs')
    last_date = models.DateField(null=False)
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateField()
    status = models.CharField(max_length=100, default="")
    posts = models.IntegerField(default=0, blank=True)
    required_exp=models.CharField(choices=EXP_TYPE, max_length=50)	
    
    def __str__(self):
        return self.title
