from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request ,'app1/index.html')

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "app1/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("app1:upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("app1:upload_csv"))
	except Exception as e:

		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("app1:upload_csv"))