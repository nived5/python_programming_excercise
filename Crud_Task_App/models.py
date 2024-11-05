from django.db import models

# Create your models here.
# class AddStudy(models.Model):
#     PhaseChoices = [
#         ('phase1','phase1'),
#         ('phase2','phase2'),
#         ('phase3','phase3'),
#         ]
#
#     studyName = models.CharField(max_length=100)
#     studyDescription = models.CharField(max_length=255)
#     SutdyPhase = models.CharField(max_length=20,choices=PhaseChoices,default='phase1')
#     SponsorName = models.CharField(max_length=255)

class AddStudy(models.Model):
    PhaseChoices = [
        ('phase1','phase1'),
        ('phase2','phase2'),
        ('phase3','phase3'),
        ]

    studyName = models.CharField(max_length=100)
    studyDescription = models.CharField(max_length=255)
    SutdyPhase = models.CharField(max_length=20,choices=PhaseChoices,default='phase1')
    SponsorName = models.CharField(max_length=255)