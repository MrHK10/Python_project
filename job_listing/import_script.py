# import_data.py
import os
import django
import pandas as pd
from django.utils import timezone

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_listing.settings')

# Initialize Django
django.setup()

from django.conf import settings
from listing_jobs.models import JobListing

def import_data_from_excel(file_path):
    # Read data from Excel file
    df = pd.read_excel(file_path)
    
    # Filter DataFrame columns based on JobListing model fields
    model_fields = [field.name for field in JobListing._meta.fields]
    df = df[[col for col in df.columns if col in model_fields]]
    
    # Iterate over rows and create instances of JobListing
    for index, row in df.iterrows():
        # Create dictionary to hold valid fields
        valid_fields = {}
        for field in model_fields:
            # Check if the field is in the DataFrame and is not null or NaN
            if field in row and not pd.isnull(row[field]):
                valid_fields[field] = row[field]
        
        # Check if date_job_post is provided
        if 'date_job_post' not in valid_fields:
            # If date_job_post is not provided, set it to the current date
            valid_fields['date_job_post'] = timezone.now().date()
        
        # Create instance of JobListing with valid fields
        JobListing.objects.create(**valid_fields)

def main():
    # Path to your Excel file
    excel_file_path = 'indeed_20240122.144303.xlsx'
    
    # Import data from Excel
    import_data_from_excel(excel_file_path)

if __name__ == "__main__":
    main()
    
