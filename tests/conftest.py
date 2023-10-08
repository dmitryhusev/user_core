import pytest

class RerunErrorHandler:
        record_trace = False
        test_name = None
        count = 0

handler = RerunErrorHandler()

def pytest_exception_interact(call, report):
    handler.test_name = report.head_line
    handler.record_trace = True
    handler.count += 1


@pytest.fixture()
def page(playwright, request):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    if handler.record_trace:
        if request.node.name == handler.test_name:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    if (
         handler.record_trace and
         handler.test_name == request.node.name and
         handler.count > 1):
            context.tracing.stop(path=f"./traces/{request.node.name}.zip")
