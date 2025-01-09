# Network

**Network** is a social media platform created as part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course. This web application allows users to create posts, follow other users, and interact with posts by liking and commenting. The project utilizes the **Django** framework to implement essential social media features, focusing on user authentication, post management, and a real-time feed of user activities.

## About the Project
In this project, I built a simplified social media application with the following features:
- **User Authentication**: Users can sign up, log in, and log out.
- **Creating Posts**: Users can create and view posts made by others.
- **Follow System**: Users can follow and unfollow other users.
- **Likes & Comments**: Users can like and comment on posts.
- **Profile Page**: Each user has a profile page that displays their posts and followed users.
  
The project is built using **Django**, utilizing its powerful ORM and templating system. It also incorporates JavaScript for handling dynamic actions like liking and commenting without needing to reload the page.

## Features
- **User Authentication**: Secure login and registration system.
- **User Profiles**: View and edit user profiles.
- **Post Creation**: Post text and images.
- **Following System**: Follow other users to see their posts in your feed.
- **Like & Comment System**: Interact with posts by liking and commenting.
- **Real-time Updates**: Use JavaScript to dynamically update post interactions (likes/comments).

## Technologies Used
- **Python**  
- **Django**  
- **HTML/CSS**  
- **JavaScript**  
- **SQLite** (for database storage)

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lonyasha/cs50w-network.git
2. **Navigate into the project directory**:
   ```bash
   cd cs50w-network
3. **Create a virtual environment**:
      ```bash
      python3 -m venv venv
4. **Activate the virtual environment**:
   - For **Windows**:
     ```bash
     venv\Scripts\activate
   - For **MacOS/Linux**:
     ```bash
     source venv/bin/activate
5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
6. **Run the migrations to set up the database**:
   ```bash
   python manage.py migrate
7. **Create a superuser to access the admin panel (optional)**:
   ```bash
   python manage.py createsuperuser
8. **Run the server**:
   ```bash
   python manage.py runserver

### Key Points:
- All installation and setup instructions are placed in properly formatted code blocks.
- This allows for easy copying and pasting directly into the terminal.

---

This project is a part of **[CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)** course by Harvard University. The course provided a comprehensive introduction to web development, and this project was designed to showcase the skills learned throughout the course.

Thank you for visiting! 🎉
