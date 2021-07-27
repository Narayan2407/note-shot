from django.shortcuts import render
from .models import  course,sem, course_pdf

# Create your views here.
from django.views import View
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def courses(request):
    categoryid = 0
    filtered_category = []

    try:
        categoryid = request.GET['category']
    except:
        pass

    if categoryid:
        clist= course.objects.filter(category_id=categoryid)
    else:
        clist = course.objects.all()

    n = len(clist)
    params = {
        'clist': clist
    }
    return render(request, 'courses.html', params)



def notes(request):
    cname= 0
    try:
        cname = request.GET['cid']
    except:
        pass

    if cname:
        pdf_list= course_pdf.objects.filter(ccid=cname)
    else:
        pdf_list = course_pdf.objects.all()

    # pdf_list = course_pdf.objects.all()
    n = len(pdf_list)
    params = {
        'pdf_list': pdf_list,
    }
    # context={'cname': cname}
    return render(request, 'pdf_display.html', params)

