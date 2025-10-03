#!/usr/bin/env python3
"""
PythonAnywhere deployment preparation script for Django Local Library project.
Run this script before uploading to PythonAnywhere.
"""

import os
import sys
import subprocess


def run_command(command, description):
    """Run a command and print the result."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main deployment preparation function for PythonAnywhere."""
    print("🚀 Django Local Library - PythonAnywhere Deployment Preparation")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("✗ Error: manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Create logs directory
    os.makedirs('logs', exist_ok=True)
    print("✓ Created logs directory")
    
    # Update .env for PythonAnywhere
    print("\n📝 PythonAnywhere Configuration:")
    print("Make sure to update your .env file with:")
    print("  - ALLOWED_HOSTS=yourusername.pythonanywhere.com")
    print("  - DEBUG=False")
    print("  - Database credentials for MySQL")
    
    # Run Django checks
    print("\n🔍 Running Django deployment checks...")
    try:
        result = subprocess.run(['python3', 'manage.py', 'check', '--deploy'], 
                              capture_output=True, text=True, check=True)
        print("✓ Django deployment checks passed")
    except subprocess.CalledProcessError as e:
        print("✗ Django deployment checks failed")
        print("Please fix the issues above before deploying")
        return False
    
    # Collect static files
    if not run_command('python3 manage.py collectstatic --noinput', 'Collecting static files'):
        return False
    
    # Run migrations (if database is available)
    print("\n📊 Database preparation:")
    print("Note: You'll need to run migrations on PythonAnywhere after setting up the database")
    
    print("\n🎉 PythonAnywhere deployment preparation completed!")
    print("\nNext steps:")
    print("1. Create PythonAnywhere account at https://www.pythonanywhere.com/")
    print("2. Upload your project code")
    print("3. Set up virtual environment and install requirements")
    print("4. Create MySQL database")
    print("5. Configure web app with WSGI file")
    print("6. Set up static files mapping")
    print("7. Run migrations and create superuser")
    print("8. Test your deployed site")
    
    print("\n📋 Files to check before upload:")
    print("  - .env (update with your PythonAnywhere credentials)")
    print("  - requirements.txt (includes mysqlclient)")
    print("  - wsgi.py (ready for PythonAnywhere)")
    print("  - locallibrary/settings_pythonanywhere.py (production settings)")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
