# 🧠 VeriWell: AI Wellness Coach for Students
> **HackHarvard 2025 Submission**

VeriWell uses **Generative AI** to help students connect their daily habits (sleep, study time, diet) to their measured well-being, providing personalized, data-driven coaching that goes far beyond simple logging.

## 🚀 Quick Links & Demo
| Item | Link |
| :--- | :--- |
| **Demo Video/Pitch** | [**https://youtu.be/6NL0ZSm25nw**] |

## ✨ Key Technologies (The Stack)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![AI/ML](https://img.shields.io/badge/LLM-Gemini_API-3C77E0?style=for-the-badge&logo=google)](https://ai.google.dev/gemini-api)
[![Framework](https://img.shields.io/badge/App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Database](https://img.shields.io/badge/Database-Firebase-FFCA28?style=for-the-badge&logo=firebase)](https://firebase.google.com/)

---

## 💡 The Problem

College students face high rates of burnout, poor sleep, and mental stress. They often track their habits in journals or simple apps but struggle to connect those inputs to their overall mental and academic performance. Existing tools are passive; they log data but fail to provide the personalized, **actionable insights** students need to make meaningful changes.

---

## 🎯 VeriWell's Core Features

VeriWell acts as a data scientist and coach, turning raw input into tailored behavior modification:

1.  **Habit & Well-being Logging:** A fast, simple interface (built with Streamlit) allows students to log daily activities (sleep, exercise, meals, study hours) and subjective well-being scores (e.g., mood, stress level).
2.  **AI Correlation Engine (Gemini API):** We engineered a custom LLM prompt that processes the user's historical data, transforming it into a correlation analysis. The AI identifies specific patterns such as: *"When your screen time exceeds 4 hours, your sleep latency increases by an average of 15 minutes."*
3.  **Personalized Coaching:** Based on the data-driven correlations, VeriWell provides specific, empathetic, and actionable coaching recommendations, replacing generic advice with highly personalized, weekly tasks aimed at improving student performance and mental health.

---

<img width="1271" height="624" alt="0" src="https://github.com/user-attachments/assets/992ce2e2-2083-4cdf-89f5-01ea797181cd" />
<img width="1271" height="624" alt="1" src="https://github.com/user-attachments/assets/b540bdd8-ac24-441b-ad35-59b8635eadda" />
<img width="1271" height="624" alt="3" src="https://github.com/user-attachments/assets/2428ec15-a2e8-40bd-b0bc-f906265d6517" />
<img width="1216" height="681" alt="4" src="https://github.com/user-attachments/assets/1cafd024-3a29-402e-9567-bffbd5bed718" />

---

## ⚙️ Technical Deep Dive

The architecture is designed for rapid development, secure data handling, and powerful AI analysis:

* **The AI Core:** We utilized the **Gemini API** for its advanced reasoning capabilities. The model is specifically instructed to analyze tabular data, identify statistical relationships, and generate human-readable text output that functions as a sophisticated, data-driven wellness report.
* **Data Persistence:** All habit and well-being data is securely managed and stored in **Firebase Firestore**, ensuring persistent, scalable data tracking for longitudinal analysis.
* **Frontend Interface:** **Streamlit** allowed us to build an interactive, data-focused web application in a fraction of the time, letting us focus almost entirely on the AI logic and backend integration.

---

## 💪 Challenges & Triumphs

We faced complexity in creating a truly analytical AI tool within the hackathon timeframe:

* **Challenge: Data-Driven Prompts:** The core difficulty was prompt engineering the LLM to transition from a general-purpose chat interface to a highly analytical tool that *only* provides data-driven correlations, avoiding generic, pre-programmed wellness advice.
* **Triumph: Consistent Analysis:** We successfully engineered a multi-step prompt system that consistently delivers statistically sound, actionable insights, making the coaching feel personalized and valuable to the user.
* **Triumph: Full Stack Integration:** We successfully implemented a full application loop, from **Streamlit UI** → **Python/LLM Logic** → **Firebase Read/Write** and back, demonstrating a robust, production-ready minimum viable product.

---

## 🔮 Future Vision

1.  **Wearable Integration:** Implement hooks for Apple Health and Google Fit to automatically ingest sleep, heart rate, and activity metrics, eliminating manual logging.
2.  **Gamification:** Introduce streaks, badges, and positive feedback loops to incentivize consistent logging and habit adherence.
3.  **Predictive Modeling:** Use the collected data to predict potential burnout periods or declines in well-being before they occur.

---
***

## ⚙️ Local Setup Guide

If you wish to run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/anunjinb/VeriWell-HackHarvard2025.git](https://github.com/anunjinb/VeriWell-HackHarvard2025.git)
    cd VeriWell-HackHarvard2025
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up secrets (IMPORTANT):**
    * Copy `.env.example` to `.env` and fill in your keys.
    * Place your Firebase service account JSON at the project root as `firebase_credentials.json`.
    * Alternatively, set the API key in your terminal: `export GEMINI_API_KEY="your_key"`
4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
