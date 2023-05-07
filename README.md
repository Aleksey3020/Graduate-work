# Graduate-work
***
## About this framework:
***
Current framework was created to test functionality of https://galanteya.by/. 
Current framework was created using **Python + Pytest + Selenium + Allure**. 

## How to run tests:
***
First of all it's required to clone this repository using:

`git clone https://github.com/Aleksey3020/Graduate-work.git`

Then you need to install all the dependencies:

`pip install -r requirements.txt`

AAfter completing all the above steps, you can run the tests.

Tests are run by default Python commands from the framework 
root folder:
```
- pytest --alluredir=logs --reruns 5 .\test\ 
- pytest .\test\
```
After tests are finished you need to run:

`allure serve logs`

To create a test report.