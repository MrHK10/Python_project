import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_listing.settings')

# Configure Django settings
django.setup()

from listing_jobs.models import JobListing

def delete_all_records():
    try:
        # Delete all records from YourModel
        JobListing.objects.all().delete()
        print("All records deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_all_records()
