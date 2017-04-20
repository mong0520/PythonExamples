#!/usr/bin/env python
# ref: http://pythonhosted.org/tendo/

from tendo import singleton
import time
me = singleton.SingleInstance()


def main():
    while True:
        print 'Program is running'
        time.sleep(1)

if __name__ == '__main__':
    main()
