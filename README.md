# ASD-Detect

ASD-Detect is a machine learning model designed to identify autism spectrum disorder traits through predictive analysis of behavioral data, via a questionnaire. It is a machine learning-based web application developed to help in the early detection of Autism Spectrum Disorder (ASD). The application asks users a set of questions based on the AQ10 (Autism Spectrum Quotient) questionnaire and uses a regressor model to predict whether the individual might have autism or not, based on their responses. The application is built using Python, Flask, and a simple HTML frontend to collect user input.<br>

**Basic Flow of the Application:**

![Assessment Questionnaaire](https://github.com/SK-21-D3v/ASD-Detect/blob/main/Screenshot%20(1379).png?raw=true)<br>

![List Of Reports]() <br>

![Adding a New Report]() <br>

![Upadtes List of Reports]()<br>

## Features:

- **AQ10-Based Questionnaire:** The application asks users a set of 10 questions derived from the AQ10 questionnaire to assess the likelihood of autism.<br>

- **Real-Time Prediction:** Based on the user's responses (Yes/No), the machine learning regressor model predicts whether the person has autism or not.<br>

- **User-Friendly Interface:** The web interface (index.html) makes it easy for users to answer the questions and view the result instantly.<br>

- **Model Integration:** The regressor model is integrated into the Flask backend to process the user responses and provide a prediction.<br>

## Technologies Used: 

- **Python:** The primary programming language for the backend logic and machine learning model.<br>

- **Flask:** Used for developing the web application backend, handling user inputs, and returning predictions.<br>

- **HTML/CSS:** Simple frontend with an index.html file to interact with users and collect responses.<br>

- **Scikit-learn:** For developing and using the regressor model to predict autism likelihood based on responses.<br>

- **Jinja2:** Templating engine used by Flask to render dynamic content in the frontend.<br>

## Future Enhancements

- Improved Model: Enhance the model’s accuracy by training it with a larger and more diverse dataset.<br>

- Multilingual Support: Add support for multiple languages to make the questionnaire accessible to a broader audience.<br>

- Mobile-Friendly Interface: Make the frontend responsive to ensure a better user experience on mobile devices.<br>

- User Authentication: Implement user login/logout functionality to save and track responses over time.<br>

- Detailed Reporting: Provide more detailed feedback and insights based on the user's answers, explaining the prediction results.<br>
