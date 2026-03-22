# Battery Health Prediction System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated web-based application built with Flask for predicting battery State of Health (SOH) and Remaining Useful Life (RUL) using advanced machine learning models. This system provides accurate battery diagnostics through an intuitive user interface, supporting data-driven decision-making for battery management and maintenance.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Model Details](#model-details)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Secure registration and login system with session management
- **Machine Learning Predictions**: Real-time SOH and RUL predictions using trained ML models
- **Web Interface**: Responsive Flask-based web application with HTML templates
- **Data Processing**: Automated feature scaling and encoding for accurate predictions
- **Session Management**: Persistent user sessions with logout functionality
- **Error Handling**: Comprehensive flash messaging for user feedback

## Architecture

The application follows a modular Flask architecture:

```
battery-prediction-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── home.html
│   ├── user_registration.html
│   ├── user_login.html
│   ├── index.html
│   ├── predict.html
│   └── result.html
├── static/                # CSS, JS, images (if applicable)
├── models/                # ML model files
│   ├── soh_model.pkl
│   ├── rul_model.pkl
│   ├── scaler.pkl
│   └── battery_le.pkl
├── Battery_dataset.csv    # Training dataset
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd battery-health-prediction
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Model Files**
   Ensure the following model files are present in the root directory:
   - `soh_model.pkl` - State of Health prediction model
   - `rul_model.pkl` - Remaining Useful Life prediction model
   - `scaler.pkl` - Feature scaler
   - `battery_le.pkl` - Battery ID label encoder

## Configuration

The application uses the following configuration:

- **Secret Key**: Change `app.secret_key` in `app.py` for production deployment
- **Debug Mode**: Set `debug=False` in production
- **Model Paths**: Update model file paths if stored in different locations

## Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   Open your browser and navigate to: `http://127.0.0.1:5000`

3. **User Workflow**
   - Visit the home page
   - Register a new account or login
   - Access the dashboard
   - Navigate to the prediction page
   - Enter battery parameters
   - View prediction results

## API Reference

### Routes

- `GET /` - Home page
- `GET/POST /user_registration` - User registration
- `GET/POST /user_login` - User login
- `GET /index` - User dashboard (requires authentication)
- `GET/POST /predict` - Battery prediction (requires authentication)
- `GET /logout` - User logout

### Prediction Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| battery_id | string | Unique battery identifier |
| cycle | float | Current cycle number |
| chI | float | Charge current |
| chV | float | Charge voltage |
| chT | float | Charge temperature |
| disI | float | Discharge current |
| disV | float | Discharge voltage |
| disT | float | Discharge temperature |
| BCt | float | Battery capacity test value |

## Model Details

### State of Health (SOH) Model
- Predicts the current health percentage of the battery
- Output: Percentage value (0-100%)

### Remaining Useful Life (RUL) Model
- Estimates the remaining operational cycles
- Output: Integer value representing cycles

### Preprocessing
- **Scaling**: StandardScaler for numerical features
- **Encoding**: LabelEncoder for battery ID categorical variable

## Testing

Run the test suite:

```bash
python test.py
```

Additional test files:
- `tested.py` - Unit tests
- `tested1.py` - Integration tests

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -am 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions, issues, or contributions:

- **Project Repository**: [GitHub Repository URL]
- **Issue Tracker**: [GitHub Issues URL]
- **Email**: [Your Email Address]

---

*Built with ❤️ using Flask and scikit-learn*