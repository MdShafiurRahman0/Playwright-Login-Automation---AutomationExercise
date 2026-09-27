# Playwright Login Automation (Python + Pytest)

A professional web automation project built using **Python, Playwright, and Pytest**. This project automates the login functionality of the **Automation Exercise** website by following the **Page Object Model (POM)** design pattern.

**Repository:** https://github.com/MdShafiurRahman0/Playwright-Login-Automation---AutomationExercise

---

## Project Overview

This project automates the following user journey:

1. Launch the Automation Exercise website
2. Navigate to the Login page
3. Enter registered user credentials
4. Submit the login form
5. Verify successful login

The project was developed as a practical automation assignment for an internship assessment.

---

## Tech Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python 3.12       | Programming Language         |
| Playwright        | Browser Automation           |
| Pytest            | Test Runner                  |
| Pytest-Playwright | Playwright Fixture           |
| Python-Dotenv     | Secure Environment Variables |

---

## Project Structure

```text
automation-excercises/
│
├── pages/
│   ├── __init__.py
│   ├── HomePage.py
│   └── LoginPage.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

### Folder Explanation

| Folder/File        | Description                   |
| ------------------ | ----------------------------- |
| `pages/`           | Page Object Model classes     |
| `tests/`           | Test cases                    |
| `.env.example`     | Environment variable template |
| `pytest.ini`       | Pytest configuration          |
| `requirements.txt` | Project dependencies          |
| `.gitignore`       | Files excluded from Git       |

---

# Environment Setup

## 1. Clone Repository

```bash
git clone https://github.com/MdShafiurRahman0/Playwright-Login-Automation---AutomationExercise.git

cd Playwright-Login-Automation---AutomationExercise
```

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

**Linux / Deepin / Ubuntu**

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Playwright Browser

```bash
playwright install
```

---

# Configure Test Account

For security reasons, credentials are **not stored** inside the source code.

## Create `.env`

Create a file named `.env` in the project root.

```text
USER_EMAIL=your_email@example.com
USER_PASSWORD=your_password
```

Example:

```text
USER_EMAIL=test@example.com
USER_PASSWORD=StrongPassword123
```

> Never commit the `.env` file to GitHub.

---

# Test Execution

## Run All Tests

```bash
pytest -v
```

## Run With Browser

```bash
pytest --headed -v
```

## Run With Slow Motion

```bash
pytest --headed --slowmo 500 -v
```

## Generate HTML Report

```bash
pytest \
--headed \
--html=reports/report.html \
--self-contained-html \
-v
```

Open report:

```bash
xdg-open reports/report.html
```

---

# Test Scenario

### Login Automation Flow

```text
Open Website
      │
      ▼
Click Login
      │
      ▼
Enter Email
      │
      ▼
Enter Password
      │
      ▼
Click Login
      │
      ▼
Verify "Logged in as"
```

---

# Page Object Model (POM)

This project follows the **Page Object Model** to separate UI actions from test logic.

## HomePage

Responsible for:

* Launch website
* Navigate to Login page

## LoginPage

Responsible for:

* Locate email field
* Locate password field
* Click Login button

## Test File

Responsible for:

* Create page objects
* Execute user flow
* Validate expected result

This separation improves **maintainability**, **reusability**, and **readability**.

---

# Expected Result

| Step              | Expected Result             |
| ----------------- | --------------------------- |
| Open Website      | Homepage loads successfully |
| Navigate Login    | Login page opens            |
| Enter Credentials | Email & Password accepted   |
| Submit            | Login request sent          |
| Verification      | **Logged in as** is visible |

---

# Security

This project follows basic credential security practices.

* Credentials are stored in `.env`
* `.env` is ignored by Git
* `.env.example` is shared as a template
* No real password is included in the repository

---

# How the Test Works

1. `load_dotenv()` loads environment variables.
2. `HomePage` opens the website.
3. `goto_login()` navigates to the Login page.
4. `LoginPage.login()` fills the credentials.
5. Pytest verifies successful login using:

```python
assert page.locator("text=Logged in as").is_visible()
```

---

# Author

**Md. Shafiur Rahman**

* GitHub: https://github.com/MdShafiurRahman0
* LinkedIn: https://www.linkedin.com/in/mdshafiur/
