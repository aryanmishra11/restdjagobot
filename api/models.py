from django.db import models

# Create your models here.
class  CodeExplainer(models.Model):
    _input= models.CharField(max_length=500)
    _output=models.TextField()
    
    class Meta:
        db_table="t_code_explainer"