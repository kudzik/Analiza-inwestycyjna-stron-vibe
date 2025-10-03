import gradio as gr

def shout(message, intensity):
    return "Hello, " + message + "!" * int(intensity)

demo = gr.Interface(
    fn=shout,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
