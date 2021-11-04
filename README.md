# dump-scripts

Dumps all scripts on a page to a local directory, including inline scripts.


## Usage

`usage: dump-scripts.py [-h] [--useragent USERAGENT] URL`

e.g. 

`./dump-scripts.py https://reddit.com`

`python3 dump-scripts.py --useragent="haxbot v1337" https://wikipedia.com`

After which you will have a folder called "scripts" underneath the directory the dump-scripts.py file resides in containing all scripts found on said page.

