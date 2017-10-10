
## Hello Google (Selenium with Python)

### WHAT IT IS:
This is a HelloWorld kind of application to use Selenium with several explorers and open google page and search for ""Hello Google".

### REQUIREMENTS:
It requires:
* Mac-OSx
* Ant
* Python2.7
* PIP (Python's tools)
* Selenium

### HOW TO RUN IT:
1. Clone the sources using ```git clone https://github.com/jmcruz1983/HelloGoogle.git```
2. Install Python2.7 using Mac-OSx installer [python-2.7.14-macosx10.6.pkg](https://www.python.org/ftp/python/2.7.14/python-2.7.14-macosx10.6.pkg). See [instructions](https://www.python.org/downloads/release/python-2714/).
3. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) for PIP installation. See [instructions](https://pip.pypa.io/en/stable/installing/).
4. Install PIP using command ```python get-pip.py```
5. Install Selenium using ```pip install selenium```. See [instructions](http://selenium-python.readthedocs.io/installation.html).
6. Go into the directory with ``` cd HelloGoogle```.
7. Install ant with following script ``` source setup.sh```.
8. Run the application using chrome driver with ```ant chrome```. 
    1. If you want to run it with firefox instead use ```ant firefox```.