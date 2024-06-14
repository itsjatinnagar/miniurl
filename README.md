![miniurl_preview](https://github.com/itsjatinnagar/miniurl/assets/121741542/225c4cc4-1cd6-4730-95ab-6080ba1dec9b)

## Overview

**miniurl** is a web application that allows users to generate unique, short identifiers for long URLs. These can be shared across any platform, and the service takes only milliseconds to create a short URL.

## Features

- **Password-less User Authentication**: Utilizes OTPs for a smooth and secure login process without traditional passwords.
- **QR Code Generation**: Users can download a QR Code image for each generated short URL.
- **Responsive Design**: Fully responsive web application, adaptable to various device screens.

## Technical Overview

The application is built using the following technologies:

- **Frontend**: React with Context API and Reducers. For more details and the source code, see the [miniurl-ui](https://github.com/itsjatinnagar/miniurl-ui).
- **Styling**: TailwindCSS for modern, utility-first styling.
- **Backend**: Flask as a lightweight, easy to extend Python Web Framework.
- **Database**: PostgreSQL for robust, scalable data storage.
- **Deployment**: Render for simple, seamless deployment.

### Why this stack?

- **React** (with Context API and Reducers) was chosen for its powerful UI rendering capabilities and efficient state management, ideal for dynamic applications like this URL shortener.
- **TailwindCSS** provides utility-first components that speed up development without sacrificing the application's aesthetic and responsiveness.
- **Flask** offers simplicity and flexibility, making it perfect for small to medium projects where quick iterations are necessary.
- **PostgreSQL** is used for its reliability and integrity in handling data, crucial for features like user management and URL mapping.
- **Render** was selected for its ease of use in deployment and its free tier, which is suitable for small projects and prototypes.

## Setup Instructions

### Pre-requisites

- Python: 3.10.12
- PIP: 24.0

### Installation

```bash
git clone https://github.com/itsjatinnagar/miniurl.git
cd miniurl
pip install -r requirements.txt
# Generate Secret Key
python -c "import secrets; print(secrets.token_hex(32))"
# Initialize Database and Tables
python database/init.py
# Run Application
flask run
```

## Usage

Access the web application by navigating to **\`127.0.0.1:5000\`** in your web browser. The application's homepage will serve as the main interface for all interactions.

## Database Configuration

- **\`users\`** stores user details including their email with registration date and time.
  | Column | Type |
  | ------ | ---- |
  | `id` | integer |
  | `email` | varchar(320) |
  | `created_at` | varchar(10) |

- **\`links\`** stores information about the shortened URLs.
  | Column | Type |
  | ------ | ---- |
  | `id` | integer |
  | `uid` | integer |
  | `hash` | char(4) |
  | `long_url` | varchar(2048) |
  | `created_at` | varchar(10) |
  | `clicks` | integer |

- **\`analytics\`** captures user interactions for each link.
  | Column | Type |
  | ------ | ---- |
  | `id` | integer |
  | `lid` | integer |
  | `user_agent` | varchar(180) |
  | `redirect_at` | varchar(10) |

## Deployment

Deploy the application as a **Web Service** on [Render](https://render.com). Note the _free tier_ specifics, such as the server spinning down after 15 minutes of inactivity.

## Environment Variables

- **SECRET_KEY**: Used to encrypt session cookies.
- **EMAIL_USER**: Email login for sending OTPs.
- **EMAIL_PASS**: Password for email account used in sending OTPs.
- **EMAIL_HOST**: SMTP server for outgoing emails.
- **EMAIL_PORT**: Port number for SMTP server.
- **DB_URI**: Connection string for the PostgreSQL database.

## Contributing

This project is open for suggestions and bug reports. However, as it is part of a personal portfolio, direct code contributions are not currently being accepted.

## License

This project is not covered under any specific open-source license and is intended for educational and portfolio use only.
