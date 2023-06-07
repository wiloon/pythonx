if __name__ == '__main__':
    d = {
        "key0": "value0",
        "key1": "value1",
    }

    # print('key0' in d.keys())
    # print(d["key0"])
    # print('key2' in d.keys())
    print("key1" in d)
    print("key2" in d)
    print("key2" not in d or d["key2"] is None)
    #print(d["key2"])
    # print('key0' in "foo")

    # s="foo"
    # s["bar"]
