import os
import subprocess
import shutil

def main():
    # Check if running in the correct virtual environment
    if 'VIRTUAL_ENV' not in os.environ:
        raise RuntimeError("This script must be run within the correct virtual environment.")
    
    # Install required packages via a temporary requirements file
    with open('temp_requirements.txt', 'w') as f:
        f.write('beautifulsoup4\npytest\n')
    
    try:
        subprocess.check_call(['pip', 'install', '-r', 'temp_requirements.txt'])
    finally:
        os.remove('temp_requirements.txt')  # Clean up temporary file
    
    # Display and save all installed packages
    installed = subprocess.check_output(['pip', 'freeze'], text=True)
    print(installed)
    
    with open('requirements.txt', 'w') as f:
        f.write(installed)
    
    # Archive the virtual environment
    env_path = os.environ['VIRTUAL_ENV']
    shutil.make_archive('venv_archive', 'zip', env_path)

if __name__ == '__main__':
    main()