# 0x11. Python - Network #1

By Guillaume, CTO at Holberton School

Author [Carlos Andres Polania](https://twitter.com/timberdev) (capolaniaq@correo.udistrital.edu.co)

## Learning Objectives

-   How to fetch internet resources with the Python package  `urllib`
-   How to decode  `urllib`  body response
-   How to use the Python package  `requests`  #requestsiswaysimplerthanurllib
-   How to make HTTP  `GET`  request
-   How to make HTTP  `POST`/`PUT`/etc. request
-   How to fetch JSON resources
-   How to manipulate data from an external service

## Tasks

### 0. What's my status? #0
Write a Python script that fetches  `https://intranet.hbtn.io/status`

-   You must use the package  `urllib`
-   You are not allowed to import any packages other than  `urllib`
-   The body of the response must be displayed like the following example (tabulation before  `-`)
-   You must use a  `with`  statement

### 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the  `X-Request-Id`  variable found in the header of the response.

-   You must use the packages  `urllib`  and  `sys`
-   You are not allow to import packages other than  `urllib`  and  `sys`
-   The value of this variable is different for each request
-   You don’t need to check arguments passed to the script (number or type)
-   You must use a  `with`  statement

### 2. POST an email #0

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

### 3. Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

### 4. What's my status? #1

Write a Python script that fetches `https://intranet.hbtn.io/status`

-   You must use the package  `requests`
-   You are not allow to import packages other than  `requests`
-   The body of the response must be display like the following example (tabulation before  `-`)

### 5. Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

### 6. POST an email #1

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

### 7. Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

### 8. Search API

Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

### 9. My GitHub!

Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://intranet.hbtn.io/rltoken/7CiInsXY2fMRZWSoHQs_TA "GitHub API") to display your `id`

### 10. Time for an interview!
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one: