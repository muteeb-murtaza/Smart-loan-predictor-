# Smart Loan Predictor API

A FastAPI-based web application that predicts loan approval using machine learning models.

## Project Structure

```
Smart_Loan_Predictor/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── schemas.py           # Pydantic models for request/response
│   ├── model_loader.py      # Load ML models from disk
│   └── prediction.py        # Prediction logic and risk assessment
├── models/
│   ├── random_forest_model.pkl    # Pre-trained Random Forest model
│   └── preprocessor.pkl           # Feature preprocessor (scaling/encoding)
├── static/
│   ├── index.html           # Frontend HTML
│   ├── style.css            # Frontend styling
│   └── script.js            # Frontend JavaScript
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Features

- 🎯 **ML-Based Predictions**: Uses Random Forest classifier for accurate loan approval predictions
- 💻 **FastAPI Backend**: Modern, fast Python web framework
- 🎨 **Interactive Frontend**: Beautiful, responsive web interface
- 📊 **Risk Assessment**: Calculates risk levels based on multiple factors
- 📈 **Probability Scoring**: Returns approval probability (0-1)
- ✅ **Input Validation**: Comprehensive validation for all input fields
- 🔄 **CORS Support**: Enables cross-origin requests

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or navigate to the project directory**:
   ```bash
   cd Smart_Loan_Predictor
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Place ML models**:
   - Add `random_forest_model.pkl` to the `models/` directory
   - Add `preprocessor.pkl` to the `models/` directory

## Usage

### Running the API Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Accessing the Web Interface

1. Open your browser and navigate to:
   ```
   http://localhost:8000/static/index.html
   ```

2. Fill in the loan application form with your details:
   - **Age**: 18-100 years
   - **Annual Income**: Dollar amount
   - **Credit Score**: 0-850
   - **Years of Employment**: Non-negative integer
   - **Existing Loans**: Number of current loans
   - **Loan Amount**: Requested loan amount in dollars

3. Click "Get Prediction" to receive the result

### API Endpoints

#### Health Check
```
GET /health
```
Returns: `{"status": "healthy"}`

#### Loan Prediction
```
POST /predict
Content-Type: application/json

Request Body:
{
  "age": 35,
  "income": 75000,
  "credit_score": 720,
  "employment_years": 5,
  "existing_loans": 1,
  "loan_amount": 25000
}

Response:
{
  "prediction": "Approved",
  "probability": 0.85,
  "risk_level": "Low",
  "recommendation": "Applicant is eligible for the requested loan amount with favorable terms."
}
```

#### Interactive API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Prediction Output

### Fields

- **prediction**: `"Approved"` or `"Rejected"` - The final prediction
- **probability**: `0.0-1.0` - Confidence level of the prediction
- **risk_level**: `"Low"`, `"Medium"`, or `"High"` - Assessed risk level
- **recommendation**: String message with actionable advice

### Risk Assessment Logic

The risk level is calculated based on:
- Credit Score
- Model Probability
- Number of Existing Loans
- Debt-to-Income Ratio

## Model Information

The system uses a pre-trained Random Forest classifier with the following features:
1. Age
2. Annual Income
3. Credit Score
4. Years of Employment
5. Number of Existing Loans
6. Requested Loan Amount

## Frontend Features

- ✨ Modern, gradient UI design
- 📱 Responsive design for mobile and desktop
- 🎯 Real-time form validation
- 🔄 Loading spinner during API calls
- ⚠️ Error handling with user-friendly messages
- 📊 Visual indicators for risk levels (🟢 Low, 🟡 Medium, 🔴 High)

## Development

### Project Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.104.1 | Web framework |
| uvicorn | 0.24.0 | ASGI server |
| pydantic | 2.5.0 | Data validation |
| scikit-learn | 1.3.2 | ML model and preprocessing |
| numpy | 1.24.3 | Numerical computing |

### Running Tests

(Test suite can be added here)

### Code Structure

- `app/main.py`: FastAPI application setup, CORS configuration, and endpoints
- `app/schemas.py`: Pydantic models for type-safe request/response handling
- `app/model_loader.py`: Model loading and error handling
- `app/prediction.py`: Core prediction logic and risk assessment algorithms

## Troubleshooting

### Models Not Found
If you see "Warning: Model file not found", ensure:
- Model files are in the `models/` directory
- File names match exactly: `random_forest_model.pkl` and `preprocessor.pkl`

### CORS Issues
If the frontend can't connect to the backend:
- Check that both are running (frontend on any port, backend on 8000)
- Ensure the API URL in `script.js` matches your backend URL

### Port Already in Use
If port 8000 is already in use:
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```
Then update the `API_BASE_URL` in `script.js` to the new port.

## Future Enhancements

- [ ] Database integration for loan history
- [ ] User authentication system
- [ ] Advanced analytics dashboard
- [ ] Model retraining pipeline
- [ ] Batch prediction API
- [ ] Email notifications
- [ ] Export prediction reports

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please refer to the project documentation or contact the development team.
