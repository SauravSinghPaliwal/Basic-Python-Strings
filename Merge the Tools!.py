from collections import OrderedDict
def tools(string, k):

    strlen = len(string)
    for i in range(0,strlen,k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    tools(string, k)