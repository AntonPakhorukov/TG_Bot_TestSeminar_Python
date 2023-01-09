def Decompress(string: str):
        input_str = string
        decompress = ''
        for i in range(0, (len(input_str) - 1), 2):
                decompress += input_str[i + 1] * int(input_str[i])
        return decompress