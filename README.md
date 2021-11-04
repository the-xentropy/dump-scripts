# dump-scripts

Dumps all scripts on a page to a local directory, including inline scripts.


## Usage

`usage: dump-scripts.py [-h] [--useragent USERAGENT] [--prettify] URL`

e.g. 

`./dump-scripts.py https://reddit.com`

`python3 dump-scripts.py --useragent="haxbot v1337" https://wikipedia.com`

`python3 dump-scripts.py --prettify https://www.example.com`

After which you will have a folder called "scripts" underneath the directory the dump-scripts.py file resides in containing all scripts found on said page.


## Prettifying

dump-scripts relies on [js-beautify](https://github.com/beautify-web/js-beautify) for supporting prettifying all scripts through the `--prettify` flag (this also rudimentarily unminifies/unpacks them). If you want to use it, you have to install the `jsbeautifier` pip package, but I intentionally designed this script so that it will still work without it.

To install the package required:

`$ pip install jsbeautifier`

