def mutate(string, position, character):
    pos = position+1
    Output = string[:position]+character+string[pos:]
    return Output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    new_string = mutate(s, int(i), c)
    print(new_string)