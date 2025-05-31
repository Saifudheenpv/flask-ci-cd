Flask CI/CD and Docker Project

This project demonstrates a simple Flask web application with a CI/CD pipeline using GitHub Actions and containerization using Docker. The pipeline automates linting (Flake8) and unit testing (pytest) on every push to the main branch. The app is containerized and pushed to Docker Hub.

Features





Flask web app with a single endpoint (/).



Unit tests using pytest.



Linting with Flake8 to enforce code quality.



GitHub Actions workflow for continuous integration.



Dockerized Flask app with a Dockerfile.



Docker image hosted on Docker Hub.

Prerequisites





Python 3.8+



Git



Docker Desktop



GitHub account



Docker Hub account

Setup Instructions

Run Locally (Without Docker)





Clone the repository:

git clone https://github.com/your-username/flask-ci-cd.git
cd flask-ci-cd



Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate



Install dependencies:

pip install -r requirements.txt



Run the Flask app:

python app.py

Open http://127.0.0.1:5000/ in your browser to see "Hello, DevOps World!".



Run tests:

pytest



Run linting:

flake8 app.py test_app.py

Run with Docker





Ensure Docker Desktop is running.



Build the Docker image:

docker build -t flask-app .



Run the container:

docker run -p 5000:5000 flask-app

Open http://127.0.0.1:5000/ in your browser.



Pull the image from Docker Hub:

docker pull yourusername/flask-app:latest

Replace yourusername with your Docker Hub username.

CI/CD Pipeline

The GitHub Actions workflow (.github/workflows/ci.yml) runs on every push or pull request to the main branch. It:





Sets up Python 3.8.



Installs dependencies from requirements.txt.



Runs Flake8 for linting.



Executes pytest for unit tests.

Docker Details





The Dockerfile builds a lightweight Python 3.8 image with the Flask app.



The image is pushed to Docker Hub: yourusername/flask-app.



.dockerignore excludes unnecessary files to optimize the build.

Challenges Faced





Learned to configure GitHub Actions for Python projects.



Ensured proper virtual environment setup on Windows.



Fixed Flake8 warnings to improve code quality.



Learned Docker commands and Dockerfile syntax.



Resolved Windows-specific Docker Desktop setup issues.

Future Improvements





Add more endpoints to the Flask app.



Integrate a deployment step (e.g., deploy to Heroku or AWS).



Add Docker Compose for multi-container setups.



Add code coverage reporting with Coveralls.

Author





Your Name (link to your GitHub profile)