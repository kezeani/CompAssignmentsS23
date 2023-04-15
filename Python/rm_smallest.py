def rm_smallest(d):
    ans = d
    length = len(ans)
    keys = list(ans)
    if length == 0 or length == 1:
        return {}
    else:
        lst = list(ans.values())
        min = lst[0]
        index = 0
        for i in range(len(lst)):
            if lst[i] < min:
                min = lst[i]
                index = i
        del ans[keys[index]]
    print(ans)
    return ans

    
def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()