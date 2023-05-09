from django.db import models
class Student(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.SmallIntegerField()
    kurs = models.SmallIntegerField()
    student_raqami = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ism

class Reja(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    batafsil_malumot = models.CharField(max_length=100, blank=True, null=True)
    bajarilgan = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
