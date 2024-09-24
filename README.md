# StarTrek Airline Reservation System

This is a Django-based web application that allows users to view available flights, book tickets, and manage their reservations. The system is built using Python and MySQL, providing a simple yet robust interface for both users and administrators.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Flight Management:** View flight schedules and available seats.
- **User Authentication:** Users can sign up, log in, and manage their bookings.
- **Booking System:** Users can book flights and manage their reservations.
- **Admin Interface:** Administrators can manage flights, airports, and passengers through a user-friendly admin panel.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/airline-reservation-system.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd airline-reservation-system
   ```
3. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up the MySQL database:**
   - Ensure MySQL is installed and running.
   - Create a new database and update the `settings.py` file with your database credentials.

6. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000`.

## Usage

- Users can sign up and log in to book flights.
- Administrators can manage flights, passengers, and airports through the Django admin interface.
- To access the admin panel, use the following URL: `http://127.0.0.1:8000/admin/`.

## Technologies Used

- **Backend:** Django, Python
- **Database:** MySQL
- **Frontend:** HTML, CSS, Django Templates
- **Other:** Django ORM, Bootstrap

## Project Structure

```
airline-reservation-system/
│
├── airline/                     # Main project folder
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   └── wsgi.py                  # WSGI configuration
│
├── flights/                     # App for managing flights
│   ├── models.py                # Database models
│   ├── views.py                 # Views for handling requests
│   ├── urls.py                  # URL routing for flights
│   └── templates/               # HTML templates
│
├── users/                       # App for user authentication
│   ├── models.py                # User model
│   ├── views.py                 # Authentication views
│   └── templates/               # HTML templates for login/signup
│
└── manage.py                    # Django management script
```

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
