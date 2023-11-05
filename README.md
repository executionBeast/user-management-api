Backend Internship Assignment: User Management System

Objective:
  Create a simple user management system backend using Firebase. The system will provide
  APIs to perform user registrations, user logins, and the ability to retrieve, update, and delete
  user profiles.

Language: Please use Python, FastAPI.


Requirements:

  Firebase Setup:
    Initialize a new Firebase project.
    Use Firebase Authentication to handle user registration and login.
    Use Firebase Firestore as the database to store user details.

  User Registration:
    Create an API endpoint to register new users.
    Store the following user information in Firestore:
    1. username,
    2. email,
    3. full name,
    4. created_at timestamp.

  Use Firebase Authentication to handle the actual user creation.
  Ensure passwords are not stored in Firestore.

  User Login:
    Create an API endpoint to log in users.
    On successful login, return a Firebase Auth token to the user.

  User Profile:
    Create API endpoints to allow users to retrieve and update their profile information (excluding
    password).
    Create an API endpoint to delete a user account.

  Validation and Security:
    Implement input validation for all user inputs.
    Secure the API endpoints so that only authenticated users can access their profiles.

Documentation:
  Provide a Postman collection or equivalent API documentation for interacting with your API.
  Include a README file with setup instructions and any other necessary documentation for your
  project.

Deliverables:
  Source code pushed to a Git repository (e.g., GitHub, GitLab).
  Documentation and setup instructions.

Evaluation Criteria:

Functionality: All endpoints must work as described.

Code Quality: Code should be clean, well-organized, and commented.

Error Handling: The system should gracefully handle and return appropriate error messages.

Security: Implementation of security best practices.

Documentation: Clarity and completeness of documentation.

Bonus Points (Optional):

Implement password reset functionality.

Implement a simple rate limiting mechanism on the API endpoints.

Write a few unit tests for your API endpoints.
Instructions:

You are allowed to use online resources, including documentation and forums, for reference and
learning.

You may also interact with AI tools such as ChatGPT to seek guidance or explanations.

Please submit the repository link and any necessary documentation by the deadline. Good luck,
and we're looking forward to seeing your solution!