```markdown
# QuestionWebApp in Django

QuestionWebApp is a Django web application that allows users to test their knowledge of world geography by identifying countries and their capitals.

## Features

- **Navigation Bar:**
  - The application includes a navigation bar with two main links: Home and Geography.

- **Home Page:**
  - The Home page provides a brief introduction to the application and its purpose.

- **Geography Game:**
  - Clicking on the "Geography" button in the navigation bar leads users to the Geography game.
  - The game randomly selects a country, and users have to input the correct capital for that country.

- **Continent Filter:**
  - Users can filter the countries based on continents using checkboxes.
  - This feature helps users focus on specific regions during the game.

## Prerequisites

Before running the application, make sure you have the following installed:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/QuestionWebApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd QuestionWebApp
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the QuestionWebApp.

## Usage

1. Navigate to the Home page to get an introduction to the application.
2. Click on the "Geography" button to start the Geography game.
3. Identify the capital of the displayed country.
4. Use the continent checkboxes to filter countries based on continents.

## Contributing

If you'd like to contribute to the development of QuestionWebApp, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to customize the README to fit the specific details of your application.