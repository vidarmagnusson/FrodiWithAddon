from django.db import models
from secondary_schools.schools.models import School

class StudentSociety(models.Model):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(School)
    description = models.TextField()
    website = models.URLField()
    email = models.EmailField()
    chairman_email = models.EmailField()
    logo = models.ImageField(upload_to='studentsocieties/logos', 
                             blank=True, null=True)
    photo = models.ImageField(upload_to='studentsocieties/photos',
                               blank=True, null=True)
    video = models.FileField(upload_to='studentsocieties/videos',
                              blank=True, null=True)

    def __unicode__(self):
        return self.name, '-', self.school
