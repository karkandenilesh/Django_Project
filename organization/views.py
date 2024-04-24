from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization, Profile

import csv
from .forms import CSVUploadForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrganizationSerializer
from rest_framework import generics
from django.db.models import Count
from django.db import IntegrityError


# Create your views here.


def upload(request):
    return render(request, 'upload.html')

def query(request):
    organizations = Organization.objects.all()
    return render(request, 'query.html', {'organizations': organizations})




def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                return render(request, 'upload.html', {'form': form, 'error': 'Please upload a CSV file.'})

            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    try:
                        Organization.objects.create(
                            id=row.get('id'),
                            name=row.get('name'),
                            domain=row.get('domain'),
                            year_founded=row.get('year founded'),
                            industry=row.get('industry'),
                            size_range=row.get('size range'),
                            locality=row.get('locality'),
                            country=row.get('country'),
                            linkedin_url=row.get('linkedin url'),
                            current_employee_estimate=row.get('current employee estimate'),
                            total_employee_estimate=row.get('total employee estimate')
                        )
                    except IntegrityError:
                        return render(request, 'upload.html', {'form': form, 'error': 'ID duplication found in the uploaded file. ID must be unique.'})

                return render(request, 'upload.html', {'form': form, 'success': 'CSV file uploaded successfully.'})
            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': f'Something went wrong: {e}'})
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})




def filter_organizations(request):
    return render(request, 'queryfilter.html')


class FilterOrganizations(generics.ListAPIView):

    serializer_class = OrganizationSerializer

    def get_queryset(self):
        queryset = Organization.objects.all()
        print("***",queryset)
        
        # Filtering based on query parameters
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        domain = self.request.query_params.get('domain', None)
        if domain:
            queryset = queryset.filter(domain__icontains=domain)
        
        industry = self.request.query_params.get('industry', None)
        if industry:
            queryset = queryset.filter(industry__icontains=industry)
        
        year_founded = self.request.query_params.get('year_founded', None)
        if year_founded:
            queryset = queryset.filter(year_founded__icontains=year_founded)

        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country__icontains=country)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Aggregating count
        count = queryset.aggregate(total=Count('id'))
        total_count = count['total']

        serializer = self.get_serializer(queryset, many=True)

        return Response({'organizations': serializer.data, 'filtered_count': total_count})



def user_list(request):
    users = User.objects.all()
    print(users)
    return render(request, 'user.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')



