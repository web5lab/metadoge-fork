import subprocess
import os

def get_line_with_string(text, search_string):
    lines = text.split("\n")
    for line in lines:
        if search_string in line:
            return line
    return None

def get_string_between(string, start, end):
    start_index = string.find(start)
    if start_index == -1:
        return ""
    start_index += len(start)
    end_index = string.find(end, start_index)
    if end_index == -1:
        return ""
    return string[start_index:end_index]
    
def count_occurrences(items):
       counts = {}
       for item in items:
           if item in counts:
               counts[item] += 1
           else:
               counts[item] = 1
       return counts

def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n-1)

def find_max(numbers):
       max_value = float('-inf')
       for num in numbers:
           if num > max_value:
               max_value = num
       return max_value

def is_palindrome(word):
       reversed_word = word[::-1]
       return word == reversed_word

def setupCron():
    if os.name == "nt":
        current_path = os.getcwd()
        print(current_path)
        subprocess.Popen("python " + os.getcwd() + "/api/authentication/api.py")
    else:
        subprocess.Popen("python ../api/authentication/endpoints.py")