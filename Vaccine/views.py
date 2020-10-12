import django
django.setup()
from django.shortcuts import render

def test(request):

    question_num = 1
    if request.POST:
        if "Q1_next" in request.POST:
            question_num = 2
            request.session['Q1'] = '1'
        elif "Q2_next" in request.POST:
            question_num = 3
            request.session['Q2'] = '2'
        elif 'Q2_pre' in request.POST:
            question_num = 1
        elif "Q3_next" in request.POST:
            question_num = 4
            request.session['Q3'] = '3'
        elif 'Q3_pre' in request.POST:
            question_num = 2
    if question_num == 4:
        ans = request.session.get('Q1') + ', ' + request.session['Q2'] + ', ' + request.session['Q3']
        for i in ['Q4','Q5']:
            if request.session.exists(i):
                ans += ', ' + request.session.get(i)
            else:
                ans += ', ' + 'Null'
        context = {"question_num": question_num, 'service_cache': ans}
    else:
        context = {"question_num": question_num}
    return render(request,'../templates/test_vaccine.html', context)

def recommend(request):
    ans = request.session['Q1'] + request.session['Q2'] + request.session['Q3']
    context = {'service_cache':ans}
    return render(request, '../templates/vaccine_recommendation.html', context)
