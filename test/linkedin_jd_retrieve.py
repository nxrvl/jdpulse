import requests

url = "https://api.linkedin.com/v2/jobs/3422079787"
headers = {
  "Authorization": "Bearer {Z1g053r8F6I9SP69}",
  "X-RestLi-Protocol-Version": "2.0.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
  job_data = response.json()
  print("Job Title:", job_data["title"])
  print("Job Description:", job_data["description"])
  print("Company Name:", job_data["company"]["name"])
else:
  print("Failed to retrieve job information, status code:", response.status_code)
