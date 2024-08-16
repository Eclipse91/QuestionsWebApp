# QuestionsWebApp in Django

QuestionsWebApp is a Django web application that allows users to test their knowledge of world geography by identifying countries and their capitals.

## Requirements

- Python 3.6 or higher
- Required Python packages are listed in the requirements.txt file

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/QuestionsWebApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd QuestionsWebApp
   ```

3. Install the required dependencies (creating a virtual environment is strongly recommended):

   ```bash
   pip install -r requirements.txt
   ```

4. Create a file .env containing this text:
   
    SECRET_KEY=_your_secret_key_

5. 
   ```bash
   python manage.py makemigrations geography
   ```

6. 
   ```bash
   python manage.py migrate
   ```

7. Load Fixtures:

   ```bash
   python manage.py loaddata geography
   ```

8. Run the development server:

   ```bash
   python manage.py runserver
   ```

9. Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the QuestionsWebApp.

## Usage

1. Visit the Home page to gain an introduction to the application.
2. Click on the "Geography" button to initiate the Geography game.
3. Identify the capital of the displayed country.
4. The cursor is always ready within the input bar for immediate typing.
5. Press "Enter" after providing an answer to swiftly progress to the next question.
6. In case of an incorrect response, a popup displays the correct solution.
7. Press "Enter" again to seamlessly move on to the next question, with the cursor conveniently placed in the input bar.
8. Utilize continent checkboxes to filter countries based on specific continents, customizing the game based on geographical preferences.

## Structure
   ```
├── QuestionsWebApp
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── geography
│   ├── templates
│   │   └── geography
│   │       └── geography.html
│   ├── fixtures
│   │   └── geography
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── shared
│   ├── templates
│   │   └── shared
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── images
│   │   ├── django_logo.png
│   │   ├── favicon.ico
│   │   ├── QWA-192x192.png
│   │   └── QWA.png
│   ├── js
│   │   └── script.js
│   └── styles
│       └── styles.css
├── templates
│   ├── base.html
│   └── navbar.html
├── .gitignore
├── LICENSE
├── README.md
├── db.sqlite3
├── manage.py
└── requirements.txt
   ```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the QuestionsWebApp. Adjust the content as needed for your project.