from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from stackpro.apps.employee.models import  advert, answer 
from  stackpro.apps.employee.forms import  advertform, answerform

def view_work(request):
	message = ''
	if request.method == 'POST':
		form = advertform(request.POST, request.FILES)
		if form.is_valid():
			status = False
			company = form.cleaned_data['company']
			avatar = form.cleaned_data['avatar']
			website = form.cleaned_data['website']
			titlefoemployee  = form.cleaned_data['titlefoemployee']
			place = form.cleaned_data['place']
			salary  =  form.cleaned_data['salary']
			prove = form.cleaned_data['prove']
			descriptionofjob = form.cleaned_data['descriptionofjob']
			advertobject =  advert()
			advertobject.status = status
			if avatar:
				advertobject.avatar = avatar
			advertobject.company = company
			advertobject.website = website
			advertobject.titlefoemployee = titlefoemployee
			advertobject.place = place
			advertobject.salary = salary
			advertobject.prove = prove
			advertobject.descriptionofjob = descriptionofjob
		 	advertobject.save()
			return HttpResponseRedirect('/')	 	
		message = 'error, vuelva a intentarlo'
		ctx ={'message':message, 'form':form}
		return render(request, 'employee/employee.html', ctx)
	form = advertform()
	ctx = {'form':form}
	return render(request, 'employee/employee.html', ctx)