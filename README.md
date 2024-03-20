git clone [<repository_url>](https://github.com/Dhruvanshu1775/company-task.git)

# Navigate to the project directory
cd <project_directory>

# Create and activate a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # On Linux/macOS
env\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

## run command
python manage.py migrate

python manage.py runserver 

## check api
localhost:8000/insert/

1. add file of csv and send that in post request
2. check value by using get api
