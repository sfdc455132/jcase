from django.db import models

# Create your models here.


# 分類
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering=['id']
    def __str__(self):
        return f'{self.name}-{self.createdon}'

# 外包金額
class Amount(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    createdon = models.DateField(auto_now_add=True)
    class Meta:
        ordering=['id']
    def __str__(self):
        return f'{self.name}-{self.createdon}'

# 合作模式
class Mode(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    createdon = models.DateField(auto_now_add=True)
    class Meta:
        ordering=['id']
    def __str__(self):
        return f'{self.name}-{self.createdon}'


# 發案狀態
class State(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    createdon = models.DateField(auto_now_add=True)
    class Meta:
        ordering=['id']
    def __str__(self):
        return f'{self.name}-{self.createdon}'

# 工作週期
class Period(models.Model):
    name=models.CharField(max_length=50,unique=True,null=False)
    createdon = models.DateField(auto_now_add=True)
    class Meta:
        ordering=['id']
    def __str__(self):
        return f'{self.name}-{self.createdon}'