# Canvas Helper
Canvas Helper is an app to show the Canvas assignments on the desktop.
## Preview
## How to use
### 1. Install python3 and its library
- If you haven't install python3, please log on https://www.python.org/ and install python3.
- If you have install python3, please follow these steps:
  1. Use `win + R` and enter `cmd` to open Command Prompt.
  2. Enter `pip install pyautogui`.
  3. Enter `pip install ctypes`.
  4. Enter `pip install requests`.
  5. Enter `pip install configparser`.
  6. Enter `pip install playsound`.
### 2. Install CanvasHelper
- You can find the latest version in `release`. (Now, the latest version is `2.0.0`)
- Download `CanvasHelper.zip`.
- Extract it to folder.
### 3. Configure
- Find `config.ini` file, and open it with `Notepad`.
- Log on your personal Canvas page and find `Calendar` on the left side of the homepage.
- Find `Calendar Feed` and click it.
- Copy all the text in the textbox and paste it behind `url = ` in `config.ini`.

  Example: `url = https://jicanvas.com/feeds/calendars/user_aaaaaaaaaaaaaaa`.
- Choose your favourite theme. (Now we only have `Railgun`)
- Close `config.ini`.
### 4. Start
- Open `CanvasHelper.exe` to start software.
- You can right click on the text to show the menu: `Update` and `Quit`.
  - Click `Update` to update your newest assignments.
  - Click `Quit` to quit the software.
## Bug Report
You can open an issue and report your problems.
## Works Cited
linsyking / CanvasHelper: https://github.com/linsyking/CanvasHelper.
## Contact
Email: linzixiang@sjtu.edu.cn