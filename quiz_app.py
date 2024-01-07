import sys
import random
import questions
import os
def main():
    # TODO: your code here
    # 1. Get the command line arguments via sys.argv
    amountQues=int(sys.argv[2])
    countQues=0
    count=0
    with open(rf"questions\{sys.argv[1]}.txt") as file:
        for line in file:
            if countQues==amountQues:
                break
            countQues+=1
            line = line.strip()
            q,ans,opt=line.split(';')
            lst=[ans,opt]
            options=[]
            for i in lst:
                options.extend(i.split(","))   
            random.shuffle(options)
            print(q)
            for i, item in enumerate(options):
                print(f'{i+1}. {item}')
            answer= input("Select the correct answer: ")
            answer=int(answer)
            for i, item in enumerate(options):
                if answer==i+1:
                    if item==ans:
                        count+=1
        print(f'You answerd {count}/{amountQues} correct answers')
                    

            
        

            # with open('.\\questions\\' + subject + '.txt') as file:
    # 2. Open the correct file open(rf'questions\<filename>.txt)'
# def calc_question(text):
#  text = text.strip()
#  n1, op, n2 = text.split()
#  n1 = int(n1)
#  n2 = int(n2)
 
#  if op == '+':
#  return n1 + n2
#  if op == '-':
#  return n1 - n2
#  if op == '*':
#  return n1 * n2
    # 3. Iterate over the file

    #       3.1. Parse the line (use s.split())
    #       3.2 Create a list of options
    #       3.3 random.shuffle(l)
#     import os

# folder_name = "questions"
# file_name = f'{sys.argv[1]}.txt'

# # Construct the file path
# file_path = os.path.join(folder_name, file_name)

# # Open the file
# try:
#     with open(file_path, "r") as file:
#         # Perform operations on the file here
#         # For example, you can read its contents using file.read()
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
    pass


if __name__ == '__main__':
    main()
