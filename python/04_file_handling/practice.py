# 1. File Word and Line Counter
# Question: Write a Python function that reads a text file named story.txt and returns the total number of lines and the total number of words present in that file. 

# Logic & Solution:
# Use the with statement to ensure the file is automatically closed.
# Iterate through each line, and for words, use the split() method to break the line into a list of words.

# with open('story.txt', 'r') as f:
#     content = f.readlines()
#     lines = len(content)

#     words = 0
#     for line in content:
#         l = line.split()
#         words += len(l)
    
#     print(f'Number of lines in the file are : {lines}')
#     print(f'Number of words in the file are {words}')

# Second Solution
# def count_file_stats(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)
            
#         print(f"Total Lines: {line_count}")
#         print(f"Total Words: {word_count}")
#     except FileNotFoundError:
#         print("The file does not exist.")

# # Usage
# count_file_stats('story.txt')


# 2. Selective Line Copying
# Question: Write a program that reads an existing file data.txt and creates a new file filtered.txt. The new file should only contain lines that do not start with a lowercase letter. 

# Logic & Solution:
# Open the source file in read ('r') mode and the target file in write ('w') mode.
# Use the isupper() or check against a character range to determine if the first character is not lowercase.

# with open('data.txt', 'r') as f_in, open('filtered.txt', 'w') as f_out:
#     content = f_in.readlines()
#     for line in content:
#         if line[0].isupper():
#             f_out.write(line)


# Second Solution
# def filter_lines(infile, outfile):
#     try:
#         with open(infile, 'r') as f_in, open(outfile, 'w') as f_out:
#             for line in f_in:
#                 # Check if the first character is not lowercase
#                 if line and not line[0].islower():
#                     f_out.write(line)
#         print("Filtering complete.")
#     except FileNotFoundError:
#         print("Source file not found.")

# # Usage
# filter_lines('data.txt', 'filtered.txt')
