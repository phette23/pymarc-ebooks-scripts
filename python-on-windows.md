# Setting Up Python on Windows

Lines beginning with "PS" are commands to be typed into Windows Powershell. Don't type the "PS" part.

Download 2.7.4: http://www.python.org/download/releases/2.7.4/

I used 64bit, instructions differ for 32.

Go to Control Panel > System > Advanced system settings > Environment Variables
Scroll down to Path in the bottom list, edit Path and append ";C:\Python27;C:\Python27\Scripts" to its value (very important to do this verbatim, leaving off the leading semicolon will break everything)

2nd directory ("Scripts") is to get `easy_install` on the path

Run ez_setup.py script downloaded from here: https://pypi.python.org/pypi/setuptools

It was at http://peak.telecommunity.com/dist/ez_setup.py when I visited last.

```
PS python ez_setup.py
```

Install pip

```
PS easy_install pip
```

Install pymarc

```
PS pip install pymarc
```

You're done.

To execute scripts, just run
```
PS python script_name.py
```
