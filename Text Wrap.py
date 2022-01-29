import textwrap

def twrap(string, max_width):
    return textwrap.TextWrapper(width=max_width).fill(text=string)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = twrap(string, max_width)
    print(result)
