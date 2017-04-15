# coding:utf-8
#
# Author: Masayuki Komai
#


""" imports """
import sys,os
import argparse

""" variables """
""" arguments """
def def_args ():
    parser = argparse.ArgumentParser (
        description="This script is a template for any python scripts.")
    
    parser.add_argument ("-v", "--var", type=str,
                         dest="variable",
                         help=u"message",
                         default=None, 
                         required=True)

    args = parser.parse_args ()    
    options = args.__dict__

    if None in options.values ():
        parser.print_help ()
        exit (-1)
    
    return options

""" functions """

""" main """
def main(options={}):
    print options

if __name__ == "__main__":
    options = def_args ()
    main (options)
