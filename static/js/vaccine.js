var q1choice = ''
var q2choice = ''
var q3choice = ''
var q4choice = 'Null'
var q5choice = 'Null'
function q1(){
    document.getElementById('question1').style.display='None';
    document.getElementById('question2').style.display='block'
    document.getElementById('block1').style.display = 'None';
    document.getElementById('block2').style.display = 'block';
    q1choice=$('input:radio[name="Q1"]:checked').val()
}
function q2(){
    document.getElementById('question2').style.display='None'
    document.getElementById('question3').style.display='block'
    document.getElementById('block3').style.display='block';
    document.getElementById('block2').style.display='None';
    q2choice = document.getElementById('que2').value;

    if (q2choice == '0-2 months'){
        document.getElementById('nexti3').style.display='None'
        document.getElementById('next3').style.display='None'
    }
}
function q3() {
    q3choice=$('input:radio[name="Q3"]:checked').val()
    if (q2choice == '0-2 months'){
        document.getElementById('submit').style.display='block'
    }
    else if (q3choice == 'Yes') {
        document.getElementById('question3').style.display = 'None'
        document.getElementById('question4').style.display = 'block'
        document.getElementById('block4').style.display='block';
        document.getElementById('block3').style.display='None';
    }
    else{
       if(q1choice == 'Yes' && q2choice == '1-5 years') {
           document.getElementById('question3').style.display = 'None'
           document.getElementById('question5').style.display = 'block'
           document.getElementById('block5').style.display='block';
           document.getElementById('block3').style.display='None';
       }
        else {
            document.getElementById('submit').style.display='block'
            document.getElementById('next3').style.display='None';
            document.getElementById('nexti3').style.display='None';
        }
    }

}
function q4(){
    q4choice = document.getElementById('que4').value
    if(q1choice == 'Yes' && q2choice == '1-5 years'){
        document.getElementById('question4').style.display = 'None'
        document.getElementById('question5').style.display = 'block'
        document.getElementById('block5').style.display='block';
        document.getElementById('block4').style.display='None';
    }
    else if(q1choice != 'Yes' || q2choice != '1-5 years') {
        document.getElementById('submit').style.display = 'block'
        document.getElementById('next4').style.display='None';
        document.getElementById('nexti4').style.display='None';
    }
}
function q5(){
    q5choice = $('input:radio[name="Q5"]:checked').val()
    document.getElementById('submit').style.display='block'
}

var compare_str = ''
var recommendation_list = '{{ recommendation|safe }}';
var obj =JSON.parse(recommendation_list);

function submit(){
    compare_str = q1choice + ', ' + q2choice + ', ' + q3choice
                    + ', ' + q4choice + ', ' + q5choice

    for (i = 0; i <obj.list.length; i++){
        if (obj.list[i].choice == compare_str){
            document.getElementById('submit recommendation').innerText = obj.list[i].recommendation
        }
    }
document.getElementById('recom').style.display = 'block';
}

function icon1() {
   document.getElementById('question1').style.display = 'None';
   document.getElementById('question2').style.display = 'block';
   document.getElementById('block1').style.display = 'None';
   document.getElementById('block2').style.display = 'block';
}

function icon2(){
   document.getElementById('question1').style.display='block';
   document.getElementById('question2').style.display='None';
   document.getElementById('block1').style.display='block';
   document.getElementById('block2').style.display='None';
}

function  icon3(){
   document.getElementById('question3').style.display='block';
   document.getElementById('question2').style.display='None';
   document.getElementById('block3').style.display='block';
   document.getElementById('block2').style.display='None';
}

function icon4(){
   document.getElementById('question2').style.display='block';
   document.getElementById('question3').style.display='None';
   document.getElementById('block2').style.display='block';
   document.getElementById('block3').style.display='None';
   document.getElementById('submit').style.display='None'
}

function icon5(){
   q3choice=$('input:radio[name="Q3"]:checked').val()
    if (q3choice == 'Yes') {
        document.getElementById('question3').style.display = 'None'
        document.getElementById('question4').style.display = 'block'
        document.getElementById('block4').style.display='block';
        document.getElementById('block3').style.display='None';
    }
    else{
       if(q1choice == 'Yes' && q2choice == '1-5 years') {
           document.getElementById('question3').style.display = 'None'
           document.getElementById('question5').style.display = 'block'
           document.getElementById('block5').style.display='block';
           document.getElementById('block3').style.display='None';
       }
        else {
            document.getElementById('submit').style.display='block'
        }
    }
}

function icon6() {
    document.getElementById('question4').style.display = 'None'
    document.getElementById('question3').style.display = 'block'
    document.getElementById('block4').style.display = 'None'
    document.getElementById('block3').style.display = 'block'
    document.getElementById('submit').style.display = 'None'
}

function icon7() {
    q4choice = document.getElementById('que4').value
    if (q1choice == 'Yes' && q2choice == '1-5 years') {
        document.getElementById('question4').style.display = 'None'
        document.getElementById('question5').style.display = 'block'
        document.getElementById('block5').style.display = 'block'
        document.getElementById('block4').style.display = 'None'
        document.getElementById('submit').style.display = 'block'

    } else if (q1choice != 'Yes' || q2choice != '1-5 years') {
        document.getElementById('submit').style.display = 'block'
    }
}

function icon8() {

   if (q2choice != '0-2 months' && q3choice == 'Yes') {
       document.getElementById('question5').style.display = 'None'
       document.getElementById('question4').style.display = 'block'
       document.getElementById('block5').style.display = 'None'
       document.getElementById('block4').style.display = 'block'
       document.getElementById('submit').style.display = 'None'
   }
   else{
       document.getElementById('question5').style.display = 'None'
       document.getElementById('question3').style.display = 'block'
       document.getElementById('block5').style.display = 'None'
       document.getElementById('block3').style.display = 'block'
       document.getElementById('submit').style.display = 'None'
   }
}

function dispear(){
   document.getElementById('previous3').style.display='None';
   document.getElementById('previousi3').style.display='None';
   document.getElementById('previous4').style.display='None';
   document.getElementById('previousi4').style.display='None';
   document.getElementById('previous5').style.display='None';
   document.getElementById('previousi5').style.display='None';
   document.getElementById('next3').style.display='None';
   document.getElementById('nexti3').style.display='None';
   document.getElementById('next4').style.display='None';
   document.getElementById('nexti4').style.display='None';
}