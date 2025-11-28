import gradio as gr

# Simple Bubble Sort with step-by-step output
def bubble_sort_steps(numbers_str):
    # handle bad input safely
    try:
        arr = [int(x) for x in numbers_str.split(",")]
    except:
        return ["Error: please enter a list of integers separated by commas." ]

    steps = []
    n = len(arr)

    # record the initial array
    steps.append(f"Start: {arr}")

    # basic bubble sort (very beginner friendly)
    for i in range(n):
        for j in range(0, n - i - 1):
            # record comparison
            steps.append(f"Comparing {arr[j]} and {arr[j+1]}")

            if arr[j] > arr[j + 1]:
                # swap the values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(f"Swapped → {arr}")
            else:
                steps.append(f"No swap → {arr}")

    steps.append(f"Finished: {arr}")
    return "\n".join(steps)


# GUI
def run_app():
    title = "Bubble Sort Visualizer (CISC 121 Project)"
    description = "Enter numbers separated by commas. The app shows each comparison and swap."

    with gr.Blocks() as demo:
        gr.Markdown("# Bubble Sort Visual Simulation")
        gr.Markdown("Made for CISC 121. Enter a list of integers!")

        input_box = gr.Textbox(label="Enter numbers (ex: 5,3,8,1)")

        output_box = gr.Textbox(label="Step-by-step Result", lines=20)

        run_button = gr.Button("Run Bubble Sort")

        run_button.click(fn=bubble_sort_steps, inputs=input_box, outputs=output_box)

    return demo


app = run_app()

# Only needed for local running:
if __name__ == "__main__":
    app.launch()