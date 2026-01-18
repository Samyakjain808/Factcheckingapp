# Fact-Checking Web App

This project is a web application that uses AI to extract and verify factual claims from a PDF document. It leverages the power of Large Language Models (LLMs) to identify verifiable claims and then uses web search to determine their accuracy.

### Live Deployment

🔗 https://factcheckingapp-enlcwkcqhwqehtznbq9d32.streamlit.app/

## Features

-   **PDF Upload**: Upload a PDF document to have its claims fact-checked.
-   **Claim Extraction**: Automatically extracts factual claims related to statistics, dates, prices, financial figures, and technical specifications.
-   **Claim Verification**: Verifies each claim using live web data and classifies it as "Verified", "Inaccurate", or "False".
-   **Streamlit Interface**: A simple and intuitive web interface built with Streamlit.

## How it Works

1.  **PDF Text Extraction**: The application first extracts the text from the uploaded PDF document.
2.  **Claim Extraction**: The extracted text is then passed to a Google Gemini Pro model, which has been prompted to identify and extract verifiable claims.
3.  **Web Search**: For each extracted claim, the application uses the Serper API to perform a Google search to find relevant information and sources.
4.  **Claim Verification**: The search results are then passed to another instance of the Gemini Pro model, which is prompted to determine the validity of the claim based on the provided web data.
5.  **Display Results**: The application then displays each claim along with its verification status ("Verified", "Inaccurate", or "False") and a brief explanation.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

This project requires API keys for Google Gemini and Serper.

1.  Create a `.env` file in the root directory of the project.
2.  Add your API keys to the `.env` file as follows:

    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    SERPER_API_KEY="YOUR_SERPER_API_KEY"
    ```

    -   You can get a Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
    -   You can get a Serper API key from [Serper.dev](https://serper.dev/).

## Usage

To run the application locally, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit web server, and you can access the application in your browser at `http://localhost:8501`.

## Deployment

This application is designed to be deployed on Streamlit Cloud.

1.  **Push to GitHub:** Make sure your project is in a GitHub repository.
2.  **Sign up for Streamlit Cloud:** If you don't have an account, sign up at [streamlit.io/cloud](https://streamlit.io/cloud).
3.  **Deploy New App:**
    *   Click "New app" from your Streamlit Cloud dashboard.
    *   Connect your GitHub account.
    *   Select the repository and branch for your app.
    *   The main file path should be `app.py`.
4.  **Add Secrets:** The application requires API keys to function. You must add these as secrets in your Streamlit Cloud app settings.
    *   Go to your app's settings (Advanced settings).
    *   Under the "Secrets" section, add the following:
        ```
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
        SERPER_API_KEY="YOUR_SERPER_API_KEY"
        ```

After saving the secrets, your app will restart, and it should be live and accessible via the provided URL.

## Project Structure

```
.
├── app.py              # The main Streamlit application
├── claim_extractor.py  # Module for extracting claims from text
├── verifier.py         # Module for verifying claims using web search
├── requirements.txt    # Project dependencies
├── list.py             # Helper script to list available Gemini models
├── .env                # your secret api code
└── README.md           # This file
```


