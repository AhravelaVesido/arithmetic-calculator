# Arithmetic Calculator

A web-based arithmetic calculator built with **Python** and **Flask**, deployed live on Render.

🔗 **Live demo:** https://arithmetic-calculator-rd6u.onrender.com/

## Overview

This project handles the four basic arithmetic operations through a clean, responsive web interface. It was built as a foundational Flask project to practice backend request handling, input validation, and deploying a Python web app to a live production environment.

## Features

- Addition, subtraction, multiplication, and division of two numbers
- Graceful error handling for division by zero (no crashes, clear user-facing message)
- Responsive design that works on both mobile and desktop
- Clean, electric cyan UI theme

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render (via Procfile + Gunicorn)

## How to Run Locally

```bash
git clone https://github.com/AhravelaVesido/arithmetic-calculator.git
cd arithmetic-calculator
python -m venv venv
.\venv\Scripts\activate      # on Windows
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## What I Learned

Building this project reinforced core Flask routing and request-handling patterns, and was my first experience taking a Python web app from local development through to a live Render deployment.

## Author

**Ahravela D. Vesido** — Licensed Electronics Engineer (ECE, ECT)
[Portfolio](https://vesido-ahravela-portfolio.vercel.app/) · [GitHub](https://github.com/AhravelaVesido)
