# VeriWell-HackHarvard2025
VeriWell: An AI wellness coach helping students connect their daily habits to their well-being. Built for HackHarvard 2025

## Setup & Secrets

This project uses API keys and Firebase credentials which must NOT be committed to version control.

- Copy `.env.example` to `.env` and fill in your API keys (do not commit `.env`).
- Place your Firebase service account JSON at the project root as `firebase_credentials.json` (do NOT commit this file).

Example:

```bash
# copy example and edit
cp .env.example .env
open .env # or use an editor to paste your keys
```

The repository already includes a `.gitignore` that excludes `.env` and `firebase_credentials.json`.
It also excludes `config.json` because it may contain your Google API key. Instead, use `config.example.json` and copy it to `config.json` locally.

If you accidentally added `config.json` to git, remove it from the index (keeps the file locally) with:

```bash
git rm --cached config.json
git commit -m "chore: remove config.json from repo and add to .gitignore"
```


For local development you can also set the API key in the shell for a single run:

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
streamlit run app.py
```

