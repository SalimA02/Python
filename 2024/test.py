def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    dictionary = {}
    decoded_message = ""
    numbers = []

    for line in lines:
        num, word = line.strip().split(' ')
        numbers.append(int(num))
        dictionary[int(num)] = word
        numbersSorted = sorted(numbers)
        
    pyramid = create_staircase(numbersSorted)

    for row in pyramid:
        if decoded_message == "":
            decoded_message = decoded_message+(dictionary[(row[len(row)-1])])
        else:
            decoded_message = decoded_message+" "+(dictionary[(row[len(row)-1])])
    return decoded_message



def create_staircase(nums):
    result = []
    i = 1
    while i * (i + 1) / 2 <= len(nums):
        result.append(nums[int((i - 1) * i / 2):int(i * (i + 1) / 2)])
        i += 1

    
    return result

message = decode('C:/Users/Likkle S/Desktop/SALAH.io/Prayer Times/coding_qual_input.txt')
print(message)