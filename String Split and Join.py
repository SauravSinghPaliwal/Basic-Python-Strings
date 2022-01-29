def splitjoin(line):
    Output = line.split();
    Output = "-".join(Output)
    return Output;
    
if __name__ == '__main__':
    line = input()
    result = splitjoin(line)
    print(result)