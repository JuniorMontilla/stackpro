from django.shortcuts import render


def view_index(request):
	ctx = {}
	return render(request, 'base.html', ctx)