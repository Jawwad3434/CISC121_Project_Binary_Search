import gradio as gr
import random 


# Binary Search Logic
def binary_search(arr, target):
    """
    Performs binary search on a sorted array.

    Returns:
        steps: list of tuples (left, right, mid)
    """
    steps = []
    left, right = 0, len(arr) - 1

    # Continue searching while the search space is valid
    while left <= right:
        # Calculate the middle index and steps
        mid = (left + right) // 2
        steps.append((left, right, mid))  # store indices

        # Check if target is present at mid
        if arr[mid] == target:
            return steps

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target was not present in the list
    return steps


# Random Array Generator
def generate_array(size, low, high):
    """
    Generates a sorted random array.
    """
    arr = [random.randint(low, high) for i in range(size)]
    arr.sort()
    return arr


# Visualization Function (HTML Bar Chart)
def render_bars(arr, left, right, mid, reveal_full, revealed_set, found_index=None):
    """
    Creates an HTML bar chart showing:
    - Active search region
    - Current midpoint
    - Previously revealed values
    - Found target (green)
    """
    
    if not arr:
        return "<p>Empty array</p>"

    max_val = max(abs(x) for x in arr) + 1

    html = """
    <div style='display:flex; justify-content:center; margin-bottom:30px;'>
    <div style='display:flex; align-items:flex-end; gap:10px; height:400px; position:relative;'>

    <!-- Baseline (zero line) -->
    <div style='position:absolute; top:50%; left:0; right:0; height:2px; background:#ccc;'></div>
    """

    for i, val in enumerate(arr):

        # Height And Direction
        if reveal_full:
            # True proportional height
            height = (abs(val) / max_val) * 140 + 20
        
            # True direction
            if val >= 0:
                bar_style = f"bottom:50%; height:{height}px;"
            else:
                bar_style = f"top:50%; height:{height}px;"

        else:
            # Hidden: Uniform Height
            height = 60
        
            # Hidden: All Bars Upward
            bar_style = f"bottom:50%; height:{height}px;"
        
        # Colours
        if i < left or i > right:
            color = "#e0e0e0" # outside search range
        elif i == mid:
            color = "#ff7675" # current midpoint
        else:
            color = "#74b9ff" # active search range

        if found_index is not None and i == found_index:
            color = "#55efc4" # found target

        # Labels
        if reveal_full or i in revealed_set:
            label = str(val)
        else:
            label = "?"

        # HTML For Each Bar
        html += f"""
        <div style='display:flex; flex-direction:column; align-items:center; width:30px;'>

            <!-- Bar container -->
            <div style='position:relative; height:300px; width:100%;'>

                <!-- Actual bar -->
                <div style='position:absolute;
                            width:24px;
                            left:50%;
                            transform:translateX(-50%);
                            {bar_style}
                            background:{color};
                            border-radius:10px;'>
                </div>
            </div>

            <!-- Label BELOW bars (never overlaps) -->
            <div style='font-size:14px; margin-top:8px; height:20px;'>
                {label}
            </div>
        </div>
        """

    html += "</div></div>"
    return html





# Main Function (Run Everything)
def run_visual(input_mode, user_input, size, low, high, target, reveal_full):
    """
    Main driver function:
    - Builds array
    - Runs binary search
    - Generates all visualization steps
    """
    try:
        # Build Array
        if input_mode == "Random":
            arr = generate_array(int(size), int(low), int(high))
        else:
            if not user_input.strip():
                return [], "Error", gr.update(max=1, value=0)
            arr = list(map(int, user_input.split(",")))
            arr.sort()

        target = int(target)
        
        # Run Binary Search
        steps = binary_search(arr, target)

        visuals = []
        descriptions = []

        revealed_set = set()
        found_index = None

        # Go Through All Steps
        for step_num, (left, right, mid) in enumerate(steps):
            revealed_set.add(mid)

            if arr[mid] == target:
                found_index = mid

            visuals.append(
                render_bars(
                    arr, left, right, mid,
                    reveal_full, 
                    revealed_set, 
                    found_index
                )
            )

            descriptions.append(
                f"Step {step_num+1}: Checking index {mid} (value = {arr[mid]})"
            )

        if found_index is None:
            descriptions.append("Target not found.")
            visuals.append("<p style='text-align:center; color:orange;'>Target Not Found</p>")
        else:
            descriptions.append(f"Target found at index {found_index}")
            visuals.append("<p style='text-align:center; color:green;'>Target Found</p>")
        
        return "<br>".join(visuals), "\n".join(descriptions)

    except Exception as e:
        return f"<p>{str(e)}</p>", "Error"


# User Interface
with gr.Blocks(title="Interactive Binary Search") as demo:
    gr.Markdown("Interactive Binary Search")
    
    # Random Tab 
    with gr.Tab("Random"):
        size = gr.Number(value=20, label="Number of values")
        low = gr.Number(value=-100, label="Minimum value")
        high = gr.Number(value=100, label="Maximum value")
        target_r = gr.Number(label="Target value")
        reveal_r = gr.Checkbox(label="Reveal full array", value=True)

        run_btn_r = gr.Button("Run Binary Search")
        
        output_html_r = gr.HTML(label="Visualization", elem_id="centered")
        output_text_r = gr.Textbox(label="Steps")
        
        # Run
        run_btn_r.click(
            lambda s,l,h,t,r: run_visual("Random","",s,l,h,t,r),
            inputs=[size, low, high, target_r, reveal_r],
            outputs=[output_html_r, output_text_r]
        )
    
    # Manual Tab
    with gr.Tab("Manual"):
        user_input = gr.Textbox(
            label="Custom Array",
            placeholder="e.g. 5, -2, 10, 3"
        )

        target_m = gr.Number(label="Target value")

        run_btn_m = gr.Button("Run Binary Search")

        output_html_m = gr.HTML(label="Visualization", elem_id="centered")
        output_text_m = gr.Textbox(label="Steps")

        # Run
        run_btn_m.click(
            lambda u,t: run_visual("Manual",u,0,0,0,t,True),
            inputs=[user_input, target_m],
            outputs=[output_html_m, output_text_m]
        )
    

demo.launch(theme=gr.themes.Soft(), css="#centered {text-align: center;}")
