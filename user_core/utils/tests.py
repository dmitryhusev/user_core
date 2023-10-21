

class RerunErrorHandler:
        # relevant when tests are running with --reruns flag
        
        def __init__(self):
            self.test_name = ''
            self.is_failed = False
            self.count = 0

        def record_trace(self, test_name):
            self.test_name = test_name
            self.is_failed = True
            self.count += 1
