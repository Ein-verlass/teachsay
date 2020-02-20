from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', '女'),
    )

    username = models.CharField(max_length=128, default='')
    phonenumber = models.CharField(max_length=128, unique=True, default='')
    school = models.CharField(max_length=128, default='')
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):       #显示对象信息
        return self.phonenumber

    class Meta:
        ordering = ["-c_time"]
        verbose_name = '用户'
        verbose_name_plural = "用户"
