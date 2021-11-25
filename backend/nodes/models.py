from django.db import models

# Create your models here.




class Node(models.Model):
    
    url = models.URLField('url of node', unique=True, null=False, blank=False)
    allowIncoming = models.BooleanField()
    allowOutgoing = models.BooleanField()
    
    authRequiredIncoming = models.BooleanField()
    authRequiredOutgoing = models.BooleanField()
    
    incomingName = models.CharField(blank=False, null=False, default='defaultName',max_length=128,)
    outgoingName = models.CharField(blank=False, null=False, default='defaultName',max_length=128,)
    
    incomingPassword = models.CharField(max_length=128,blank=False, null=False,default="passpass")
    outgoingPassword = models.CharField(max_length=128,blank=False, null=False,default="passpass")
    
    description = models.CharField(max_length=300, blank=True, default=False)
    
    
    
    def __str__(self) -> str:
        return str(self.url)