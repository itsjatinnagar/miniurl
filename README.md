# MiniUrl

MiniUrl is a Web Application based URL Shortening Service.

## Features

- Passwordless Login
- Single Page Application
- Supports QR Codes
- Supports Link Analytics

## Technologies used

1. React
1. Redux Toolkit
1. Flask
1. PostgreSQL

## Database Schema

- User
  | Column | Type |
  | ------ | ---- |
  | `_id` | integer |
  | `email` | varchar(320) |
  | `created_at` | varchar(10) |

- URL
  | Column | Type |
  | ------ | ---- |
  | `_id` | integer |
  | `uid` | integer |
  | `hash` | varchar(4) |
  | `long_url` | varchar(2048) |
  | `created_at` | varchar(10) |
  | `clicks` | integer |

- Analytics
  | Column | Type |
  | ------ | ---- |
  | `_id` | integer |
  | `lid` | integer |
  | `ua` | varchar(120) |
  | `redirect_at` | varchar(10) |

## Checkout

You can checkout the Frontend of the **MiniUrl** on https://github.com/itsjatinnagar/miniurl-ui
