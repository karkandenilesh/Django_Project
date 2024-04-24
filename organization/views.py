from django.shortcuts import render, redirect
from .models import Organization, Profile
import csv
from .forms import CSVUploadForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrganizationSerializer
from .filters import OrganizationFilter
from rest_framework import filters
from rest_framework import generics
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect


# Create your views here.


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')

def query(request):
    organizations = Organization.objects.all()
    return render(request, 'query.html', {'organizations': organizations})
    # return render(request, 'query.html')

# def user(request):
#     return render(request, 'user.html')

# def upload_csv(request):
#     if request.method == 'POST':
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['csv_file']
#             if not csv_file.name.endswith('.csv'):
#                 return render(request, 'upload_csv.html', {'form': form, 'error': 'Please upload a CSV file.'})

#             # Process CSV file
#             decoded_file = csv_file.read().decode('utf-8').splitlines()
#             reader = csv.DictReader(decoded_file)
#             for row in reader:
#                 Organization.objects.create(
#                     id=row['id'],
#                     name=row['name'],
#                     domain=row['domain'],
#                     year_founded=row['year_founded'],
#                     industry=row['industry'],
#                     size_range=row['size_range'],
#                     locality=row['locality'],
#                     country=row['country'],
#                     linkedin_url=row['linkedin_url'],
#                     current_employee_estimate=row['current_employee_estimate'],
#                     total_employee_estimate=row['total_employee_estimate']
#                 )
#             return render(request, 'upload_csv.html', {'form': form, 'success': 'CSV file uploaded successfully.'})
#     else:
#         form = CSVUploadForm()
#     return render(request, 'upload_csv.html', {'form': form})


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                return render(request, 'upload_csv.html', {'form': form, 'error': 'Please upload a CSV file.'})

            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    Organization.objects.create(
                        id=row.get('id', ''),
                        name=row.get('name', ''),
                        domain=row.get('domain', ''),
                        year_founded=row.get('year_founded', 1900),  # Handle missing field gracefully
                        industry=row.get('industry', ''),
                        size_range=row.get('size_range', ''),
                        locality=row.get('locality', ''),
                        country=row.get('country', ''),
                        linkedin_url=row.get('linkedin_url', ''),
                        current_employee_estimate=row.get('current_employee_estimate', 10000),
                        total_employee_estimate=row.get('total_employee_estimate', 10000)
                    )
                return render(request, 'upload.html', {'form': form, 'success': 'CSV file uploaded successfully.'})
            except KeyError as e:
                error_message = f'Missing field in CSV file: {e}'
                return render(request, 'upload.html', {'form': form, 'error': error_message})

    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})



def filter_organizations(request):
    filtered_count = None  # Initialize filtered_count variable outside of if block

    if request.method == 'POST':
        name = request.POST.get('name')
        domain = request.POST.get('domain')
        year_founded = request.POST.get('year_founded')
        industry = request.POST.get('industry')
        size_range = request.POST.get('size_range')
        locality = request.POST.get('locality')
        country = request.POST.get('country')

        # Filter organizations based on form input
        organizations = Organization.objects.all()
        if name:
            organizations = organizations.filter(name__icontains=name)
        if domain:
            organizations = organizations.filter(domain__icontains=domain)
        if year_founded:
            organizations = organizations.filter(year_founded=year_founded)
        if industry:
            organizations = organizations.filter(industry__icontains=industry)
        if size_range:
            organizations = organizations.filter(size_range__icontains=size_range)
        if locality:
            organizations = organizations.filter(locality__icontains=locality)
        if country:
            organizations = organizations.filter(country__icontains=country)

        filtered_count = organizations.count()

        return render(request, 'queryfilter.html', {'organizations': organizations, 'filtered_count': filtered_count})

    else:
        return render(request, 'queryfilter.html', {'organizations': [], 'filtered_count' : filtered_count})


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



# class FilterOrganizationsAPIView(APIView):
#     def post(self, request):
#         name = request.data.get('name')
#         domain = request.data.get('domain')
#         year_founded = request.data.get('year_founded')
#         industry = request.data.get('industry')
#         size_range = request.data.get('size_range')
#         locality = request.data.get('locality')
#         country = request.data.get('country')

#         organizations = Organization.objects.all()
#         if name:
#             organizations = organizations.filter(name__contains=name)
#             print(organizations)
#         if domain:
#             organizations = organizations.filter(domain__icontains=domain)
#         if year_founded:
#             organizations = organizations.filter(year_founded=year_founded)
#         if industry:
#             organizations = organizations.filter(industry__icontains=industry)
#         if size_range:
#             organizations = organizations.filter(size_range__icontains=size_range)
#         if locality:
#             organizations = organizations.filter(locality__icontains=locality)
#         if country:
#             organizations = organizations.filter(country__icontains=country)

#         serializer = OrganizationSerializer(organizations, many=True)
#         return Response({
#             'organizations': serializer.data,
#             'filtered_count': organizations.count()
#         })


# class FilterOrganizationsAPIView(APIView):
#     def post(self, request):
#         filter_data = request.data

#         # Apply filters
#         organization_filter = OrganizationFilter(filter_data, queryset=Organization.objects.all())
#         filtered_organizations = organization_filter.qs

#         serializer = OrganizationSerializer(filtered_organizations, many=True)
#         return Response({
#             'organizations': serializer.data,
#             'filtered_count': filtered_organizations.count()
#         })


# class FilterOrganizationsAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = OrganizationSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']


# class FilterOrganizationsAPIView(generics.ListAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     filterset_class = OrganizationFilter

# class FilterOrganizations(generics.ListAPIView):
#     serializer_class = OrganizationSerializer

#     def get_queryset(self):
#         name = self.request.query_params.get('name', None)
#         count = name.count()
#         return Organization.objects.filter(name=name)


# class FilterOrganizations(generics.ListAPIView):
#     serializer_class = OrganizationSerializer

#     def get_queryset(self):
#         queryset = Organization.objects.all()
        
#         # Filtering based on query parameters
#         name = self.request.query_params.get('name', None)
#         if name:
#             queryset = queryset.filter(name__icontains=name)
        
#         domain = self.request.query_params.get('domain', None)
#         if domain:
#             queryset = queryset.filter(domain__icontains=domain)
        
#         industry = self.request.query_params.get('industry', None)
#         if industry:
#             queryset = queryset.filter(industry__icontains=industry)
        
#         # Add more fields for filtering as needed
        
#         # Aggregating count
#         count = queryset.aggregate(total=Count('id'))
#         total_count = count['total']

#         return queryset, total_count


class FilterOrganizations(generics.ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        queryset = Organization.objects.all()
        
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
    

def delete_user(request, user_id):
    # Retrieve the user object to be deleted
    user = get_object_or_404(User, id=user_id)

    # Check if the request method is POST (since delete actions should typically be performed via POST)
    if request.method == 'POST':
        # Delete the user
        user.delete()
        # Redirect to a success page or another appropriate URL
        return redirect('user_list')