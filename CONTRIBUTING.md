# Rules & Guidelines for contributors
Welcome to the team! We're excited to have you on board as part of our development team. 
To ensure a smooth and efficient workflow, we've put together some key rules and guidelines. 
Please take a moment to review them before getting started.
## Backend
### First steps:
Please ensure you have Python 3.12.5 installed.
```bash
# Clone the repository to your local system's projects folder
git clone https://github.com/teamfishydino/quizapp.git

# Change the working directory to quizapp/backend
cd ./quizapp/backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On windows
source .venv/Scripts/activate
# On Linux/Mac
source .venv/bin/activate

# Install packages to the virtual environment
pip install -r requirements.txt
```
To deactivate the virtual environment just type `deactivate`.
To activate the virtual environment in your IDE, simply select the Python interpreter from the `.venv/` folder.
___

### Testing
We follow the principles of test-driven development. For new features, please consistently write tests using pytest. You can refer to this 
[FastAPI guide](https://fastapi.tiangolo.com/tutorial/testing/) for more information on how to write tests.
```bash
# Run all tests
pytest

# Run a specific test
pytest tests/test_something.py
```
## Version Control
- Branching: For every task or feature, create a fresh branch.
  - Use the naming conventions: {category}/{short-branch-name-with-hiphens} for example `feature/setup-frontend`    
  - Example categories: bugfix, hotfix, feature, experimental etc.
- For commit messages use our internal fishydino Version Control Policy 
- Pull Requests: Upon completing and testing your feature, initiate a pull request (PR) against the main or the designated development branch.
- Code Reviews: Each PR must undergo a review by at least one developer. Address all comments and feedback before finalizing the merge.
  
## Collaboration & Communication
- Issues: Whenever you come across bugs or have suggestions for new features, please create a relevant GitHub issue. Be sure to provide a clear description and use the appropriate labels for categorization.
- Just ask: Questions? Just ask the team.
- Respect & Open-mindedness: Approach team discussions and critiques with an open mind and heart. Show respect for the diversity of thoughts and contributions.
