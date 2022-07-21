from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Adddata
from Instaworkapp.forms import AddForm


# Create your views here.

class AdddataListView(ListView):
    model = Adddata
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['nobjects'] = self.get_queryset().count()
        return context

class AdddataCreateView(CreateView):
    model = Adddata
    form_class = AddForm
    # fields = ['firstname', 'lastname', 'email', 'phoneNumber', 'role']
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class AdddataUpdateView(UpdateView):
    template_name = 'Instaworkapp/update.html'
    form_class = AddForm
    # fields = ['id']
    queryset = Adddata.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Adddata, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class AdddataDeleteView(DeleteView):
    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Adddata, id=id)

    def get_success_url(self):
        return reverse("Instaworkapp:listview")
#
# def addview(request):
#     addform = AddForm()
#     if request.method == 'POST':
#         # print(request.POST)
#         addform = AddForm(request.POST)
#         if addform.is_valid():
#             addform.save()
#             print("success")
#             return redirect('Instaworkapp:listview')
#     return render(request, 'Instaworkapp/adddata_form.html', {'addform': addform})
#
# def editview(request, id):
#     data = Adddata.objects.get(id=id)
#     editform = AddForm(instance=data)
#
#     if request.method == 'POST':
#         editform = AddForm(request.POST, instance=data)
#         if editform.is_valid():
#             editform.save()
#             return redirect('Instaworkapp:listview')
#         else:
#             print(editform.errors.as_data())
#             # raise forms.ValidationError(editform.errors)
#
#     return render(request, 'Instaworkapp/editmembers.html', {'editform': editform, 'data': data, 'error': editform.errors.as_data()})
#
# def deleteview(request, id):
#     data= Adddata.objects.get(id=id)
#     if request.method == 'POST':
#         data.delete()
#         return redirect('Instaworkapp:listview')
#     return render(request, 'Instaworkapp/adddata_confirm_delete.html', {'data': data})
