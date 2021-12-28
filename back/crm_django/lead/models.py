from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'
    
    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )
    
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
    CHOICES_PRIORITY = (
        (LOW,'Low'),
        (MEDIUM,'Medium'),
        (HIGH,'High'),
    )
    
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(help_text="email@email.com")
    phone = models.CharField(max_length=40)
    website = models.CharField(max_length=255, blank=True, null = True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value= models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(User, related_name='leads', help_text="Usuario creador",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ["-created_at"]
        
    """
    def get_absolute_url(self):
       
       # INVESTIGAR COMO USAR get_absolute_url
       # Retorna la url para acceder a una instancia particular de un autor.
       
        return reverse('dashboard/leads', args=[str(self.id)])
    """
    
    
    def __str__(self):
        return f"{self.company}"
        #return f"{self.company} + {self.contact_person} + {self.created_by}"
    