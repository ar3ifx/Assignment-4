#Task_1
try:
    with open("sample.txt","rt") as fh:
        content = fh.readlines()
        for line in content:
            print(line)
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found")

#Task_2
with open("output.txt","wt") as fh:
    user_input1=input("Enter text to write to the file: ")
    fh.write(user_input1+'\n')
    print("Data successfully written to output.txt.")
with open("output.txt","at") as fh:
    user_input2=input("Enter additional text to append:  ")
    fh.write(user_input2+'\n')
    print("Data successfully appended.")
with open("output.txt","rt") as fh:
    final_content=fh.readlines()
    print("Final content of output.txt:")
    for line in final_content:
        print(line.rstrip('\n'))

