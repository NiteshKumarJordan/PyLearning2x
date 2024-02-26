api_response = {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john@example.com",
    "Password": "Jordan",
    "Age": 30,
    "Address": {
        "Street": "123 Main St",
        "City": "New York",
        "State": "NY"},
    "Phone": ["123-456-7890", "987-654-3210"]
}

print(api_response)
print(type(api_response))
print(api_response.get("Password"))

api_response["Password"] = "NITESH JORDAN"
print(api_response)

