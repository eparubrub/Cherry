# Mr.Snooze
Mr. Snooze is a program intended to help ensure rapid checkouts on retail sites.

## Current Functionality
Right now, the program is under development to support SupremeNewYork.com

## Installation
Currently, there is no "nice way" of properly installing everything and the installation process 
 still needs to be developed for easier use. 1st you will need to install a proper 
 [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) into 
 the /helper_utilities folder. Make sure you pick the proper chromedriver according to your
 [chrome version](https://www.whatversion.net/chrome/). 2nd you will need to make sure that you 
 have the [selenium](https://pypi.org/project/selenium/) python package installed as well. Lastly, 
 make sure that you have python 3.6 or above installed.
 
## Usage
In order to use the program right now, you will need to do a bit of coding. First you will have to 
 enter the appropriate information into the **UserPackage.py** file. Next you will have to look into the 
 **Supreme.py** file in order to check current configurations. By default, the main functionality is in the 
 **checkout_no_profile()** function which will create a new instance, and check out by entering in all 
 information by typing into selected element fields on the checkout page. There is a way of checking out with
 autofill that is still currently under development. It first requires the user to use the **setup()** function 
 first, where the user will login and install the autofill extension, then use the **checkout_with_profile()** 
 function to run the script with autofill.

In order to run the program simply enter this into terminal:
```terminal
python Supreme.py
```

## Development
Pull requests are welcome. Please contact me if you would like to contribute to the repository. If there 
 is any confusion please contact me so I can update the README with more information.


