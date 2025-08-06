# Live Weather App with Flask on EC2

A simple Flask web app that fetches real-time weather data using the free wttr.in API. Deployed on AWS EC2.

## Features
- Enter city name
- Get current temperature and weather description
- Uses free wttr.in API (no API key needed)

## Tech
- Python + Flask
- wttr.in API
- Hosted on AWS EC2

## Run Locally
git clone https://github.com/abir8/weather-app-ec2.git
cd weather-ec2-demo
pip install -r requirements.txt
python app.py

## EC2 Setup (Summarized)
- Launch t2.micro EC2
- Allow port 5000 or set up nginx
- SSH into instance
- Clone repo, install requirements
- Run app

## Live Demo
`http://<your-ec2-ip>:5000`
