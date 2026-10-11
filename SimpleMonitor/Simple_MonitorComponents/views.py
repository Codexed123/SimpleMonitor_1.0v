from django.shortcuts import render, redirect, get_object_or_404
from Simple_MonitorComponents.forms import WebsiteForm
from Simple_MonitorComponents.models import CheckResult, WebsiteConfigure
import requests
import time
from django.utils import timezone
def main_page(request):
    data1 = WebsiteConfigure.objects.all()
    data2 = CheckResult.objects.all()
    down = CheckResult.objects.filter(is_up=False).count()
    up = CheckResult.objects.filter(is_up=True).count()
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            web_form = form.save()
            url_fetched = form.cleaned_data['url']
            try:
                time_scan_s = time.time()
                web_checker = requests.get(url_fetched, timeout=3)
                time_scan_e = time.time()
                if(web_checker.status_code == 200 or web_checker.status_code == 300):
                    print("Website Online")
                    data = CheckResult(web_configured=web_form,status_code=web_checker.status_code,response_time=(time_scan_e - time_scan_s)*1000,is_up=True)
                    data.save()
                else:
                    print("Website Offline")
                    data = CheckResult(web_configured=web_form,status_code=web_checker.status_code,response_time=(time_scan_e - time_scan_s)*1000,is_up=False)
                    data.save()
            except requests.RequestException:
                print("something went wrong")
                data = CheckResult(web_configured=web_form, status_code=0, response_time=0, is_up=False)
                data.save()
            return redirect('main')
    else:
        form = WebsiteForm()
    return render(request, "Simple_MonitorComponents/main_page.html", {'form': form, 'WC': data1, 'CR': data2, 'Up': up, 'Down': down})

def delete_button(request, id):
    data1 = get_object_or_404(CheckResult, id=id)
    data1.delete()
    return redirect('main')
