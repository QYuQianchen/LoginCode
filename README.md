# Python Auto-Login

This python code helps you to automatically sign up for classes at ASVZ, such as *TRX Suspension Training*, *Sportberatung*, 
*Kraftberatung*, *Cycling Class*, *Rowing Class*.

If you don't know what I'm talking about, you can close the webpage, now. You're welcome.

## Getting Started

### Prerequisites

* Be a member of ASVZ. (Otherwise, ask yourself why you need this...)
* Be a member of ETH. (The default code is built for member of ETH. It can be modified for people who use other SwitchAAI login)
* Chrome and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Python 3.6](https://docs.python.org/3/using/windows.html#installing-python)
* [Selenium](http://www.seleniumhq.org/) browser automation toolkit

### Installing

Let's do it step by step.

Download the AutoLog.py file in your favorite folder.

Use the link above (Or the other file in this repo) to download and unzip ChromeDrive, put the .exe file under the same folder where the AutoLog.py is.

If you don't have Python installed on your pc, download and install it with the link above. Make sure its version is 3.6.x

To install Selenium to Python, open a Command Prompt window and type

```
py -m pip install selenium
```
You should have everything you need installed. 

## Running

It's pretty simple to use it. Just replace some fields in the code with your personal information and run it on the day of registration 
(a couple of hours/minutes before the registration starts). Don't close the Command Prompt/Chrome until the sign-up process is finished.

### Customize the code

Open the AutoLog.py with any text editor you have on your pc. Enter your ETH username and ETH password in line 15 and 16.
```
usernameStr = 'your username'
passwordStr = 'your ETH-password'
```
Go to the website of ASVZ and choose the classe you'd register. (If you don't have it, ask yourself again why you need this code...) 
Replace the *urlStr* and *timeStr* with the URL address of the class desciption page (DETAILAUSSCHREIBUNG) and the starting time of 
the registration. (line 17 and 18)

```
urlStr = 'https://schalter.asvz.ch/tn-mvc/Event/Lesson/Detail/581508'
timeStr = '14:00'
```
Save it.

### On the day of registration

You can start running the code half an hour/a few minutes before the registration time.

Open a Command Prompt and go to the folder that contains the code

```
cd (the repo address)
py AutoLog.py
```
You can now leave the code running and do whatever you want. 
Please don't shut down the cmd window and make sure your pc won't go to sleep. (You can, but not him.) 
You should get the place if you follow the instruction. If not, well, bad luck for you.
Others may use a better code than this one.

## Authors

* **Chenchen** - A student at ETH, who missed signing up for sport classes when working (coding) on her own Master Thesis project.

## License

Well, no License now.

## Acknowledgments

* Please reach out to me for any questions regarding the code.
* Inspired by a conversation with a dear friend.
* Built with love and curiosity.
