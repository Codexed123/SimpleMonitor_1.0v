from django.db import models

# Create your models here.

class WebsiteConfigure(models.Model):
    web_name = models.CharField(max_length=50)
    url = models.URLField()
    created_at = models.DateField(auto_now=True)

class CheckResult(models.Model):
    web_configured = models.ForeignKey(WebsiteConfigure, on_delete=models.CASCADE, related_name="websites")
    status_code = models.IntegerField()
    response_time = models.CharField(max_length=50, blank=True)
    is_up = models.BooleanField(default=False)
    checked_at = models.DateTimeField(auto_now_add=True)
