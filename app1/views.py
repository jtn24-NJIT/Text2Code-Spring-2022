import io

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

import csv
import pandas as pd

def index(request):
    return render(request,'app1/index.html')

def upload_csv(request):
	csvfile = request.FILES['csv_file']
	csvfile = csvfile.read().decode("UTF-8")
	iostring = io.StringIO(csvfile)
	data = csv.reader(iostring, delimiter=',')
	# Store the data somewhere and pass for data
	data = pd.read_csv(data)
	data_html = data.to_html()
	context = {'loaded_data': data_html}
	return render(request, "upload_csv.html", context)

"""
def upload_csv(request):
	if request.POST:
		context = {}
		reader = csv.reader(request.FILES["csv_file"])
		for row in reader:
			header = list(row.keys())
			break

		data = {}

		for row in reader:
			for i in header:
				values = []
				values.append(row.get(i))
				if i not in data:
					data[i] = values
				data[i].extend(values)

		context['header'] = header
		context['data'] = data
		return render(request, 'upload_csv.html', context)

	return (render(request, 'upload_csv.html'))
"""

"""
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
"""
