# Bubble Sort Visual Simulation (CISC 121 Project)

This is a small Python app that visually simulates **Bubble Sort** using **Gradio**.  
The user types a list of integers, and the app shows each comparison and swap step-by-step.

---

## Demo Screenshots

### First test
![Screenshot 1](screenshot1.png)

### Second test
![Screenshot 2](screenshot2.png)

---

## 1. Problem Breakdown & Computational Thinking

### 1.1 Decomposition

I broke the project into these smaller pieces:

- **Input handling**  
  - Read a string from the Gradio textbox (ex: `"5,3,8,1"`).  
  - Split by commas and convert each piece to an `int`.

- **Bubble sort logic**  
  - Use two loops (`i` and `j`).  
  - Compare neighbouring elements `arr[j]` and `arr[j+1]`.  
  - Swap if they are in the wrong order.

- **Recording steps**  
  - Keep a `steps` list of strings.  
  - Add messages like `"Comparing 5 and 3"`, `"Swapped → [3, 5, 8, 1]"`, etc.  
  - At the end, join all steps into one big string for display.

- **User interface (Gradio)**  
  - One textbox for input numbers.  
  - One textbox for all the steps.  
  - One button that runs `bubble_sort_steps(...)` when clicked.

### 1.2 Pattern Recognition

Some patterns I noticed in Bubble Sort:

- On every **pass** of the outer loop, the largest remaining value moves to the right.
- I always compare **neighbouring elements** (`j` and `j+1`).
- The inner loop gets **shorter each pass** (`n - i - 1`) because the last part of the list is already sorted.
- The same compare → maybe swap → move on pattern repeats until the list is sorted.

### 1.3 Abstraction

To keep things simple for the user:

- I only show:
  - The current array
  - Which two numbers are being compared
  - Whether they were swapped or not
- I hide the low-level details like:
  - Exact values of `i` and `j`
  - How Python manages memory or the call stack
- The UI just asks for:
  - A comma-separated list of integers  
    (no need to understand loops or indices to use it).

### 1.4 Algorithm Design

High-level algorithm for my app:

1. **User input**: get a string from the textbox (ex: `"5,3,8,1"`).
2. **Parse input**: split by `","` and try to convert to integers.
   - If this fails, return an error message.
3. **Initialize**:
   - Save the starting array in `steps` as `"Start: [ ... ]"`.
4. **Bubble Sort loops**:
   - For each `i` from `0` to `n-1`:
     - For each `j` from `0` to `n-i-2`:
       - Record `"Comparing a and b"`.
       - If `arr[j] > arr[j+1]`:
         - Swap the two values.
         - Record `"Swapped → [new array]"`.
       - Else:
         - Record `"No swap → [array]"`.
5. **Finish**:
   - Record `"Finished: [sorted array]"`.
   - Join all strings in `steps` with newlines and return that string.
6. **Gradio**:
   - Show the result string in a multiline textbox.

---

## 2. Flowchart
![flowchart](flowchart.png.png)
