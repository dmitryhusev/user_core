import pytest
from user_core.utils.tests import RerunErrorHandler
import os


RERUNS = os.getenv('RERUNS', 1)

handler = RerunErrorHandler()

def pytest_exception_interact(report):
    handler.record_trace(report.head_line)


@pytest.fixture()
def page(playwright, request):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    if handler.is_failed and handler.count == RERUNS:
        if request.node.name == handler.test_name:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    if handler.count == RERUNS + 1:
        handler.reset_state()
        context.tracing.stop(path=f"./traces/{request.node.name}.zip")
