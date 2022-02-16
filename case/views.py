from django.shortcuts import render,redirect
from .models import Case
from .forms import CreateCaseForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def case(request,id):
    case=Case.objects.get(id=id)

    case.view+=1
    case.save()
    return render(request,'./case/case.html',{'case':case})
    
@login_required(login_url='login')
def create_case(request):
    form = CreateCaseForm()

    if request.method == 'POST':
        form = CreateCaseForm(request.POST)

        if form.is_valid():
            case = form.save(commit=False)
            # 設定擁有者
            case.owner = request.user
            case.save()
            form.save_m2m()
            return redirect('cases')

    return render(request,'./case/create-case.html',{'form':form})













def cases(request):
    cases=Case.objects.all()
    print(cases)
    for case in cases:
        print(case)

    return render(request,'./case/cases.html',{'cases':cases})