# MiniUrl

## Overview

MiniUrl is a Web Application based URL Shortening Service.

## Features

-   Passwordless Login
-   Single Page Application
-   Supports QR Codes
-   Supports Link Analytics (like: click count)
-   Custom Short ID

## Technologies used

1. HTML5
2. CSS3
3. JavaScript
4. Flask
5. PostgreSQL
6. Docker

## System Design

### Assumptions

Assuming 117K new URLs per month and 100:1 read-write ratio.

|        Title        |                  Calculation                   |       Estimate       |
| :-----------------: | :--------------------------------------------: | :------------------: |
|      New URLs       |    117K / (30 days x 24 hours x 60 minutes)    |  3 links per minute  |
|    URL redirects    | 117K x 100 / (30 days x 24 hours x 60 minutes) | 270 links per minute |
| Storage for 90 days |        3000 bytes/URL x 117K x 3 months        |         1 GB         |

### Constraints

-   512 MB RAM
-   1 GB Database Storage
-   90 Days Data Life

## Database Schema

-   User
    | Column | Type |
    | ------ | ---- |
    | `_id` | integer |
    | `email` | varchar(320) |

-   URL
    | Column | Type |
    | ------ | ---- |
    | `hash` | varchar(16) |
    | `title` | varchar(925) |
    | `long_url` | varchar(2048) |
    | `creation_date` | varchar(7) |
    | `clicks` | integer |
