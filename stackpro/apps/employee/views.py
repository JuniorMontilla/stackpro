from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from stackpro.apps.employee.models import  advert, answer
from  stackpro.apps.employee.forms import  advertform, answerform

def view_answer(request):
	message = ""
	if request.method == 'POST':
		form = answerform(request.POST)
		if form.is_valid():
			links  = form.cleaned_data['links']
			email  = form.cleaned_data['email']
			answerobj = answer()
			answerobj.links  = links
			answerobj.email  = email
			answerobj.fk     = request.user.id
			answerobj.save()
			return HttpResponseRedirect("/employee/")
		message = 'error, vuelva a intentarlo'
		ctx ={'message':message, 'form':form}
		return render(request, 'details/details.html', ctx)
	for foreign in  advert.objects.all():
		answerobj = answer.objects.filter(fk=foreign)
	form = answerform()
	ctx = {"form":form, "answerdata":answerobj}
	return render(request, 'answer/answer.html', ctx)

def view_work(request):
	message = ''
	if request.method == 'POST':
		form = advertform(request.POST, request.FILES)
		if form.is_valid():
			status = False
			company = form.cleaned_data['company']
			avatar = form.cleaned_data['avatar']
			website = form.cleaned_data['website']
			titleofemployee  = form.cleaned_data['titleofemployee']
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
			advertobject.titleofemployee = titleofemployee
			advertobject.place = place
			advertobject.salary = salary
			advertobject.descriptionofjob = descriptionofjob
			advertobject.prove = prove
		 	advertobject.save()
			return HttpResponseRedirect('/')
		message = 'error, vuelva a intentarlo'
		ctx ={'message':message, 'form':form}
		return render(request, 'employee/employee.html', ctx)
	form = advertform()
	ctx = {'form':form}
	return render(request, 'employee/employee.html', ctx)
