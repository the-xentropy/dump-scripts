#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
import os
import hashlib
import argparse


"""
Simple python utility to dump all scripts from a given page.
By: @SamuelAnttila
License: MIT
"""

def download_script(url,downloads_dir_path,headers={}):
    """Download script into given directory. Note: Does nothing to avoid name collisions"""

    # /asdf/file.js?123=123 -> file.js
    url_path = requests.compat.urlparse(url).path
    local_filename = os.path.basename(url_path)

    # streaming file download because putting everything in memory at once is silly
    with requests.get(url, stream=True, headers={}) as r:
        r.raise_for_status()
        with open(os.path.join(downloads_dir_path,local_filename), 'wb+') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename


def ensure_dir(file_path):
    """Ensure directory exists by creating it if not present"""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == "__main__":
    downloads_dirname = "scripts/"
    curr_path = os.path.dirname(os.path.realpath(__file__))
    downloads_path = os.path.join(curr_path,downloads_dirname)
    ensure_dir(downloads_path)

    parser = argparse.ArgumentParser(description='Download all scripts from a website into a scripts/ folder underneath this script')
    parser.add_argument('url', metavar='URL', type=str, help='The url (including schema) from which to dump scripts')
    parser.add_argument('--useragent', dest='useragent', type=str, default="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", help='User agent to use when making requests')
    args = parser.parse_args()

    res = requests.get(args.url,headers={"User-Agent":args.useragent})
    soup = bs(res.text,features="html.parser")
    for script in soup.find_all("script"):
        if "src" in script.attrs:
            #externally loaded script
            download_url = requests.compat.urljoin(args.url, script.attrs["src"])
            print(f'Downloaded {download_script(download_url,downloads_path,headers={"User-Agent":args.useragent})}')
        else:
            #inline script
            print(script.text)
            m = hashlib.sha256()
            m.update(script.text.encode("utf32"))
            local_filename = m.hexdigest() # To give all inline scripts a unique name we take the hash of its contents. Only identical scripts should collide.
            with open(os.path.join(downloads_path,local_filename)+".js", 'w+') as f:
                f.write(script.text)
    print("Done downloading scripts. They should be under the 'scripts/' folder.")



