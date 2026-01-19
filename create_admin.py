import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinecourse.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin if it exists
User.objects.filter(username='admin').delete()

# Create new superuser
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

print(f"Superuser created successfully!")
print(f"Username: admin")
print(f"Password: admin123")
print(f"Email: admin@example.com")
