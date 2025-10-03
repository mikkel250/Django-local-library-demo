# PythonAnywhere Quick Reference

## 🚀 Quick Deployment Checklist

### Before Upload:
- [ ] Update `.env` with your PythonAnywhere username
- [ ] Set `DEBUG=False` in `.env`
- [ ] Set `ALLOWED_HOSTS=yourusername.pythonanywhere.com`

### On PythonAnywhere:

#### 1. Upload & Setup
```bash
# Clone or upload your project
git clone https://github.com/yourusername/Django-local-library-demo.git
cd Django-local-library-demo

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Database Setup
```bash
# Create MySQL database in PythonAnywhere dashboard first
# Then run migrations
python manage.py migrate
python manage.py createsuperuser
```

#### 3. Web App Configuration
- **Virtualenv**: `/home/yourusername/env`
- **WSGI File**: Use the provided `wsgi.py`
- **Static Files**: 
  - URL: `/static/`
  - Directory: `/home/yourusername/Django-local-library-demo/staticfiles/`

#### 4. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

## 🔧 Key Files

### WSGI Configuration
```python
# In PythonAnywhere WSGI file
import os
import sys

path = '/home/yourusername/Django-local-library-demo'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings_pythonanywhere'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Environment Variables (.env)
```bash
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
DB_NAME=yourusername$locallibrary
DB_USER=yourusername
DB_PASSWORD=your_mysql_password
DB_HOST=yourusername.mysql.pythonanywhere-services.com
DB_PORT=3306
```

## 🐛 Common Issues

### Static Files Not Loading
- Check static file mappings in Web tab
- Ensure `collectstatic` was run
- Verify file permissions

### Database Connection Error
- Check database credentials
- Ensure MySQL client is installed: `pip install mysqlclient`
- Verify database exists in PythonAnywhere dashboard

### Import Errors
- Check virtual environment path
- Ensure all dependencies installed
- Verify Python path in WSGI file

## 📊 Free Plan Limits
- **CPU**: 100 seconds/day
- **Disk**: 1GB
- **Custom domains**: Not available
- **HTTPS**: Available (free SSL)

## 🔗 Useful Links
- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [Django on PythonAnywhere](https://help.pythonanywhere.com/pages/Django/)
- [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

## 📝 Commands Reference
```bash
# Check deployment readiness
python manage.py check --deploy

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Check logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log
```

Your Django Local Library is ready for PythonAnywhere! 🎉
