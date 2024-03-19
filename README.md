django admin user -> admin
django admin password -> admin@123!

## Django admin 

User -> admin
Password -> admin@123!

## Endpoints for menu items and bookings

| Endpoint           | URL                                          | Method     | Admin Permissions | User Permissions            |
|--------------------|----------------------------------------------|------------|-------------------|-----------------------------|
| List Bookings      | `/api/restaurant/bookings/`                  | GET        | Full access       | View own bookings           |
| Create Booking     | `/api/restaurant/bookings/`                  | POST       | Full access       | Create own bookings         |
| Retrieve Booking   | `/api/restaurant/bookings/<booking_id>/`     | GET        | Full access       | View own booking details    |
| Update Booking     | `/api/restaurant/bookings/<booking_id>/`     | PUT, PATCH | Full access       | Update own booking details  |
| Delete Booking     | `/api/restaurant/bookings/<booking_id>/`     | DELETE     | Full access       | Delete own bookings         |
| List Menu Items    | `/api/restaurant/menu-items/`                | GET        | Full access       | View menu items             |
| Create Menu Item   | `/api/restaurant/menu-items/`                | POST       | Full access       | No permission (only admins) |
| Retrieve Menu Item | `/api/restaurant/menu-items/<menu_item_id>/` | GET        | Full access       | View menu items             |
| Update Menu Item   | `/api/restaurant/menu-items/<menu_item_id>/` | PUT, PATCH | Full access       | No permission (only admins) |
| Delete Menu Item   | `/api/restaurant/menu-items/<menu_item_id>/` | DELETE     | Full access       | No permission (only admins) |

## Endpoints for authentication

| Endpoint          | URL                                       | Method          | Description                                      | Permissions              |
|-------------------|-------------------------------------------|-----------------|--------------------------------------------------|--------------------------|
| User Registration | `/api/auth/users/`                        | POST            | Register a new user account.                     | Public access            |
| User Login        | `/api/auth/token/login/`                  | POST            | Obtain a JWT authentication token.               | Public access            |
| User Logout       | `/api/auth/token/logout/`                 | POST            | Invalidate the current JWT authentication token. | Authenticated users only |
| User Profile      | `/api/auth/users/me/`                     | GET, PUT, PATCH | Retrieve or update the user's profile.           | Authenticated users only |
| Change Password   | `/api/auth/users/set_password/`           | POST            | Change the user's password.                      | Authenticated users only |
| Reset Password    | `/api/auth/users/reset_password/`         | POST            | Request a password reset email.                  | Public access            |
| Set New Password  | `/api/auth/users/reset_password_confirm/` | POST            | Set a new password after receiving reset token.  | Public access            |

