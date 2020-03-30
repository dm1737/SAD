from django.shortcuts import render, HttpResponse, redirect
from .models import Profile, Journal, AdjustingJournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .forms import NewUserForm, EmailForm, JournalForm, AdjustingJournalForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse 
import re 


def homepage(request):
    return render(request = request,
                template_name="accounts/home.html",)
                
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("accounts:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "accounts/register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                template_name = "accounts/register.html",
                context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("accounts:homepage")
def fgtpassword(request):
    if request.method == 'GET':
        form = EmailForm()
        return render(request = request,
                template_name = "accounts/forgot_password.html",
                context={"form":form})
    if request.method == 'POST':    
        form = EmailForm(data=request.POST)
        if form.is_valid():            
            email = form.cleaned_data.get('email')            
            #user = authenticate(email=email)
            #print(user)
            if email is not None:                
                messages.info(request, f"Email sent to {email}")
               # return redirect('/')
            else:
                messages.error(request, "Invalid email.")
        else:
            messages.error(request, "Invalid email.")
        return render(request = request,
                template_name = "accounts/forgot_password.html",
                context={"form":form})
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.profile.attempts < 3:
                        user.profile.attempts = 0
                        login(request, user)                        
                        messages.info(request, f"You are now logged in as {username}")
                        return redirect('/')
                    else:
                        user.is_active = False
                        user.save()
                        messages.warning(request, 'Your account has been locked out because of too many failed login attempts.')
            else:
                raise Exception
        except:
            username = form.cleaned_data.get('username')
            userset = User.objects.filter(username=username)           
            if userset.exists():
                userID = userset[0].id
                obj = User.objects.get(id=userID)
                obj.profile.attempts += 1
                obj.save()
                if obj.profile.attempts > 2:
                    messages.warning(request, 'Your account has been locked out because of too many failed login attempts.')
                else:                               
                    messages.error(request, "Invalid password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})

def profile(request):
    return render(request = request,
                    template_name = "accounts/profile.html")
                    #context={"form":form})

def help(request):
    return render(request = request, template_name = "accounts/help.html") 

def view_account(request):
    args = {'user': request.user}
    return render(request, 'accounts/accountinfo.html', args)

def ledger(request):
    model = Journal
    query_set = Journal.objects.all()
    return render(request = request,
                  template_name = "accounts/ledger.html",
                  context = {"journals": query_set})

def journals(request):
    if request.method == 'POST': 
        form = JournalForm(request.POST or None, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.profile.role == 2:                
                form.save()
                Journalset = Journal.objects.filter(Journal_number=form.cleaned_data.get('Journal_number'))                           
                if Journalset.exists():
                    JournalID = Journalset[0].id
                    obj = Journal.objects.get(id=JournalID)
                    obj.status = 1
                    obj.save()
                form = JournalForm()
            else:                
                form.save()
                form = JournalForm() 

    else:
        form = JournalForm() 
    context = {'form': form}
    return render(request, 'accounts/journals.html', context)

def manageJournals (request):
    if request.method == 'POST':
        status = request.POST['status']
        number_list = re.findall(r'\d+', status)
        a_string = "".join(number_list)
        number = int(a_string)
        status_list = re.findall(r'\D+',status)
        status_cleaned = "".join(status_list)
        journalSet = Journal.objects.filter(Journal_number=number)           
        if journalSet.exists():
            journalID = journalSet[0].id
            obj = Journal.objects.get(id=journalID)
            if status_cleaned=="Pending":
                obj.reason_for_rejection=""
                obj.status = 1
                messages.info(request, "Saved!")
            if status_cleaned=="Accepted":
                obj.reason_for_rejection=""
                obj.status = 2
                messages.info(request, "Saved!")
            if status_cleaned=="Rejected":
                comment_name=str(request.POST.get("status"))
                comment = request.POST[comment_name]
                if comment != "":
                    obj.reason_for_rejection = comment
                    obj.status = 3
                    messages.info(request, "Saved!")
                else:
                    messages.warning(request,"Please enter a reason for rejecting this journal.")           
            obj.save()
        journal_list = Journal.objects.all()
        ad_journal_list = AdjustingJournalEntry.objects.all()
        return render(request = request,
                        template_name = "accounts/manage_journals.html",
                        context={#"form":form,
                        "journal_list":journal_list,
                        "ad_journal_list":ad_journal_list
                        })
    if request.method == 'GET':
        journal_list = Journal.objects.all()
        ad_journal_list = AdjustingJournalEntry.objects.all()
        return render(request = request,
                        template_name = "accounts/manage_journals.html",
                        context={#"form":form,
                        "journal_list":journal_list,
                        "ad_journal_list":ad_journal_list
                        })
def journal_view (request,id):
    journal = Journal.objects.get(Journal_number=id)
    return render(request = request,
                    template_name = "accounts/journal_view.html",
                    context={"journal":journal,                      
                    })

def adjusting_journals(request):
    if request.method == 'POST': 
        form = AdjustingJournalForm(request.POST or None, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.profile.role == 2:                
                form.save()
                Journalset = AdjustingJournalEntry.objects.filter(Adjusted_journal_number=form.cleaned_data.get('Journal_number'))                           
                if Journalset.exists():
                    JournalID = Journalset[0].id
                    obj = AdjustingJournalEntry.objects.get(id=JournalID)
                    obj.status = 2
                    obj.save()
                form = AdjustingJournalForm()
            else:                
                form.save()
                form = AdjustingJournalForm() 

    else:
        form = AdjustingJournalForm() 
    context = {'form': form}
    return render(request, 'accounts/adjusting_journals.html', context)