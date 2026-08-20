import os
import sys
import django
from datetime import date, timedelta
from pathlib import Path
from PIL import Image
import io

# Настройка окружения Django (вместо устаревшего setup_environ)
BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from employees.models import Employee, Skill, EmployeeImage, EmployeeSkill
from django.core.files.base import ContentFile

# Создаём навыки
python_skill, _ = Skill.objects.get_or_create(name='Python')
django_skill, _ = Skill.objects.get_or_create(name='Django')
testing_skill, _ = Skill.objects.get_or_create(name='Testing')

# Данные сотрудников
employees_data = [
    {'first_name': 'Анна', 'last_name': 'Петрова', 'gender': 'F', 'role': 'backend', 'desk': 1, 'days_ago': 5},
    {'first_name': 'Иван', 'last_name': 'Сидоров', 'gender': 'M', 'role': 'frontend', 'desk': 3, 'days_ago': 10},
    {'first_name': 'Елена', 'last_name': 'Козлова', 'gender': 'F', 'role': 'tester', 'desk': 5, 'days_ago': 3},
    {'first_name': 'Дмитрий', 'last_name': 'Волков', 'gender': 'M', 'role': 'backend', 'desk': 7, 'days_ago': 20},
]

for i, data in enumerate(employees_data):
    hire_date = date.today() - timedelta(days=data['days_ago'])

    # Создаём сотрудника (валидация соседства сработает здесь)
    emp = Employee.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        role=data['role'],
        desk_number=data['desk'],
        hire_date=hire_date,
    )

    # Привязываем навыки
    if data['role'] == 'backend':
        EmployeeSkill.objects.create(employee=emp, skill=python_skill, level='advanced')
        EmployeeSkill.objects.create(employee=emp, skill=django_skill, level='intermediate')
    elif data['role'] == 'frontend':
        EmployeeSkill.objects.create(employee=emp, skill=python_skill, level='beginner')
    else:
        EmployeeSkill.objects.create(employee=emp, skill=testing_skill, level='expert')

    # Генерируем фиктивное изображение (чтобы было фото в карточке)
    img = Image.new('RGB', (400, 300), color=(i * 50, 100, 200))
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG')
    EmployeeImage.objects.create(
        employee=emp,
        image=ContentFile(buffer.getvalue(), name=f'test_photo_{i}.jpg'),
        order=0
    )

    # Второе фото для галереи (будет в детальной карточке, но не как главное)
    img2 = Image.new('RGB', (300, 400), color=(200, i * 50, 100))
    buffer2 = io.BytesIO()
    img2.save(buffer2, format='JPEG')
    EmployeeImage.objects.create(
        employee=emp,
        image=ContentFile(buffer2.getvalue(), name=f'test_photo_2_{i}.jpg'),
        order=1
    )

print('Тестовые сотрудники и фото созданы.')
