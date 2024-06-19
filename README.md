#============================================= RASA===========================================================#

Project Name: RASA-hometest_TaskCLI-API_Test
Description:
This project contains a home test for Task CLI and API automation and continuous integration (CI).

Installation:
Before running the scripts, ensure you have python3, pytest and requests installed. You can install them using pip:
Install python based OS command may vary, python3 used in all platforms see for more info : https://docs.pytest.org/en/7.1.x/getting-started.html
pip install pytest
pip install pytest pytest-html
pip install requests pytest

Running the Tests:
============================
Clone the Repository
Download or pull the code from the GitHub repository using the following command (also shared as a zip file):
git clone https://github.com/ashoknaidu404/RASA.git

After installing the required packages, follow these steps to run the tests:

      Task ClI Autiomation  Tests:
      ==============================
      Navigate to the directory containing rasa_hometest_ashok/task_cli_test and run the following command:
      on WSL or linux flavour 
      pytest task_cli_tests
      on mac OS
      python -m pytest task_cli_tests.py
      Above command executes the tests in task_cli_tests.py using pytest.
      
      Fake Store API Automation  Test:
      =============================
      Navigate to the directory containing rasa_hometest_ashok/fakestoreapitests/ and run the following command:
      on WSL or linux flavour 
      pytest fakestoreapitest.py
      on mac OS
      python -m pytest fakestoreapitest.py
      above  command executes the tests in fakestoreapitest.py using pytest.

Project Folder Structure
-.github
  -rasa_home_test.yml
- rasa_hometest_ashok/
  - fakestoreapitests/
    - fakestoreapitest.py
  - task_cli_test/
    - task_cli_tests.py
  -RASA_Test Cases.pdf
   

Notes: 
Task is not supported on Windows, so Task CLI tests won't work on that platform.
Ensure Python 3.x is installed on your system.
Adjust the paths according to your actual project structure.
CI currently runs only on Ubuntu 
