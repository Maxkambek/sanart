import requests


def verify(phone, code):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQyNDcsInJvbGUiOiJ1c2VyIiwiZGF0YSI6eyJpZCI6NDI0NywibmFtZSI6Ik9PTyBcIlNBTiBBUlQgQVVDSU9OXCIiLCJlbWFpbCI6InNhbmFydGF1Y3Rpb25AZ21haWwuY29tIiwicm9sZSI6InVzZXIiLCJhcGlfdG9rZW4iOm51bGwsInN0YXR1cyI6ImJsb2NrZWQiLCJzbXNfYXBpX2xvZ2luIjoiZXNraXoyIiwic21zX2FwaV9wYXNzd29yZCI6ImUkJGsheiIsInV6X3ByaWNlIjo1MCwidWNlbGxfcHJpY2UiOjExNSwidGVzdF91Y2VsbF9wcmljZSI6bnVsbCwiYmFsYW5jZSI6MzAwMDAwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6IjIwMjMtMDYtMTVUMDU6NDg6MjcuMDAwMDAwWiIsInVwZGF0ZWRfYXQiOiIyMDIzLTA2LTE1VDA2OjExOjAyLjAwMDAwMFoiLCJ3aGl0ZWxpc3QiOm51bGwsImhhc19wZXJmZWN0dW0iOjB9LCJpYXQiOjE2ODcxNjc0MzIsImV4cCI6MTY4OTc1OTQzMn0.1M1lohrCxUseXioZt5YTrmz3EiZb9QaVlYeI7eRV5Bg"}
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }

    response = requests.post(url=url, data=data, headers=headers)
    return response
