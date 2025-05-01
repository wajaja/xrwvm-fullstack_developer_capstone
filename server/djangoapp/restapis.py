import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """
    Make a GET request to the specified backend endpoint.
    Args:
        endpoint (str): The API endpoint to call
        **kwargs: Query parameters to include in the request
    Returns:
        dict: JSON response from the server or None if request fails
    """
    params = "&".join([f"{k}={v}" for k, v in kwargs.items()])
    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {"error": str(e)}


def analyze_review_sentiments(text):
    """
    Analyze the sentiment of the given text .
    Args:
        text (str): The review text to analyze
    Returns:
        dict: Sentiment analysis results or error message
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Sentiment analysis failed: {e}")
        return {"sentiment": "neutral", "error": str(e)}


def post_review(data_dict):
    """
    Post a review to the backend service.
    Args:
        data_dict (dict): Review data to post
    Returns:
        dict: Response from server or error message
    """
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(
            request_url,
            json=data_dict,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to post review: {e}")
        return {"status": "error", "message": str(e)}
