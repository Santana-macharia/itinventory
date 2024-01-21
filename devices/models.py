# models.py
from django.db import models
from datetime import datetime


class Import(models.Model):
    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    centre = models.CharField(max_length=500, blank=True, null=True)
    department = models.CharField(max_length=500, blank=True, null=True)
    hardware = models.CharField(max_length=500, blank=True, null=True)
    system_model = models.CharField(max_length=500, blank=True, null=True)
    # device_name = models.CharField(max_length=500, blank=True, null=True)
    processor = models.CharField(max_length=500, blank=True, null=True)
    ram_gb = models.CharField(max_length=500, blank=True, null=True)
    hdd_gb = models.CharField(max_length=500, blank=True, null=True)
    serial_number = models.CharField(max_length=500, blank=True, null=True)
    # assigned_by = models.CharField(max_length=500, blank=True, null=True)
    assignee_first_name = models.CharField(max_length=500, blank=True, null=True)
    assignee_last_name = models.CharField(max_length=500, blank=True, null=True)
    assignee_email_address = models.CharField(max_length=500, blank=True, null=True)
    device_condition = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    

    def save(self, *args, **kwargs):
        if self.file:
            # Read the CSV file and store its content in model fields
            csv_data = self.file.read().decode('utf-8').splitlines()

            # Assuming the first row contains headers
            headers = csv_data[0].split(',')

            for row in csv_data[1:]:
                values = row.split(',')
                import_instance = Import()

                for header, value in zip(headers, values):
                    value = value.strip()

                   # Convert date values to 'YYYY-MM-DD' format
                    if 'date' in header.lower():
                        if value:
                            try:
                                date_value = datetime.strptime(value, '%Y-%m-%d').date()
                                setattr(import_instance, header, date_value)
                            except ValueError:
                                # Handle invalid date format here
                                print(f"Invalid date format: {value}")
                                continue
                        else:
                            setattr(import_instance, header, None)
                    else:
                        setattr(import_instance, header, value)

                import_instance.save()

        super().save(*args, **kwargs)

    @property
    def display_field(self):
        return self.assignee_email_address
    

# Register the model with the custom admin class

class Report(models.Model):
    def __str__(self):
        return "Report"

   




   
   
   

        

