import os
from rich import print

username = os.getenv("TEST_USER")
password = os.getenv("TEST_PASS")

print(username, password)

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Username: {username}</h1>
    <h1>Password: {password}</h1>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file was created")