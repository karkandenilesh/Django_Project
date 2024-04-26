Django Catalyst Count
This is a Django web application developed for managing organizations and users.


Features
-Upload CSV: Allows users to upload CSV files containing organization data.
-Filter Organizations: Provides a REST API endpoint to filter organizations based on various criteria.
-User Management: Allows users to view, add, and delete users.
-Authentication: Includes user authentication using Django's AllAuth library.
-Responsive Design: Ensures a responsive and user-friendly experience across devices.


Setup
1.Clone the Repository:https://github.com/karkandenilesh/Django_Project.git

2.Install Dependencies:pip install -r requirements.txt

3.Run Migrations:python manage.py migrate

4.python manage.py runserver


Usage
Upload CSV: Navigate to the Upload page and upload a CSV file containing organization data.
Filter Organizations: Use the Filter page to filter organizations based on name, domain, industry, etc.
User Management: Access the User page to manage users (add, view, delete).
REST API: The API endpoint for filtering organizations can be accessed at /api/filter-organizations/.

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

