class TraceLogger:
    def __init__(self):
        self.steps = []

    def log(self, step_type, **kwargs):
        self.steps.append({
            "type": step_type,
            **kwargs
        })

    def print_summary(self):
        print("\nTRACE SUMMARY\n")

        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")