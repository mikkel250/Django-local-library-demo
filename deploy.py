#!/usr/bin/env python3
"""
Deployment script for Django Local Library project.
This script helps prepare the project for production deployment.
"""

import os
import sys
import subprocess
import django
from django.core.management import execute_from_command_line

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
    """Main deployment preparation function."""
    print("🚀 Django Local Library - Deployment Preparation")
    print("=" * 50)
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("✗ Error: manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Create logs directory
    os.makedirs('logs', exist_ok=True)
    print("✓ Created logs directory")
    
    # Run Django checks
    print("\n🔍 Running Django deployment checks...")
    try:
        execute_from_command_line(['manage.py', 'check', '--deploy'])
        print("✓ Django deployment checks passed")
    except SystemExit as e:
        if e.code != 0:
            print("✗ Django deployment checks failed")
            print("Please fix the issues above before deploying")
            return False
        else:
            print("✓ Django deployment checks passed")
    
    # Collect static files
    if not run_command('python3 manage.py collectstatic --noinput', 'Collecting static files'):
        return False
    
    # Run migrations
    if not run_command('python3 manage.py migrate', 'Running database migrations'):
        return False
    
    print("\n🎉 Deployment preparation completed successfully!")
    print("\nNext steps:")
    print("1. Set up your production environment variables")
    print("2. Configure your web server (nginx, Apache, etc.)")
    print("3. Set up your production database")
    print("4. Configure SSL/HTTPS")
    print("5. Deploy to your hosting platform")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
