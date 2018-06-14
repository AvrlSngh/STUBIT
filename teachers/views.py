from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import teacher_required
from . import forms

@login_required(login_url="/accounts/login/")
@teacher_required
def teacher_dashboard(request):
    return render(request, 'teachers/teacher_dashboard.html')

# View for uploading papers
@login_required(login_url="/accounts/login/")
@teacher_required
def upload_paper(request):
    if request.method == 'POST':
        upload_paper_form = forms.UploadPaper(request.POST, request.FILES)
        if upload_paper_form.is_valid():
            # save paper to db
            instance = upload_paper_form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('teachers:teacher_dashboard')
    else:
        upload_paper_form = forms.UploadPaper()
    return render(request, 'teachers/upload_paper.html', {'upload_paper_form':upload_paper_form})

# View for uploading notes
@login_required(login_url="/accounts/login/")
@teacher_required
def upload_notes(request):
    if request.method == 'POST':
        upload_notes_form = forms.UploadNote(request.POST, request.FILES)
        if upload_notes_form.is_valid():
            # save paper to db
            instance = upload_notes_form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('teachers:teacher_dashboard')
    else:
        upload_notes_form = forms.UploadNote()
    return render(request, 'teachers/upload_notes.html', {'upload_notes_form':upload_notes_form})


# View for uploading links
@login_required(login_url="/accounts/login/")
@teacher_required
def upload_links(request):
    if request.method == 'POST':
        upload_links_form = forms.UploadLink(request.POST)
        if upload_links_form.is_valid():
            # save paper to db
            instance = upload_links_form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('teachers:teacher_dashboard')
    else:
        upload_links_form = forms.UploadLink()
    return render(request, 'teachers/upload_links.html', {'upload_links_form':upload_links_form})
