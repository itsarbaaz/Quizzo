from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserLoginForm, RegistrationForm
from django.contrib.auth import authenticate, logout,login as user_login
from django.contrib.auth.decorators import login_required
from .models import QuizProfile,AttemptedQuestion
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request,'home.html')

def leaderboard(request):
    top_quiz_profiles = QuizProfile.objects.order_by('-total_score')[:500]
    total_count = top_quiz_profiles.count()
    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'leaderboard.html', context=context)

def register(request):
    title = "Create account"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'registration.html', context=context)

def login(request):
        title = "Login"
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            user_login(request, user)
            return redirect('/user_home')
        return render(request, 'login.html', {"form": form, "title": title})


@login_required()
def user_home(request):
    context = {}
    return render(request, 'user_home.html', context=context)

@login_required()
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')

        attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = attempted_question.question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        quiz_profile.evaluate_attempt(attempted_question, selected_choice)

        return redirect(attempted_question)

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)

        context = {
            'question': question,
        }

        return render(request, 'play.html', context=context)
    


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def submission_result(request, attempted_question_pk):
    attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
    context = {
        'attempted_question': attempted_question,
    }

    return render(request, 'submission_result.html', context=context)

