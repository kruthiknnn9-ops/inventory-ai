# Inventory AI – AI Integration & Testing

**Author:** Kruthik Nagendra  
**GitHub:** https://github.com/kruthiknnn9-ops

## Project Overview
An academic/demo Inventory AI application demonstrating two responsibilities:

1. **AI Integration** – connecting inventory data, machine-learning components, REST APIs and business rules.
2. **Testing** – validating AI outputs, API behavior, edge cases and business logic.

## AI Features
- 7-day demand forecasting
- Stockout-risk detection
- Reorder recommendation
- Sales anomaly detection
- Dashboard/API integration

## Architecture
Inventory Data → Flask REST API → AI Integration Layer → Forecast/Anomaly Models → Business Rules → Dashboard

## Testing
Automated tests cover:
- Normal/high-stock scenario
- Low-stock scenario
- Zero-stock scenario
- Unknown product
- Forecast output validation
- Inventory API
- Prediction API
- Invalid API request
- Anomaly output

Run tests with:

```bash
pytest -q
```

## Run the application

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python backend/app.py
```

Open `http://127.0.0.1:5000`.

## GitHub
Create a repository named `inventory-ai` under the GitHub account `kruthiknnn9-ops`, then push this project.

**Security:** Do not commit API keys, passwords, tokens or real `.env` files.
