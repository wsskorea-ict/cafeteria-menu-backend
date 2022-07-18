from django.db import models


class Division(models.Model):
    NAME = models.CharField(max_length=15)

    class Meta:
        db_table = 'DIVISION_TB'


class Cafeteria(models.Model):
    NAME = models.CharField(max_length=15)
    DIVISION = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='DIVISION_FK')

    class Meta:
        db_table = 'CAFETERIA_TB'


class Corner(models.Model):
    NAME = models.CharField(max_length=10)
    CAFETERIA = models.ForeignKey(Cafeteria, on_delete=models.CASCADE, related_name='CORNER_FK')

    class Meta:
        db_table = 'CORNER_TB'


class Slot(models.Model):
    SLOT = models.CharField(max_length=5)
    START = models.TimeField()
    END = models.TimeField()
    CAFETERIA = models.ForeignKey(Cafeteria, on_delete=models.CASCADE, related_name='SLOT_FK')

    class Meta:
        db_table = 'SLOT_TB'


class Menu(models.Model):
    MENU = models.CharField(max_length=100)
    DATE = models.DateField()
    CORNER = models.ForeignKey(Corner, on_delete=models.CASCADE, related_name='MENU_CORNER_FK')
    SLOT = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='MENU_SLOT_FK')

    class Meta:
        db_table = 'MENU_TB'
