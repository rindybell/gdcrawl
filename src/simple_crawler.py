# coding:utf-8
#
# Author: Masayuki Komai
#


""" imports """
import sys
import os
import argparse
import yaml
import urllib
import urllib2
import urlparse
import time

""" variables """
""" arguments """


def def_args():
    parser = argparse.ArgumentParser(
        description="simple crawler")

    parser.add_argument("-c", "--config", type=str,
                        dest="CONFIG",
                        help=u"config file",
                        default=None,
                        required=True)

    args = parser.parse_args()
    options = args.__dict__

    if None in options.values():
        parser.print_help()
        exit(-1)

    return options


# mkdir support fun
def try_makedir(filepath):
    if os.path.exists(filepath):
        return
    else:
        try:
            os.makedirs(filepath)
        except:
            sys.stderr.write("can't make dir")

    return


# fetch
def fetch_linear_pages(options):
    for index in xrange(options["start"], options["end"] + 1):
        url_path = options["base_URL"].format(index)
        print url_path
        item_path = "{}.html".format(index)
        save_path = os.path.join(options["savefolder"], item_path)
        urllib.urlretrieve(url_path, save_path)

        time.sleep(options["sleep_time"])

# main


def main(options={}):
    with open(options["CONFIG"]) as fconfig:
        config = yaml.load(fconfig.read())

    try_makedir(config["savefolder"])

    if config['fetch_pattern'] == 'linear':
        fetch_linear_pages(config)

if __name__ == "__main__":
    options = def_args()
    main(options)
