from django.conf import settings
from django.http import JsonResponse
import requests
import json

url = "https://app.loops.so/api/v1/transactional"
authorization_token = settings.LOOPS_API_KEY


def send_welcome_email(email, name):
    try:
        payload = {
            "email": email,
            "transactionalId": "clrxm539201hk267xpve25i24",
            "dataVariables": {"name": name, "email": email},
        }

        json_payload = json.dumps(payload)

        headers = {
            "Authorization": f"Bearer {authorization_token}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, data=json_payload)

        if response.status_code == 200:
            return JsonResponse({"data": response.json()})
        else:
            # If the request is not successful, handle the error
            return JsonResponse(
                {
                    "error": f"HTTP request failed with status code {response.status_code}"
                },
                status=response.status_code,
            )
    except requests.exceptions.RequestException as e:
        # Handle connection errors or timeouts
        return JsonResponse({"error": f"HTTP request failed: {e}"}, status=500)
    except Exception as e:
        # Handle other unexpected errors
        return JsonResponse({"error": f"An unexpected error occurred: {e}"}, status=500)
