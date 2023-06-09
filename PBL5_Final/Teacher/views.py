from django.shortcuts import render, get_object_or_404, get_list_or_404
from JLPT.models import *
from Exam.models import *
from Document.models import *
from Bookapp.models import *
import Exam.forms as ExamForms
import Document.forms as DocumentForms
import Bookapp.forms as BookappForms
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from tablib import Dataset
import openpyxl

from .resources import (
    LevelResource,
    ExamResource,
    ExamPartResource,
    GroupQuestionResource,
    QuestionResource,
)
from django.contrib import messages
import media
import os
from django.core.files.base import ContentFile


from django.core.paginator import Paginator


# Create your views here.
def teacher_home(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(
        request, "pages/teacher_home.html", {"user": user, "profile": profile}
    )


def exam_manager(request, number):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    exams = Exam.objects.all().filter(user=user)
    paginator = Paginator(exams, 10)
    page_obj = paginator.page(number)
    context = {"number": number, "user": user, "profile": profile, "page_obj": page_obj}
    return render(request, "pages/teacher_exam_manager.html", context)


def teacher_add_exam(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ExamForms.AddExamForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.user = request.user
            exam.save()
            return redirect("Teacher:ExamManager", number=1)
    form = ExamForms.AddExamForm()
    context = {"form": form, "user": user, "profile": profile}
    return render(request, "pages/teacher_add_exam.html", context)


def teacher_delete_exam(request, pk):
    exam = Exam.objects.get(id=pk)
    exam.delete()
    return HttpResponse("")


def teacher_detail_exam(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    exam = get_object_or_404(Exam, id=pk)
    form = ExamForms.AddExamForm(instance=exam)
    context = {"user": user, "profile": profile, "form": form}
    return render(request, "pages/teacher_exam_detail.html", context)


def teacher_add_exam_detail(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    exam = get_object_or_404(Exam, id=pk)
    context = {"user": user, "profile": profile, "exam": exam}
    return render(request, "pages/teacher_add_exam_detail.html", context)

def importExcel(request, pk):
    exam = get_object_or_404(Exam, id=pk)
    if request.method == "POST":
        # exam = get_object_or_404(Exam, id=pk)
        exam_id = exam.id
        dataset = Dataset()
        try:
            new_file = request.FILES["my_file"]
            imported_data = dataset.load(new_file.read(), format="xlsx")
            for data in imported_data:
                level_resource = LevelResource()
                exam_resource = ExamResource()
                exam_part_resource = ExamPartResource()
                group_question_resource = GroupQuestionResource()
                question_resource = QuestionResource()

                # Importing data to ExamPart model
                exam_part_name = data[4]
                exam_part = ExamPart.objects.filter(
                    name=exam_part_name, exam=exam
                ).first()
                if not exam_part:
                    exam_part = ExamPart.objects.create(
                        name=exam_part_name, time=data[5], pass_score=data[6], exam=exam
                    )
                    exam_part.save()

                group_question_content = data[7]
                group_question_file_path = data[8]
                group_question = GroupQuestion.objects.filter(
                    content=group_question_content, exam_part=exam_part
                ).first()
                if not group_question:
                    group_question = GroupQuestion.objects.create(
                        content=group_question_content, exam_part=exam_part
                    )

                if group_question_file_path:
                    file_name = os.path.basename(group_question_file_path)
                    with open(group_question_file_path, "rb") as file:
                        file_content = file.read()
                        group_question.file.save(
                            file_name, ContentFile(file_content), save=True
                        )

                group_question.save()

                # Importing data to Question model
                new_question = Question()
                new_question.content = data[9]
                new_question.optionA = data[10]
                new_question.optionB = data[11]
                new_question.optionC = data[12]
                new_question.optionD = data[13]
                new_question.score = data[14]
                new_question.correct = data[15]
                new_question.group_question = group_question
                new_question.save()

            messages.success(request, "Imported successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred while importing the file: {e}")
    return render(request, "pages/form.html",{"exam":exam})

def document_manager(request, number):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    documents = Post.objects.all().filter(user=user)
    paginator = Paginator(documents, 10)
    page_obj = paginator.page(number)
    context = {"number": number, "user": user, "profile": profile, "page_obj": page_obj}
    return render(request, "pages/teacher_document_manager.html", context)

def teacher_add_document(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    # form = PostForm()
    # return render(request, 'pages/teacher_add_document.html', {'form': form})
    if request.method == "POST":
        form = DocumentForms.AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect("Teacher:DocumentManager", number=1)
    form = DocumentForms.AddDocumentForm()
    context = {"form": form, "user": user, "profile": profile}
    return render(request, "pages/teacher_add_document.html", context)

def teacher_delete_document(request, pk):
    document = Post.objects.get(id=pk)
    document.delete()
    return HttpResponse("")

def teacher_detail_document(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    document = get_object_or_404(Post, id=pk)
    form = DocumentForms.AddDocumentForm(instance=document)
    context = {"user": user, "profile": profile, "form": form}
    return render(request, "pages/teacher_document_detail.html", context)

def add_exam_skill(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile' : profile
    }
    return render(request,'pages/teacher_add_exam_skill.html',context)

def create_exam_skill(request):
    name = request.GET.get("name")
    level = request.GET.get("level")
    skill = request.GET.get("skill")
    time = request.GET.get("time")
    score = request.GET.get("score")
    
    exam_part = ExamPart(
        user = request.user,
        name = name,
        time = time,
        pass_score = score,
        skill = skill,
        level = level
    )
    exam_part.save()
    return redirect('Teacher:SkillManager',number = 1)

def edit_skill_exam(request,pk):
    exam = ExamPart.objects.get(id = pk)
    context = {
        'profile' : Profile.objects.get(user = request.user),
        'exam' : exam
    }
    return render(request,'pages/teacher_edit_exam_skill.html',context)

def update_skill_exam(request,pk):
    name = request.POST.get("name")
    level = request.POST.get("level")
    skill = request.POST.get("skill")
    time = request.POST.get("time")
    score = request.POST.get("score")
    exam = ExamPart.objects.get(id = pk)
    exam.name = name
    exam.level = level
    exam.skill = skill
    exam.time = time
    exam.pass_score = score
    exam.save()
    return redirect('Teacher:SkillManager',number = 1)

def delete_exam_skill(request,pk):
    exam = ExamPart.objects.get(id = pk)
    exam.delete()
    return HttpResponse('')

def exam_skill_manager(request,number):
    profile = Profile.objects.get(user = request.user)
    exams = ExamPart.objects.filter(user = request.user)
    paginator = Paginator(exams, 10)
    page_obj = paginator.page(number)
    context = {
        'profile' : profile,
        'exams' : exams,
        'number' : number,
        "page_obj": page_obj
    }
    return render(request,'pages/teacher_exam_skill_manager.html',context)

def add_exam_skill_detail(request,pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    part = ExamPart.objects.get(id = pk)
    context = {"profile": profile, "part": part}
    return render(request, "pages/add_exam_skill_detail.html", context)
def book_manager(request, number):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    books = Book.objects.filter(user=user)
    paginator = Paginator(books, 10)
    page_obj = paginator.page(number)
    context = {
        "number": number,
        "user": user,
        "profile": profile,
        "page_obj": page_obj
    }
    return render(request, "pages/teacher_book_manager.html", context)


def teacher_add_book(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        form = BookappForms.AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            form.save_m2m()  # Lưu các trường ManyToMany
            return redirect("Teacher:BookManager", number=1)
    else:
        form = BookappForms.AddBookForm()
    
    context = {"form": form, "user": user, "profile": profile}
    return render(request, "pages/teacher_add_book.html", context)



def teacher_delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return HttpResponse("")

def teacher_detail_book(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    book = get_object_or_404(Book, id=pk)
    form = BookappForms.AddBookForm(instance=book)
    context = {"user": user, "profile": profile, "form": form}
    return render(request, "pages/teacher_book_detail.html", context)
def add_exam_skill(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile' : profile
    }
    return render(request,'pages/teacher_add_exam_skill.html',context)

def importExcelSkill(request, pk):
    exam_part = get_object_or_404(ExamPart, id=pk)
    if request.method == "POST":
        # exam = get_object_or_404(Exam, id=pk)
        exam_part_id = exam_part.id
        dataset = Dataset()
        try:
            new_file = request.FILES["my_file"]
            imported_data = dataset.load(new_file.read(), format="xlsx")
            for data in imported_data:
                level_resource = LevelResource()
                exam_resource = ExamResource()
                exam_part_resource = ExamPartResource()
                group_question_resource = GroupQuestionResource()
                question_resource = QuestionResource()

                # Importing data to ExamPart model
                # exam_part_name = data[4]
                # exam_part = ExamPart.objects.filter(
                #     name=exam_part_name, exam=exam
                # ).first()
                # if not exam_part:
                #     exam_part = ExamPart.objects.create(
                #         name=exam_part_name, time=data[5], pass_score=data[6], exam=exam
                #     )
                #     exam_part.save()

                group_question_content = data[0]
                group_question_file_path = data[1]
                group_question = GroupQuestion.objects.filter(
                    content=group_question_content, exam_part=exam_part
                ).first()
                if not group_question:
                    group_question = GroupQuestion.objects.create(
                        content=group_question_content, exam_part=exam_part
                    )

                if group_question_file_path:
                    file_name = os.path.basename(group_question_file_path)
                    with open(group_question_file_path, "rb") as file:
                        file_content = file.read()
                        group_question.file.save(
                            file_name, ContentFile(file_content), save=True
                        )

                group_question.save()

                # Importing data to Question model
                new_question = Question()
                new_question.content = data[2]
                new_question.optionA = data[3]
                new_question.optionB = data[4]
                new_question.optionC = data[5]
                new_question.optionD = data[6]
                new_question.score = data[7]
                new_question.correct = data[8]
                new_question.group_question = group_question
                new_question.save()

            messages.success(request, "Imported successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred while importing the file: {e}")
    return render(request, "pages/add_exam_skill_excel.html",{"exam_part":exam_part})
def teacher_add_exam_skill(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ExamForms.AddExamSkillPartForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.user = request.user
            exam.save()
            return redirect("Teacher:ExamManager", number=1)
    form = ExamForms.AddExamSkillPartForm()
    context = {"form": form, "user": user, "profile": profile}
    return render(request, "pages/teacher_add_exam.html", context)

def teacher_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(
        request, "pages/teacher_profile.html", {"user": user, "profile": profile}
    )
