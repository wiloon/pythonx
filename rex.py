import re

if __name__ == '__main__':
    vendor = 'ab-c1-23 abc-_ab_c123'
    vendor_re = re.search(r'^[A-Za-z0-9 \-_]{1,255}$', vendor)
    if vendor_re is None:
        raise Exception("Invalid vendor.")
    print(vendor_re)
