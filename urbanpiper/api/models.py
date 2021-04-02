import uuid
from django.db import models

# Create your models here.
class UniqueidTable(models.Model):
    uniqueid = models.CharField(max_length=50, default=str(uuid.uuid1()), primary_key = True, editable=False)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    active_state = models.CharField(max_length=10, default="active")
    hits = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.uniqueid}"


class DataTable(models.Model):
    uniqueid = models.ForeignKey(UniqueidTable, on_delete=models.CASCADE)  
    data = models.TextField()
    created_ts = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.data}"
