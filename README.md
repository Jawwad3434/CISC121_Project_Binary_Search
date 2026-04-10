# CISC121_Project_Binary_Search

# Binary Search
I chose binary search because it is an elegant searching method that has a worst-case time complexity of just O(log n). It is one of the most useful methods to search through a sorted list. It can be a list of numbers or anything that can be sorted.
The binary search algorithm repeatedly divides a sorted list in half (usually rounding down) looking for a target:
- It checks the middle value for the target value
- If the target is larger, searches the right half by moving the left pointer 1 index right of middle
- If target is smaller, searches the left half by moving right pointer 1 index left of middle
- Repeats until target found or until exhuasted and there is no target

## Demo video/screenshot of test
Video of demo linked here:
https://youtu.be/G0qNTl__hfg
### Testing
- Target Found (2 images stitched together)
<img width="1960" height="1612" alt="Target Found" src="https://github.com/user-attachments/assets/671ab6e4-5aa8-4f42-82c4-d232fd561253" />

- Target Not Found (2 images stitched together)
<img width="1984" height="1770" alt="Target Not Found" src="https://github.com/user-attachments/assets/7ac9d4df-58c5-4259-9d94-5a1c6aba331a" />

- Hidden Array Test (2 images stitched together)
<img width="1601" height="2243" alt="Hidden Array Test" src="https://github.com/user-attachments/assets/a54aecca-3d34-484a-977d-a2aa4d8cd75b" />

- Many Elements in Array Test
<img width="1849" height="1086" alt="Long Array Test" src="https://github.com/user-attachments/assets/37ce1d3b-81af-4faa-a371-7d3e6e1d3254" />

- Single Array Test Manual
<img width="1090" height="1114" alt="Single Array Test" src="https://github.com/user-attachments/assets/01de9e49-5b70-499b-9622-c4c3850e6680" />

- Letter Error
<img width="1296" height="614" alt="Letter Error" src="https://github.com/user-attachments/assets/a8741b03-2826-4ed5-9ddf-73d9096d6563" />

- Decimal Number Error
<img width="1336" height="714" alt="Decimal Error" src="https://github.com/user-attachments/assets/f1101f28-9c48-4822-a9c6-a6e771a211f7" />

- Comma/Space/Null in Array Error
<img width="1287" height="694" alt="Comma Space Error" src="https://github.com/user-attachments/assets/9b52e163-a64b-4528-863d-1de3f8f525b7" />

- Negative Number of Values Error 
<img width="1220" height="1036" alt="Negative # Values Error" src="https://github.com/user-attachments/assets/96d99908-3873-44d2-941f-51ba98401b08" />

- Empty Array Error Manual
<img width="1240" height="668" alt="Empty Manual Error" src="https://github.com/user-attachments/assets/48d2d750-8ae1-4615-adeb-9c5f81ebf9a2" />

- Empty Array Error Random
<img width="1241" height="1053" alt="Empty Random Error" src="https://github.com/user-attachments/assets/f37cdff7-ae9e-4537-9e59-c33fdbdcf148" />


### Features
This project is an interactive visualization tool that demonstrates how the binary search algorithm works step-by-step. Users can either generate a random sorted array or input their own custom array, and observe how the algorithm narrows down the search range.
- Visual step-by-step binary search
- Random array generation with adjustable bounds
- Manual array input
- Highlighted midpoint and search range
- Negative values displayed downward
- Found target highlighted in green
- Optional hidden array mode (progressive reveal)

## Problem Breakdown & Computational Thinking
### Decompisition 
- Instead of searching through a large sorted list linearly, binary search involves breaking the list into smaller sections, a lower half and upper half.
- The problem is reduced iteratively. If the target is not in the middle, you search the remaining half.

### Pattern Recognition
- Recognizing that the data is sorted allows the algorithm to skip large parts, patterns like 'divide and conquer'.
- With a repeated structure, use that logic. Finding the middle, comparing the target, and splitting the array. This repeating in every step lets us make a loop or recursive function.

### Abstraction
- Focus only on the middle, lower bound, and upper bound to find the next search range.
- Ignore values in the discarded half and use a general model to pick which half to search, like target < mid means search left, which works for any sorted list regardless of size.

### Algorithm Design
- Using two different modes, the user will control the inputs. In 'Random' mode, the user will choose the bounds and number of elements for a sorted random array, also choosing the target. In 'Manual' mode, the user will input the array and the target. The program will then sort the random array or user array. It will iterate through the array and either find the target or not, using the binary search shown above. It will then output how many steps it took as well as which values and indices it checked. This output will be visual and written.


## Steps to Run
Download the files in this repository. Then:
In Bash, you can 

```
pip install gradio
```

then run 

```
python app.py
```

Or use the Hugging Face link to access the app (Linked below).

## [Hugging Face Link] https://huggingface.co/spaces/Jawwad3434/Interactive_Binary_Search_Project_CISC121

## Acknowledgment
The code was partly made by Google's Gemini 3 Flash AI LLM using prompts I gave to it. 
