from django.shortcuts import render,redirect

# Create your views here.


from .models import CompanyModel

from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView

class CompanyListView(ListView):
    model = CompanyModel


#it display all unique company names
class CompanyListView2(ListView):
    model = CompanyModel
    template_name = 'testapp/compName.html'
    context_object_name = 'compName'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unique_company_names = set(CompanyModel.objects.values_list('company', flat=True))
        context['compName'] = unique_company_names
        return context


# it display only  employee names based on company

class CompanyEmployeeView(ListView):
    model = CompanyModel
    template_name = 'testapp/company_detail.html'
    context_object_name = 'employees'


    def get_queryset(self):

        company_name = self.kwargs.get('company')
        #queryset = super().get_queryset()
        #return queryset.filter(company=company_name)

        return CompanyModel.objects.filter(company=company_name)



# it display all details of employee
class CompanyDetailView(DetailView):
    model = CompanyModel


#it create new form

class CompanyCreateView(CreateView):
    model = CompanyModel
    fields='__all__'

#update data

class CompanyUpdateView(UpdateView):
    model = CompanyModel
    fields='__all__'


#delete employee

from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = CompanyModel
    success_url= reverse_lazy('comp_list')
