def Compress(string: str):
        i = 0
        compress = ''
        while i < len(string):
            count = 1
            while (i+1 < len(string)) and (string[i] == string[i+1]):
                count += 1
                i += 1
            compress += str(count) + string[i]
            i += 1
        return compress

