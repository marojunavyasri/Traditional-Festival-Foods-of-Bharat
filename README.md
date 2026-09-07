# Traditional-Festival-Foods-of-Bharat

This project is an interactive web application that explores the traditional and festive foods of different states of India.

The application provides an interactive map of India where users can select a state and explore information about its traditional festival foods. It also includes a chatbot that uses Google Gemini to provide AI-generated responses to user questions.

---

# Project Overview

India has a rich and diverse food culture, with every state having its own traditional dishes and festive specialties.

This project provides a simple and interactive way to explore this diversity through:

* An interactive map of India
* State-wise food information
* Individual pages for different states
* An AI-powered chatbot
* A simple and user-friendly interface
* Google Translate support

---

# Features

## Interactive India Map

The homepage contains an interactive SVG map of India.

Users can select different states from the map to explore their traditional festival foods.

## State-wise Information

The project contains separate HTML pages for different states.

Examples include:

```text
Andhra Pradesh
Arunachal Pradesh
Bihar
Chhattisgarh
Gujarat
Haryana
Himachal Pradesh
Jharkhand
Karnataka
Kerala
Madhya Pradesh
Maharashtra
Mizoram
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
```

## AI Chatbot

The project includes an AI chatbot that allows users to enter questions and receive responses generated using Google Gemini.

The chatbot frontend sends the user's message to a Flask backend, which communicates with the Gemini API and returns the response to the webpage.

## Google Translate

Google Translate is included to make the website accessible to users who prefer different languages.

---

# Technologies Used

* HTML5
* CSS3
* JavaScript
* Python
* Flask
* Google Gemini API
* SVG
* Google Translate

---

# Project Structure

```text
Traditional-Festival-Foods-of-Bharat/
│
├── README.md
├── index.html
├── frontpg.html
├── style.css
├── chatbot.js
├── chatbot.py
├── app.py
│
├── ap.html
├── ar.html
├── as.html
├── br.html
├── ct.html
├── ga.html
├── gj.html
├── hp.html
├── hr.html
├── jh.html
├── jk.html
├── ka.html
├── kl.html
├── mh.html
├── ml.html
├── mn.html
├── mp.html
├── mz.html
├── nl.html
├── or.html
├── pb.html
├── rj.html
├── sk.html
├── tg.html
├── tn.html
├── tn1.html
├── tr.html
├── up.html
├── ut.html
└── wb.html
```

---

# How the Chatbot Works

The chatbot uses a frontend and backend architecture.

```text
User
  ↓
Chatbot Interface
  ↓
JavaScript
  ↓
Flask Backend
  ↓
Google Gemini API
  ↓
AI Response
  ↓
Chatbot Interface
```

The frontend sends the user's message to the Flask `/chat` endpoint.

The Flask application processes the request and generates a response using the Gemini model.

---

# Main Files

## index.html

The main webpage of the project.

It contains:

* Project title
* Introduction
* Interactive India map
* State links
* Chatbot interface
* Google Translate integration

## style.css

Contains the styling for:

* India map
* Chatbot
* Buttons
* Input fields
* Page layout
* Hover effects

## chatbot.js

Handles communication between the chatbot interface and the Flask backend.

It sends user messages to the backend and displays the generated response.

## app.py

Contains the Flask backend.

It:

* Creates the Flask application.
* Enables CORS.
* Receives chatbot requests.
* Communicates with Google Gemini.
* Returns the AI response.

## chatbot.py

Contains a standalone Python version of the Gemini chatbot that can be run through the terminal.

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/marojunavyasri/Traditional-Festival-Foods-of-Bharat.git
```

```bash
cd Traditional-Festival-Foods-of-Bharat
```

## 2. Install Required Python Packages

```bash
pip install flask flask-cors google-generativeai
```

## 3. Configure the Gemini API Key

Do not store the API key directly in the source code.

Set it as an environment variable instead.

Example:

```text
GEMINI_API_KEY=your_api_key
```

Then configure the application to read the key from the environment.

## 4. Start the Flask Backend

```bash
python app.py
```

The Flask server runs locally and provides the `/chat` endpoint for chatbot communication.

## 5. Open the Website

Open:

```text
index.html
```

in a web browser.

The chatbot requires the Flask backend to be running.

---

# User Interaction

The user can:

1. Open the website.
2. Explore the interactive map of India.
3. Select a state.
4. View information about traditional festival foods.
5. Ask questions through the chatbot.
6. Receive an AI-generated response.

---

# Learning Outcomes

This project demonstrates:

* Web page development using HTML and CSS.
* JavaScript-based frontend interaction.
* SVG-based interactive maps.
* Creating a backend using Flask.
* Connecting a web application with an AI API.
* Sending and receiving JSON data.
* Using JavaScript `fetch()` for API communication.
* Integrating Google Translate.
* Organizing state-wise web content.

---

# Future Improvements

The project can be further improved by:

* Adding more detailed information about each food.
* Adding images for traditional dishes.
* Improving the chatbot interface.
* Adding food categories and search functionality.
* Adding responsive design for mobile devices.
* Improving accessibility.
* Deploying the application online.

---

# Author

**Navya Sri**
