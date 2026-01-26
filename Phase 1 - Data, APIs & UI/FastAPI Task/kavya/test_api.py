import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_employee():
    payload = {
        "name": "Kavya Test",
        "email": "kavya@example.com",
        "department": "AI Engineering"
    }
    
    print("--- Testing CREATE ---")
    response = requests.post(f"{BASE_URL}/employees/", json=payload)
    
    if response.status_code == 200:
        print("Success! Employee created.")
        print("Response:", response.json())
        return response.json()["id"]
    else:
        print(f"Failed. Status: {response.status_code}")
        print("Error:", response.text)
        return None

def test_get_employees():
    print("\n--- Testing READ ---")
    response = requests.get(f"{BASE_URL}/employees/")
    if response.status_code == 200:
        print(f"Found {len(response.json())} employees in Neon DB.")
    else:
        print("Error fetching employees.")

if __name__ == "__main__":
    # 1. Make sure your uvicorn server is running in another terminal!
    emp_id = test_create_employee()
    if emp_id:
        test_get_employees()