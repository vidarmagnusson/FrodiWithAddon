from secondary_schools.schools.models import School
from site_structure.shortcuts import render

def index(request):
	schools = School.objects.all()
	return render('secondary_schools/schools/all.html', {'schools':schools}, request)

def info(request):
	schools = School.objects.all()
	return render('secondary_schools/schools/all.html', {'schools':schools}, request)

def school_info(request, school):
	try:
		school = School.objects.get(abbreviation=school.upper())
		return render('secondary_schools/schools/info.html', {'school':school}, request)
	except:
		return index(request)
