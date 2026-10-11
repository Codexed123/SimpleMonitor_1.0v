from django import forms
from Simple_MonitorComponents.models import WebsiteConfigure
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = WebsiteConfigure
        fields = ['web_name', 'url']
