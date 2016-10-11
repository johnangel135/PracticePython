import requests
from bs4 import BeautifulSoup

base_url = 'http://113.161.77.24:10204'
auth_url = base_url + '/api/identity/Authenticate'
sgin_url = base_url + '/api/identity/SignIn'
sgup_url = base_url + '/api/identity/signup'

def authorize():
    url = auth_url
    payload = {
        "UserID": "admin",
        "Password": "Admin123!@#$"
    }

    r = requests.post(url, payload)
    auth = str(r.json()['Data']['AuthorizeToken'])
    return auth


header = {'Authorization': authorize()}


def signin():
    url = sgin_url
    # email = input("Email: ")
    # passw = input("Password: ")
    payload = {
    "Email": "duong.truong@s3corp.com.vn",
    "Password": "Admin!12345"
    #"Email": email,
    #"Password": passw
    }
    r = requests.post(url, headers=header, data=payload)
    return r.json()


class user():
    obj = signin()['Data']['UserObject']
    UserID = obj['UserID']
    Email = obj['Email']
    Phone = obj['MobileNumber']

def signup():
    url = sgup_url
    data = [
        ("Salutation", "Mr"),
        ("FirstName", "Anh"),
        ("LastName", "Nguyen"),
        ("MobileNumber", "0985413357"),
        ("EmailAddress", "sieunhantanbao39@mailinator.com"),
        ("CreditCardNumber", "847563"),
        ("Password", "Admin123!@#"),
        ("ConfirmPassword", "Admin123!@#"),
        ("HasAcceptTermAndPolicy", "True"),
    ]

    r = requests.post(url, headers = header, data= data)
    return r.json()