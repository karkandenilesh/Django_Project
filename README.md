Catalyst Count Web Application
This web application is built using Django 3.x/4.x, Postgres, and Bootstrap 4/5. It allows users to perform various tasks such as login, upload CSV data, filter data, and view user information.

Setup Instructions
Clone Repository: Clone the repository from GitHub or Bitbucket.
Environment Setup: Set up the project environment with Python 3.x and Django 3.x/4.x.
Database Configuration: Configure the project with a PostgreSQL database.
Environment Variables: Securely configure environment variables using django-environ for sensitive information such as database credentials, secret keys, etc.
Authentication Configuration: Configure authentication via django-all-auth for user authentication and management.
Test Data Set: Download the test data set from the provided link: Test Data Set
UI Design: Create user interface (UI) using Bootstrap 4/5 to ensure a responsive and visually appealing design.
Pages
1. Login
Users can login using their credentials.
2. Upload Data
Users can upload a large volume CSV file (1GB) with a visual progress bar for tracking the upload progress.
The uploaded file's data will be stored in the PostgreSQL database.
3. Query Builder
Users can filter the data using a form.
Once the form is submitted, the application displays the count of records based on the applied filters.
4. Users
Users can view user information.
