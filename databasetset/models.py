from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Gardian_info(models.Model):
    relation_type=models.CharField(max_length=15)
    f_name=models.CharField(max_length=15)
    m_name=models.CharField(max_length=15)
    l_name=models.CharField(max_length=15)
    occupation=models.CharField(max_length=20,null=True,default='')
    annual_income=models.IntegerField(default=0,null=True,)


class Contact_info(models.Model):
    addrese=models.TextField();
    city=models.CharField(max_length=10)
    pincode=models.IntegerField()
    ph_no=models.CharField(max_length=12)
    email=models.EmailField()

    def __str__(self):
        return self.email



class Teacher_info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    T_ID = models.CharField(primary_key=True, max_length=10)
    f_name = models.CharField(max_length=15)
    m_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)
    birthdate = models.DateField()
    blood_group = models.CharField(max_length=3)
    password = models.CharField(max_length=10)
    contact=models.OneToOneField(Contact_info,on_delete=models.CASCADE)
    img=models.FileField(blank=True)
    is_class_tec=models.BooleanField(default=False)
    def __str__(self):
        return "Teacher_id is: " + self.T_ID + " name is :" + self.f_name


class Standard_info(models.Model):
    std_num=models.IntegerField()
    class_teacher=models.OneToOneField(Teacher_info,on_delete=models.CASCADE)

    strength=models.IntegerField()

    def __str__(self):
        return str(self.std_num)



class Student_info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    S_ID=models.CharField(primary_key=True,max_length=10)
    f_name = models.CharField(max_length=15,blank=True)
    m_name = models.CharField(max_length=15,blank=True)
    l_name = models.CharField(max_length=15,blank=True)
    gender=models.CharField(max_length=7,blank=True)
    birthdate=models.DateField(null=True)
    blood_group=models.CharField(max_length=3,blank=True)
    password=models.CharField(max_length=10,blank=True)
    gardian=models.ForeignKey(Gardian_info,on_delete=models.CASCADE,blank=True,null=True)
    contact=models.OneToOneField(Contact_info,on_delete=models.CASCADE,blank=True,null=True)
    class_teacher=models.ForeignKey(Teacher_info,models.CASCADE,blank=True,null=True)
    img=models.FileField(blank=True)
    std=models.ForeignKey(Standard_info,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return "Stu_id is: "+self.S_ID+" name is :"+self.f_name


    '''def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile=Student_info.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)'''






class Subject_info(models.Model):
    name=models.CharField(max_length=15)
    teacher=models.ManyToManyField(Teacher_info)
    std=models.ForeignKey(Standard_info , on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Notes(models.Model):
    pdf=models.FileField(upload_to='nots',blank=True)
    teacher=models.ForeignKey(Teacher_info,models.CASCADE)
    name =models.CharField(max_length=15,blank=True)
    def __str__(self):
        return ("Topic is : "+self.name+" and Teacher is "+self.teacher.f_name)


class Announcement(models.Model):
    due_date=models.DateField()
    end_date=models.DateField()
    msg=models.CharField(max_length=150)
    teacher=models.ForeignKey(Teacher_info,models.CASCADE)
    def __str__(self):
        return "Due Date is : "+str(self.due_date)+" End Date is "+str(self.end_date)