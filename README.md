# 🦷 DentalAI — Intelligent Dental Health Scanner & Dashboard

For ML Pipeline view [Hack4Health-ml](https://github.com/KunalSuman/ML_backend_oral_health)

DentalAI is a modern, two-way dental care platform that combines a Django backend, RESTful APIs, and a state-of-the-art deep learning pipeline. The platform empowers both patients and dentists — patients can scan their teeth, receive instant AI-driven analysis, and track their health; dental professionals can monitor user submissions, review AI-generated reports, and provide informed guidance, all through a secure, intuitive dashboard.

## Features

- AI-Based Dental Issue Detection: Upload an image, get a score and diagnosis within seconds.
- Dual Dashboard Interface: Separate flows for patients and dentists, including onboarding, test management, and report review.
- Custom Scoring & Priority Assignment: Automated health score and urgency (Low / High / Emergency).
- Condition-wise Probability & Highlights: See per-condition AI probabilities and actionable highlights for every scan.
- RESTful, JSON-first API: Easy integration for new frontends, automation, or research.
- Mobile-First Frontend: Clean UX, responsive layouts for both Android/iOS and desktop.
- Verified Results: Every test report includes verification status and clearly identified highlights.
- Fast Inference: Model delivers results in under 0.2s (served via a separate ML pipeline).

## Setup & Deployment

Supports local and containerized (Docker) deployments.
Configurable via environment variables, JSON, or YAML (see .env / docker-compose.yml).

1. Clone and Install
    ```
    bash
    git clone https://github.com/<your-org>/dentalai.git
    cd dentalai
    python -m venv .venv
    source .venv/bin/activate            # Use `.venv\Scripts\activate` on Windows
    pip install -r requirements.txt
    ```

2. Initial Configuration
    The app supports secure config via .env, JSON, or YAML ().

    Set environment variables for secrets and DB connection.

    Adjust settings.py or config YAML as needed.

3. Database Setup
    ```
    bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. (Optional) Docker Deployment
    Optimized for Docker and Gunicorn hosting. Supports advanced container/network configs ().

bash
docker build -t dentalai:latest .
docker-compose up
Supports shm_size tuning for large ML inference.

Exposes ports and SSL configs per deployment best practices.

DNS/config integration for internal/external access ().

5. Launch (Local Dev)
bash
python manage.py runserver 0.0.0.0:5197
Access the app at http://<device-ip>:5197

🧠 How It Works
Patient’s Journey
Register or sign in as a patient.

Complete onboarding questions.

Use the webcam or upload to scan your teeth.

The AI analyzes the image, returning:

Overall score

AI-verified highlights & urgency

Detailed dental condition breakdown

Dentist’s Journey
Register as a dentist, manage your patient panel.

Instantly view test images, AI-generated diagnosis, and patient history.

Leverage per-patient and test-level insights for triage and treatment.

📦 API Usage Example
Image Inference (cURL):

bash
curl -X POST -F "image=@image.jpg" http://<host>:<port>/predict
Returns .json with score, top condition, probabilities, and highlights.

🗃️ Tech Stack
Backend: Django, Django REST Framework

Frontend: Tailwind CSS, HTML/JS

AI/Inference: Custom CNN Ensemble (Python, served over Docker/REST)

DevOps: Docker, Gunicorn, nginx (optional)

Config: Environment (.env), JSON, YAML

Networking: DNS routing, SSL (optional) ()

✨ Screenshots
Add screenshots of landing, onboarding, dashboard, report, and mobile layouts here!

👩‍💻 For Developers
RESTful design, easy to extend/automate ()

Uses Django’s custom user models, role-based routing, dynamic dashboards

Supports local, home server, or cloud deployment ()

📝 Team
Happy_Meal

DentalAI : Bringing intelligent, accessible, and early-stage dental diagnostics to everyone.
Built with passion, precision, and purpose.

If you encounter any issues, see troubleshooting.md or open an issue on GitHub!