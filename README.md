# Bubble Sort Visual Simulation (CISC 121 Project)

This is my small Python app for the CISC 121 final project.  
I chose **Bubble Sort** because it's one of the first algorithms we learned, and it is easy to show step-by-step.  
The program takes a list of integers and shows every comparison and swap using a simple Gradio interface.

---

## Demo Screenshot
### First test
![Screenshot 1](screenshot1.png)

### Second test
![Screenshot 2](screenshot2.png)

---

# Problem Breakdown & Computational Thinking

### 1. **Decomposition**
Bubble sort can be broken into these small parts:
- Look at two numbers beside each other
- Compare them
- If the first one is bigger, swap them
- Keep looping through the list until everything is sorted
- Show each step to the user in the GUI

### 2. **Pattern Recognition**
- The algorithm repeatedly compares pairs of values
- The biggest values “bubble up” to the end of the list
- The same pattern repeats inside nested loops

### 3. **Abstraction**
To keep the app simple, I only show:
- The pair being compared
- Whether a swap happened
- The array after each update

I do **not** show:
- Internal loop counters  
- Memory addresses  
- Python internal mechanics  

### 4. **Algorithm Design**
**Input:** a string of comma-separated integers  
**Processing:** bubble sort with recorded steps  
**Output:** a list of text steps displayed in order  

**Flowchart (simple):**

Start
↓
User enters numbers
↓
Convert text → list of ints
↓
For i in range(n):
For j in range(n-i-1):
Compare arr[j] and arr[j+1]
If arr[j] > arr[j+1] → swap
Record step
↓
Show final sorted list
↓
End


---

# Steps to Run (Local)

1. Install requirements:


pip install -r requirements.txt


2. Run:


python app.py


3. Gradio will open a local link in your browser.

---

# Hugging Face Link
*(Add your Hugging Face Space link here after you deploy it)*

---

# Testing & Verification

I tested my app using:
- An already sorted list: `1,2,3,4`
- Reverse order: `9,8,7,6`
- Random lists
- Repeated values: `5,5,2,9`
- Bad input (like letters) → correctly shows an error message

Screenshots of tests are included in the repo.

---

# Author & Acknowledgment

Made by **Ramez Mina**, Queen’s University, CISC 121.  
AI (ChatGPT) was used at Level 4 for help with formatting and debugging,  
but all logic and code was written by me.