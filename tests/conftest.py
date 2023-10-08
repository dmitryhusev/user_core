import pytest


@pytest.fixture()
def page(playwright, request):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=f"./traces/{request.node.name}.zip")
