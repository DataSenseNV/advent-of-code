
# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1
import re

if __name__ == "__main__":
    print("Here I go! Wish me luck!")

def extract_digits(input):
    digit_mapping = {
        'one': '1', 
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    summary = {'first': {}, 'last': {}}
    
    for key, value in digit_mapping.items():
        first = []
        last = []
        for match in re.finditer(key, input):
            first.append(match.start())
            last.append(match.end())
        
        for match in re.finditer(value, input):
            first.append(match.start())
            last.append(match.end())

        if len(first) > 0:
            summary['first'][value] = min(first)   
        if len(last) > 0:
            summary['last'][value] = max(last)   
    
    return int(min(summary['first'], key=summary['first'].get) + max(summary['last'], key=summary['last'].get))
    
def calculate_calibration_value (input):
    return sum([extract_digits(i.strip()) for i in input.strip().split("\n")])     