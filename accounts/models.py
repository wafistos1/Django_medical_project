from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

USER_TYPE_CHOICES = (
      ('Doctor', 'Doctor'),
      ('Nurse', 'Nurse'),
      ('Personnel', 'Personnel'),
  )

class CostumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='costumuser')
    identifier = models.CharField(max_length=200, null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return f'{self.user.username}'


    
class PatientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    identifier = models.CharField(max_length=200, null=True, blank=True)
    user_charge = models.ForeignKey(CostumUser, on_delete=models.SET_NULL, blank=True, null=True) 
    
    def __str__(self):
        return f'{self.identifier} suivi par {self.user_charge.user.username}'
    
    def get_delete_model_url(self):  # new
        return reverse('delete_patient', args=[str(self.id)])
