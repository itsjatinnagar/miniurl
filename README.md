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
1. Docker

## System Design

### Assumptions

Assuming 40K new URLs created per month and 50:1 read-write ratio.

|             Title             |                 Calculation                  |      Estimate       |
| :---------------------------: | :------------------------------------------: | :-----------------: |
|           New URLs            |          40K / (30 days x 24 hours)          |  50 links per hour  |
|         URL redirects         | 40K x 50 / (30 days x 24 hours x 60 minutes) | 50 links per minute |
|   Link Storage for 90 days    |       2080 bytes/URL x 40K x 3 months        |       238 MB        |
| Analytics Storage for 90 days |     134 bytes/URL x 40K x 50 x 3 months      |       767 MB        |

### Constraints

- 512 MB RAM
- 1 GB Database Storage
- 90 Days Data Life

## Database Schema

- User
  | Column | Type |
  | ------ | ---- |
  | `_id` | integer |
  | `email` | varchar(320) |

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
