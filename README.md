## Usage

1. Clone the repository:
   
2. Install the required dependencies:
   
   pip install -r requirements.txt
   
3. Set up the database:
   
   python manage.py migrate
   
4. Create a superuser (optional):
   
   python manage.py createsuperuser
   

5. Start the development server:
   
   python manage.py runserver
   

6. Open your web browser and navigate to `http://localhost:8000`

7. Register a new account using the signup form
8. Log in with your credentials
9. Select a user from the chat room to start messaging
10. Send and receive messages in real-time

11. The link for the application : https://anushkakk002.pythonanywhere.com/signup/

## Project Structure

- `chat/models.py`: Contains Message model for storing chat messages
- `chat/consumers.py`: WebSocket consumer for handling real-time messages
- `chat/views.py`: View functions for handling HTTP requests
- `chat/static/`: Static files including JavaScript for form validation
- `chat/templates/`: HTML templates for the application
