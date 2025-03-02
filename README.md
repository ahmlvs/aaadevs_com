# aaadevs_com

<a href="https://aaadevs.com" target="_blank"><strong>aaadevs.com</strong></a> is a website project built using **FastAPI**, combining backend and frontend using Jinja2Templates for dynamic HTML rendering.

This project serves as a foundation for further development and is designed to help developers learn and experiment with:

- Using **FastAPI** to build web applications.
- Rendering HTML pages server-side with **Jinja2Templates**.
- Setting up **CI/CD** pipelines with **Docker** and **GitLab**.
- Integrating a Telegram Bot using **aiogram3**. Try bot <a href="https://t.me/aaadevs_bot" target="_blank"><strong>t.me/aaadevs_bot</strong></a>

Feel free to use this project as an example or starting point for your own web applications, contribute to its development, or adapt it to fit your needs. Contributions are welcome!

Currently, the project includes the following components:

- **Home Page**: The main landing page of the website.
- **Static Files**:
  - `robots.txt`: Provides instructions for web crawlers.
  - `sitemap.xml`: Helps search engines index the site's pages.
  - `favicon.ico`: The small icon that appears in the browser tab or bookmark bar.
- **Contact Form Handler**: Processes submissions from a contact form, with logic to handle and send notifications to Telegram Bot.
- **Telegram Bot**: To get notifications from a contact form.

### Table of Contents

- [Backend FastApi](#backend-fastapi)
- [TGBot Aiogram3](#tgbot-aiogram3)
- [CI/CD](#cicd)

---

# Backend FastApi

```bash
cd backend
```

## How to Create and Activate a Virtual Environment

### Create the Virtual Environment

```bash
python3 -m venv env
```

### Activate the Virtual Environment

```bash
source env/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Deactivate the Virtual Environment (if needed)

```bash
deactivate
```

## Add Environment Variables (.env)

Create a .env file in the project root with the following variables:

```env
PROFILES=dev                                        # Use "prod" for production, "dev" for development
ALLOWED_ORIGINS=http://localhost,http://127.0.0.1   # For development
DB_URL=your_database_url                            # Database URL string. For "dev" can be ""
BOT_TOKEN=test:12345                                # Use token from BotFather
ADMINS_LIST=1111111111,1111111112                   # Use user chat id
```

## Run the Application

### Run Locally

```bash
python main.py
```

## How to Test the Application

### Running Tests

To run tests, use the pytest framework. Ensure you have pytest installed:

```bash
pip install pytest
```

Run the tests with the following command:

```bash
pytest
```

### Measure Code Coverage

To measure code coverage, use the pytest-cov plugin. Install it with:

```bash
pip install pytest-cov
```

Run tests with coverage reporting:

```bash
pytest --cov=.
```

### Generate a Coverage Report

To generate a more detailed HTML coverage report:

```bash
pytest --cov=. --cov-report=html
```

The coverage report will be generated in the htmlcov directory. Open the report in your browser:

```bash
open htmlcov/index.html
```

---

# TGBot Aiogram3

```bash
cd tgbot
```

## How to Create and Activate a Virtual Environment

### Create the Virtual Environment

```bash
python3 -m venv env
```

### Activate the Virtual Environment

```bash
source env/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Deactivate the Virtual Environment (if needed)

```bash
deactivate
```

## Add Environment Variables (.env)

Create a .env file in the project root with the following variables:

```env
BOT_TOKEN=test:12345                                # Use token from BotFather
```

## Run the Application

### Run Locally

```bash
python main.py
```

---

# CI/CD

The process of setting up CI/CD using GitLab CI, GitLab Runners, Docker Compose, and Nginx.

## Example of Setting Up a VM (Ubuntu 22.04 LTS) with a Password

## Create the Server and Domain Name

### Set Up the Server:

Create a server (e.g., on AWS, DigitalOcean, Azure, or any cloud provider).
Obtain the server’s IP address: xxx.xxx.xxx.xxx

### Purchase a Domain Name:

Buy a domain name from a registrar (e.g., GoDaddy, Namecheap, or Google Domains).
The domain is required to enable HTTPS.

### Point the Domain to the Server:

Update the domain’s DNS settings to point to your server’s IP address:
Set an A record for @ (root domain) pointing to xxx.xxx.xxx.xxx with a TTL of 1 hour.

### Access the Server via SSH locally

```bash
ssh user@xxx.xxx.xxx.xxx
```

### Install Git

```bash
sudo apt-get update
sudo apt-get install git
```

### Install Docker

Search for the official Docker installation guide (Google: “install docker ubuntu”).
Run the two main like:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Verify the installations

```bash
git --version
docker --version
```

## Installing an SSL Certificate on Server

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
```

Stop the Nginx container temporarily if it’s running:

```bash
docker stop my-nginx-container
```

Obtain the SSL certificate:

```bash
sudo certbot certonly --standalone -d your_domain.com
```

Restart the Nginx container if needed:

```bash
docker start my-nginx-container
```

### Setting Up Certificate Renewal

```bash
sudo crontab -e
```

Add the following line to renew certificates and restart Nginx automatically:

```txt
0 3 * * * certbot renew --quiet && docker stop my-nginx-container && docker start my-nginx-container
```

To test renewal manually:

```bash
sudo certbot renew --dry-run
```

## Setting Up GitLab CI/CD

### Configure GitLab CI/CD:

Go to your GitLab Project Settings > CI/CD > Variables.
Add environment variables required for the application.

### Set Up a GitLab Runner:

In GitLab, go to Settings > CI/CD > Runners.
Uncheck the Enable instance runners for this project option to ensure the runner is project-specific.

Create a New Project-Specific Runner:
We use a Docker container to run the GitLab Runner instead of running it as a standalone service.

### Install GitLab Runner on the Server

Add your user to the Docker group if needed:

```bash
sudo usermod -aG docker $USER
```

Start the GitLab Runner:

```bash
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:alpine
```

Register the Runner:

```bash
docker run --rm -it \
    -v /srv/gitlab-runner/config:/etc/gitlab-runner \
    gitlab/gitlab-runner:alpine register
```

During registration, you’ll need:

- Token: Available in the GitLab project’s CI/CD > Runners settings.
- Executor: Choose `docker`.
- Default Docker Image: Use `docker:dind`.

Update config.toml for the Runner:

```bash
nano /srv/gitlab-runner/config/config.toml
```

Update the volumes section:

```bash
volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
```

### Run the CI/CD Pipeline:

Push your code to GitLab.
The `.gitlab-ci.yml` pipeline uses the `docker-compose.yml` file to build, test, and deploy the backend and Nginx services.
