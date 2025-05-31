# Flask CI/CD with Docker Project

A modern Flask web application with CI/CD pipeline and Docker containerization.

## 🚀 Features

- **Flask Web Application**
  - Modern Bootstrap UI
  - Health check endpoints
  - Error handling
  - Logging system
  - Static file serving
  - Template rendering

- **CI/CD Pipeline**
  - Automated testing
  - Code linting (Flake8)
  - Docker image building
  - GitHub Actions workflow
  - Code quality checks

- **Docker Integration**
  - Containerized application
  - Multi-stage builds
  - Production-ready configuration
  - Easy deployment
  - Port mapping (5001)

## 📋 Prerequisites

- Python 3.8+
- Docker Desktop
- Git
- GitHub account
- Docker Hub account

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-ci-cd.git
   cd flask-ci-cd
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   python app.py
   ```
   Visit: http://localhost:5001 or http://127.0.0.1:5001

4. **Run with Docker**
   ```bash
   # Build the image
   docker build -t flask-app:latest .

   # Run the container
   docker run -d -p 5001:5001 --name flask-container flask-app:latest
   ```

## 📁 Project Structure

```
flask-ci-cd/
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline configuration
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── js/
│       └── main.js         # Frontend JavaScript
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Homepage
│   ├── health.html        # Health check page
│   └── error.html         # Error pages
├── app.py                 # Main Flask application
├── test_app.py           # Unit tests
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md           # Project documentation
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

1. **Build and Test**
   - Runs on every push
   - Executes unit tests
   - Performs code linting (Flake8)
   - Checks code style
   - Validates Python syntax

2. **Docker Build and Push**
   - Triggers on main branch
   - Builds Docker image
   - Pushes to Docker Hub
   - Tags with commit hash

## 🐳 Docker Usage

1. **Build Image**
   ```bash
   docker build -t flask-app:latest .
   ```

2. **Run Container**
   ```bash
   docker run -d -p 5001:5001 --name flask-container flask-app:latest
   ```

3. **View Logs**
   ```bash
   docker logs flask-container
   ```

4. **Stop Container**
   ```bash
   docker stop flask-container
   ```

## 🌐 Available Endpoints

- `GET /`: Homepage with welcome message
- `GET /health`: Health check page with status
- `GET /api/health`: Health check API (JSON response)
- Error handlers for 404 and 500 status codes

## 🔧 Development

1. **Local Development**
   ```bash
   python app.py
   ```

2. **Run Tests**
   ```bash
   python -m pytest
   ```

3. **Code Linting**
   ```bash
   flake8 .
   ```

## 📝 Latest Updates

- Fixed Flake8 code style issues
- Improved Flask app initialization
- Enhanced static file serving
- Added comprehensive logging
- Updated Docker configuration
- Improved error handling
- Added health check endpoints
- Modernized UI with Bootstrap
- Added CI/CD pipeline
- Updated documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Flask Documentation
- Docker Documentation
- GitHub Actions Documentation
- Bootstrap Documentation