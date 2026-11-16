from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import python as notes
from .models import html as HtmlNotes
from .models import css as CssNotes
from .models import javascript as JsNotes
def home(request):
    return render(request, 'home.html')
def multiple(request):
    a = notes.objects.all()
    return render(request, 'multiple.html', {'aa': a})
def html_view(request):
    a = HtmlNotes.objects.all()
    return render(request, 'html_notes.html', {'aa': a})
def css_view(request):
    a = CssNotes.objects.all()
    return render(request, 'css_notes.html', {'aa': a})
def javascript_view(request):
    a = JsNotes.objects.all()
    return render(request, 'javascript_notes.html', {'aa': a})
def forms(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if category and question and answer:
            if category == 'notes':
                notes.objects.create(
                    question=question,
                    answer=answer
                )
                messages.success(
                    request,
                    'Python note added successfully!'
                )
                return redirect('multiple')    
            elif category == 'html':

                HtmlNotes.objects.create(
                    question=question,
                    answer=answer
                )
                messages.success(
                    request,
                    'HTML note added successfully!'
                )

                return redirect('html') 
            elif category == 'css':

                CssNotes.objects.create(
                    question=question,
                    answer=answer
                )
                messages.success(
                    request,
                    'CSS note added successfully!'
                )
                return redirect('css')
            elif category == 'javascript':

                JsNotes.objects.create(
                    question=question,
                    answer=answer
                )

                messages.success(
                    request,
                    'JavaScript note added successfully!'
                )

                return redirect('javascript')

            else:

                messages.error(
                    request,
                    'Invalid category selected.'
                )

        else:

            messages.error(
                request,
                'Please select a category and fill in all fields.'
            )

    return render(request, 'forms.html')



def update(request, abc):

    try:

        obj = notes.objects.get(id=abc)

        if request.method == 'POST':

            question = request.POST.get('question')
            answer = request.POST.get('answer')

            if question and answer:

                obj.question = question
                obj.answer = answer
                obj.save()

                messages.success(
                    request,
                    'Python note updated successfully!'
                )

                return redirect('multiple')

            else:

                messages.error(
                    request,
                    'Please fill in all fields.'
                )

        return render(
            request,
            'update.html',
            {'i': obj, 'category': 'python'}
        )

    except notes.DoesNotExist:

        return HttpResponse('Record not found')



def delete(request, abc):

    try:

        obj = notes.objects.get(id=abc)

        if request.method == 'POST':

            obj.delete()

            messages.success(
                request,
                'Python question deleted successfully!'
            )

        return redirect('multiple')

    except notes.DoesNotExist:

        return HttpResponse('Record not found')


def update_html(request, abc):

    try:

        obj = HtmlNotes.objects.get(id=abc)

        if request.method == 'POST':

            question = request.POST.get('question')
            answer = request.POST.get('answer')

            if question and answer:

                obj.question = question
                obj.answer = answer
                obj.save()

                messages.success(
                    request,
                    'HTML note updated successfully!'
                )

                return redirect('html')

            else:

                messages.error(
                    request,
                    'Please fill in all fields.'
                )

        return render(
            request,
            'update.html',
            {'i': obj, 'category': 'html'}
        )

    except HtmlNotes.DoesNotExist:

        return HttpResponse('Record not found')



def delete_html(request, abc):

    try:

        obj = HtmlNotes.objects.get(id=abc)

        if request.method == 'POST':

            obj.delete()

            messages.success(
                request,
                'HTML question deleted successfully!'
            )

        return redirect('html')

    except HtmlNotes.DoesNotExist:

        return HttpResponse('Record not found')



def update_css(request, abc):

    try:

        obj = CssNotes.objects.get(id=abc)

        if request.method == 'POST':

            question = request.POST.get('question')
            answer = request.POST.get('answer')

            if question and answer:

                obj.question = question
                obj.answer = answer
                obj.save()

                messages.success(
                    request,
                    'CSS note updated successfully!'
                )

                return redirect('css')

            else:

                messages.error(
                    request,
                    'Please fill in all fields.'
                )

        return render(
            request,
            'update.html',
            {'i': obj, 'category': 'css'}
        )

    except CssNotes.DoesNotExist:

        return HttpResponse('Record not found')



def delete_css(request, abc):

    try:

        obj = CssNotes.objects.get(id=abc)

        if request.method == 'POST':

            obj.delete()

            messages.success(
                request,
                'CSS question deleted successfully!'
            )

        return redirect('css')

    except CssNotes.DoesNotExist:

        return HttpResponse('Record not found')


def update_javascript(request, abc):

    try:

        obj = JsNotes.objects.get(id=abc)

        if request.method == 'POST':

            question = request.POST.get('question')
            answer = request.POST.get('answer')

            if question and answer:

                obj.question = question
                obj.answer = answer
                obj.save()

                messages.success(
                    request,
                    'JavaScript note updated successfully!'
                )

                return redirect('javascript')

            else:

                messages.error(
                    request,
                    'Please fill in all fields.'
                )

        return render(
            request,
            'update.html',
            {'i': obj, 'category': 'javascript'}
        )

    except JsNotes.DoesNotExist:

        return HttpResponse('Record not found')


def delete_javascript(request, abc):

    try:

        obj = JsNotes.objects.get(id=abc)

        if request.method == 'POST':

            obj.delete()

            messages.success(
                request,
                'JavaScript question deleted successfully!'
            )

        return redirect('javascript')

    except JsNotes.DoesNotExist:

        return HttpResponse('Record not found')