import os
import django
import datetime
import sys
from django.core.files import File

# Get the absolute path to the project root
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_script_dir)  # Go up from data_migration to project root

# Add project root to Python path
sys.path.insert(0, project_root)

# Set the CORRECT Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cd_spec_viewer_web.settings')

# Now setup Django
django.setup()

from cdspec.models import SpecRun
from cdspec.util import handle_file_upload

def migrate_csv_files():
    # CSV files are in the same directory as this script
    data_folder = current_script_dir
    
    files_metadata = [
        {
            'file_path': os.path.join(data_folder, '20_roundup_no_cap.csv'),
            'run_title': 'Roundup No Cap - 03/09/2020',
            'run_description': 'CD spectroscopy scan from 500-185nm',
            'run_user': 'Lab Researcher',
            'protein_concentration': 0.1,
            'pathlength': 0.1,
            'number_of_amino_acids': 100,
            'visible_student': True,
            'visible_public': True
        },
        {
            'file_path': os.path.join(data_folder, 'Taq_stock_test_12-14-2020.csv'),
            'run_title': 'Taq Stock Test - 12/14/2020',
            'run_description': 'Temperature melt curve of Taq polymerase',
            'run_user': 'Lab Researcher',
            'protein_concentration': 0.1,
            'pathlength': 0.1,
            'number_of_amino_acids': 830,
            'visible_student': True,
            'visible_public': True
        },
        {
            'file_path': os.path.join(data_folder, '201028_buffer_test-2_1_OYA9NlT.csv'),
            'run_title': 'Buffer Test HEPES - 10/28/2020',
            'run_description': 'Buffer test with HEPES buffer solution',
            'run_user': 'Lab Researcher',
            'protein_concentration': 0.0,
            'pathlength': 0.1,
            'number_of_amino_acids': 0,
            'visible_student': True,
            'visible_public': True
        }
    ]
    
    for metadata in files_metadata:
        try:
            file_path = metadata['file_path']
            print(f"📁 Processing: {os.path.basename(file_path)}")
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue
            
            # Read and parse the CSV file
            with open(file_path, 'rb') as csv_file:
                parsed_data = handle_file_upload(csv_file)
            
            # Create SpecRun object
            spec_run = SpecRun(
                run_title=metadata['run_title'],
                run_description=metadata['run_description'],
                run_user=metadata['run_user'],
                protein_concentration=metadata['protein_concentration'],
                pathlength=metadata['pathlength'],
                number_of_amino_acids=metadata['number_of_amino_acids'],
                visible_student=metadata['visible_student'],
                visible_public=metadata['visible_public'],
                
                # Data from parsed CSV
                data=parsed_data['data'],
                data_points=parsed_data['header']['NPOINTS'],
                x_units=parsed_data['header'].get('XUNITS'),
                y_units=parsed_data['header'].get('YUNITS'),
                y2_units=parsed_data['header'].get('Y2UNITS'),
                y3_units=parsed_data['header'].get('Y3UNITS'),
                
                # Run date from CSV header
                run_date=datetime.datetime.strptime(
                    f"{parsed_data['header']['DATE']} {parsed_data['header']['TIME']}", 
                    "%y/%m/%d %H:%M:%S"
                )
            )
            
            # Save the object
            spec_run.save()
            
            # Save the source file
            with open(file_path, 'rb') as source_file:
                spec_run.source_file.save(
                    os.path.basename(file_path),
                    File(source_file)
                )
            
            print(f"✅ Successfully migrated: {os.path.basename(file_path)} (ID: {spec_run.id})")
            
        except Exception as e:
            print(f"❌ Error migrating {os.path.basename(metadata['file_path'])}: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Starting migration...")
    print(f"📂 Project root: {project_root}")
    print(f"📂 Script location: {current_script_dir}")
    migrate_csv_files()
    print("🎉 Migration complete!")