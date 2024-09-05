# Rules & Guidelines for contributors
Welcome to the team! We're excited to have you on board as part of our development team. 
To ensure a smooth and efficient workflow, we've put together some key rules and guidelines. 
Please take a moment to review them before getting started.
- [Backend](#backend)
  - [First steps](#first-steps)
  - [Testing](#testing)
  - [Code quality](#code-qualtiy)
- [Version Control](#version-control)
- [Collaboration & Communication](#collaboration--communication)
## Backend
### First steps:
We recommend using `uv` to manage Python versions, project dependencies, and virtual environments for this project. 
Please follow the [instructions](https://docs.astral.sh/uv/getting-started/installation/) to install it on your system, and refer to the [docs](https://docs.astral.sh/uv/) for more information. 
If you choose not to use `uv`, please ensure you have Python 3.12.5 installed.
```bash
# Clone the repository to your local system's projects folder
git clone https://github.com/teamfishydino/quizapp.git

# Change the working directory to quizapp/backend
cd ./quizapp/backend
```
Setup with `uv`
```bash
# This will create a virtual environment and install required packages
uv sync
```
Setup without `uv`
```bash
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
With an activated virtual environment
```bash
# Run all tests
pytest

# Run a specific test
pytest tests/test_something.py
```
Without an activated virtual environment with `uv`
```bash
# Run all tests
uv run pytest

# Run a specific test
uv run pytest tests/test_something.py
```
### Code qualtiy
#### Linter - Ruff
```bash
# With uv
uv run ruff check

# With an activated environment
ruff check

# Pass the --fix option to automatically fix the fixable errors
uv run ruff check --fix
ruff check --fix
```
If available you can also install the ruff extension to your IDE. 
For more information refer to the [docs](https://docs.astral.sh/ruff/).
#### Formatter - Ruff & isort
```bash
# With uv
uv run ruff format
uv run isort . # you can also pass a file as an arugment

# With an activated environment
ruff format
isort . # you can also pass a file as an arugment
```
For more information refer to the [ruff](https://docs.astral.sh/ruff/) and [isort](https://pycqa.github.io/isort/) docs. 
#### Pre-commit hooks
To simplify the process of maintaining coding quality standards, we've added a pre-commit configuration. This ensures that your code is automatically linted and reformatted before every commit, making it easier to keep everything clean and consistent.   

##### Install the git hook scripts
```bash
# With uv 
uv run pre-commit install

# With an activated environment
pre-commit install
```
Now `pre-commit` will run automatically on `git commit`, checking the files in the staging area. If it finds any errors, it will abort the commit.
It is recommended to run the hooks against all of the files when adding new hooks.
```bash
# With uv 
uv run pre-commit run --all-files

# With an activated environment
pre-commit run --all-files
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
