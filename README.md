 News App
I used Python, Html and Flask to make this task.
After I checking the documentation as the task provided, I find out the task isn't hard at all.

This is a Flask web application that retrieves and displays news from the [News API](https://newsapi.org/).
It allows users to view current news and search for news articles using specific search parameters.

 Features

- Display current news articles fetched from the News API.
- Allow users to enter search terms to find related news articles.

 Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.7 or above.
- You have a `<Windows/Linux/Mac>` machine. State which OS is supported/which is not.
- You have read the [News API documentation](https://newsapi.org/docs).

 Installation and Setup

1. Clone the repository:
```bash
git clone [https://github.com/kolumbino/RDI].git

2. Navigate to the project directory:
cd RDI

3. Install the requirements:
pip install -r requirements.txt

4. Set up the .env file with your News API key:
NEWS_API_KEY='your real API key here'

5. Usage

To run the application, make sure you are in the project directory and execute:

```bash
flask run
or
python app.py

The application will start on localhost:5000 by default. Open a web browser and navigate to http://localhost:5000 to use the News App.
Contributing to the News App

To contribute to the News App, follow these steps:

Fork this repository.
Create a branch: git checkout -b branch_name.
Make your changes and commit them: git commit -m 'commit_message'.
Push to the original branch: git push origin branch_name.
Create the pull request.
