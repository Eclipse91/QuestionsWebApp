# QuestionsWebApp in Django

QuestionsWebApp is a Django web application that allows users to test their knowledge of world geography by identifying countries and their capitals.

## Requirements

- Python 3.6 or higher
- Required Python packages can be installed using `pip install -r requirements.txt`

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/QuestionsWebApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd QuestionsWebApp
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a file .env containing this text:
   
    SECRET_KEY=_your_secret_key_


5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the QuestionsWebApp.

## Usage

1. Visit the Home page to gain an introduction to the application.
2. Click on the "Geography" button to initiate the Geography game.
3. Identify the capital of the displayed country.
4. The cursor is always ready within the input bar for immediate typing.
5. Press "Enter" after providing an answer to swiftly progress to the next question.
6. In case of an incorrect response, a popup displays the correct solution.
7. Press "Enter" again to seamlessly move on to the next question, with the cursor conveniently placed in the input bar.
8. Utilize continent checkboxes to filter countries based on specific continents, customizing the game based on geographical preferences.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the QuestionsWebApp. Adjust the content as needed for your project.
