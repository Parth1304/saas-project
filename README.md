# SaaS Subscription App

A scalable Django-based SaaS platform with user authentication, Stripe subscription integration, and AWS deployment (EC2 + RDS). The project allows users to sign up, manage subscriptions, and access gated content based on their plan.

## 🚀 Features

- 🧑‍💻 User authentication (Login, Signup, Logout)
- 📦 Subscription management with Stripe
- 🧾 Billing page with active plan status
- 🔒 Social authentication (Login with GitHub)
- 🧰 Admin dashboard (Django Admin)
- ☁️ Deployed on AWS EC2, with PostgreSQL on AWS RDS
- ⚙️ CI/CD configured via GitHub Actions (including automated migrations)
## 🛠️ Tech Stack

- **Backend**: Django, PostgreSQL, Django AllAuth
- **Payments**: Stripe (Test Mode)
- **Deployment**: AWS EC2, AWS RDS, Gunicorn, Nginx
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Github Actions
- **Other**: Whitenoise, Python Decouple, Bootstrap (Frontend)

## 🧪 Live Test Stripe Keys

- Use test card: `4242 4242 4242 4242`
- Any valid expiry and CVC

## 🐳 Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/saas-app.git
   cd saas-app
    ```

2. **Create and activate virtualenv**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Or .\venv\Scripts\activate on Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   Create a `.env` file in the root directory:

   ```
   BASE_URL="http://localhost:8000"
   DJANGO_DEBUG=1
   DJANGO_SECRET_KEY='your-secret-key'
   DATABASE_URL='your-local-db-url or sqlite'
   EMAIL_HOST_USER='your@gmail.com'
   EMAIL_HOST_PASSWORD='your-app-password'
   STRIPE_SECRET_KEY='your-test-stripe-key'
   ```

5. **Run Migrations & Start Server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 🐋 Docker Deployment

1. **Build Docker Image**

   ```bash
   docker-compose build 
   ```

2. **Run Containers**

   ```bash
   docker-compose up
   ```

3. **Collect Static Files**

   ```
   python manage.py collectstatic 
   ```




## 🙋 Author

**Parth Khandelwal**


---

> ⚠️ This app is currently in development. Only basic login, signup, and pricing features are fully functional.

```
Let me know if you'd like me to:
- Add screenshots
- Include CI/CD (GitHub Actions)
- Customize author links, etc.
```
