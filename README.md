# Flask CI/CD and Docker Project 🚀

[![CI/CD](https://github.com/Saifudheenpv/flask-ci-cd/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/flask-ci-cd/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

A modern Flask web application showcasing CI/CD implementation using GitHub Actions and Docker containerization. This project demonstrates industry best practices for automated testing, linting, and containerization.

## ✨ Features

- 🌐 Flask web application with RESTful endpoints
- 🧪 Comprehensive unit testing suite using pytest
- 📝 Code quality enforcement with Flake8
- 🔄 Automated CI/CD pipeline using GitHub Actions
- 🐳 Docker containerization for consistent deployments
- 🚀 Automated Docker image publishing to Docker Hub

## 🛠️ Prerequisites

- Python 3.8 or higher
- Git
- Docker Desktop
- GitHub account
- Docker Hub account

## 🚀 Getting Started

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flask-ci-cd.git
   cd flask-ci-cd
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   Visit http://127.0.0.1:5000/ in your browser

5. **Run tests**
   ```bash
   pytest
   ```

6. **Run linting**
   ```bash
   flake8 app.py test_app.py
   ```

### 🐳 Docker Setup

1. **Build the image**
   ```bash
   docker build -t flask-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 flask-app
   ```

3. **Pull from Docker Hub**
   ```bash
   docker pull yourusername/flask-app:latest
   ```

## 🔄 CI/CD Pipeline

Our GitHub Actions workflow automatically:

- ✅ Sets up Python 3.8
- 📦 Installs project dependencies
- 🔍 Runs code quality checks with Flake8
- 🧪 Executes unit tests with pytest
- 🐳 Builds and pushes Docker image (on successful merge to main)

## 🏗️ Project Structure

```
flask-ci-cd/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## 💡 Lessons Learned

- Implementing GitHub Actions for Python projects
- Managing virtual environments across different platforms
- Writing clean, Flake8-compliant code
- Docker containerization best practices
- Cross-platform compatibility considerations

## 🚀 Future Enhancements

- [ ] Additional API endpoints and features
- [ ] Automated deployment to cloud platforms (AWS/Heroku)
- [ ] Docker Compose implementation for microservices
- [ ] Code coverage reporting with Coveralls
- [ ] API documentation with Swagger/OpenAPI

## 👤 Author

[Your Name](https://github.com/your-username)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
⭐ Found this project helpful? Please consider giving it a star!