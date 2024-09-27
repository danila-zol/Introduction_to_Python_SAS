def event_handler(event_name):
    def callback(*args, **kwargs):
        print(f"Event '{event_name}' triggered with args: {args}, kwargs: {kwargs}")
    return callback

button_click = event_handler("button_click")
button_click("left_click", x=100, y=200)