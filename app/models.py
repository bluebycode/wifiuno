from django.db import models

class Log(models.Model):
    id = models.IntegerField(primary_key=True)
    comments = models.CharField(max_length=135, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Id: %d | Comments: %s ' % (self.id, self.comments)