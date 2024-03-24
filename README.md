# Little Lemon Restaurant API

This project is an API built using Django REST Framework for managing table bookings for the Little Lemon restaurant. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on booking data, enabling the restaurant to efficiently manage reservations.

## Features

- **Authentication**: Users can authenticate using username and password to access protected endpoints.
- **Booking Management**: Users can create, view, update, and delete bookings.
- **Permissions**: Different permission levels are enforced to ensure that only authorized users can perform certain actions (e.g., only administrators can delete bookings).
- **Validation**: Input data is validated to ensure it meets specified criteria (e.g., date and time format for bookings).
- **API Documentation**: The API provides documentation for endpoints, request methods, and required parameters.
- **Database Integration**: The API integrates with a MySQL database to store booking information.

## Installation

To run this project locally, follow these steps:

- Clone the repository:
```bash
git clone https://github.com/Nessvah/little-lemon-api.git
```
- Navigate to the project directory:
```bash
cd little-lemon-api
```

- Install dependencies:
```bash
pip install -r requirements.txt
```

- Create MySQL database and user:

```bash
create database littlelemon;
use littlelemon;
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';
```

- Run migrations to create the database schema:
```bash
python manage.py migrate
```

- Create a superuser for accessing the Django admin interface and test the permissions for admins:
```bash
python manage.py createsuperuser
```

- Start the development server:
```bash
python manage.py runserver
```

- Access the API at `http://localhost:800/api/`
- Access the Django admin interface at `http://localhost:8000/admin/` and log in using the credentials you created in step 5.

## Usage

- **Authentication**: Before accessing protected endpoints, users need to authenticate by providing their username and password.
- **Testing**: Run tests using `python manage.py test tests`.

### Endpoints for menu items and bookings

| Endpoint           | URL                                      | Method     | Admin Permissions | User Permissions            |
|--------------------|------------------------------------------|------------|-------------------|-----------------------------|
| List Bookings      | `/api/restaurant/bookings/`              | GET        | Full access       | View own bookings           |
| Create Booking     | `/api/restaurant/bookings/`              | POST       | Full access       | Create own bookings         |
| Retrieve Booking   | `/api/restaurant/bookings/<booking_id>/` | GET        | Full access       | View own booking details    |
| Update Booking     | `/api/restaurant/bookings/<booking_id>/` | PUT, PATCH | Full access       | Update own booking details  |
| Delete Booking     | `/api/restaurant/bookings/<booking_id>/` | DELETE     | Full access       | Delete own bookings         |
| List Menu Items    | `/api/restaurant/menu/`                  | GET        | Full access       | View menu items             |
| Create Menu Item   | `/api/restaurant/menu/`                  | POST       | Full access       | No permission (only admins) |
| Retrieve Menu Item | `/api/restaurant/menu/<menu_item_id>/`   | GET        | Full access       | View menu items             |
| Update Menu Item   | `/api/restaurant/menu/<menu_item_id>/`   | PUT, PATCH | Full access       | No permission (only admins) |
| Delete Menu Item   | `/api/restaurant/menu/<menu_item_id>/`   | DELETE     | Full access       | No permission (only admins) |

### Endpoints for authentication

| Endpoint          | URL                                       | Method          | Description                                      | Permissions              |
|-------------------|-------------------------------------------|-----------------|--------------------------------------------------|--------------------------|
| User Registration | `/api/auth/users/`                        | POST            | Register a new user account.                     | Public access            |
| User Login        | `/api/auth/token/login/`                  | POST            | Obtain a JWT authentication token.               | Public access            |
| User Profile      | `/api/auth/users/me/`                     | GET, PUT, PATCH | Retrieve or update the user's profile.           | Authenticated users only |


## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to [Meta Back-End Developer](https://www.coursera.org/professional-certificates/meta-back-end-developer) for providing guidance and resources.