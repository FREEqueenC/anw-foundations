import pytest
from playwright.sync_api import Page, expect
import os
import re

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "permissions": ["clipboard-read", "clipboard-write"]
    }

def test_handle_copy_email(page: Page):
    file_url = f"file://{os.path.abspath('index.html')}"
    page.goto(file_url)

    # Setup elements
    email_link = page.locator("#email-link")
    expect(email_link).to_be_visible()
    feedback = page.locator("#copyFeedback")
    copy_btn = page.locator("#copyEmailBtn")
    copy_icon = copy_btn.locator("i")

    # Verify initial state
    expect(feedback).to_have_class(re.compile(r".*\bopacity-0\b.*"))
    expect(copy_icon).to_have_class(re.compile(r".*\bfa-copy\b.*"))

    # ACTION 1: Click the copy button
    copy_btn.evaluate("element => element.click()")

    # VERIFY 1: Clipboard
    clipboard_content = page.evaluate("navigator.clipboard.readText()")
    assert clipboard_content == "ashleighwalker@anwfoundations.com"

    # VERIFY 1: Visual feedback immediately after click
    expect(feedback).to_have_class(re.compile(r".*\bopacity-100\b.*"))
    expect(copy_icon).to_have_class(re.compile(r".*\bfa-check\b.*"))

    # VERIFY 1: Visual feedback after timeout resets
    page.wait_for_timeout(2500)
    expect(feedback).to_have_class(re.compile(r".*\bopacity-0\b.*"))
    expect(copy_icon).to_have_class(re.compile(r".*\bfa-copy\b.*"))

    # ACTION 2: Click the email link itself
    page.evaluate("navigator.clipboard.writeText('')") # Reset clipboard
    assert page.evaluate("navigator.clipboard.readText()") == ""

    # Use page.evaluate to trigger the click handler to avoid navigation
    page.evaluate("""() => {
        const emailLink = document.getElementById('email-link');
        const event = new MouseEvent('click', { bubbles: true, cancelable: true });
        // Prevent default to avoid navigation away from test page
        emailLink.addEventListener('click', (e) => e.preventDefault(), { once: true });
        emailLink.dispatchEvent(event);
    }""")

    # VERIFY 2: Clipboard
    page.wait_for_timeout(500)
    clipboard_content = page.evaluate("navigator.clipboard.readText()")
    assert clipboard_content == "ashleighwalker@anwfoundations.com"

    # VERIFY 2: Visual feedback
    expect(feedback).to_have_class(re.compile(r".*\bopacity-100\b.*"))
    expect(copy_icon).to_have_class(re.compile(r".*\bfa-check\b.*"))

    # ACTION 3: Fast double click to test timeout clearing
    page.wait_for_timeout(2500) # Reset again
    expect(feedback).to_have_class(re.compile(r".*\bopacity-0\b.*"))

    copy_btn.evaluate("element => element.click()")
    page.wait_for_timeout(1000) # Wait 1 second
    expect(feedback).to_have_class(re.compile(r".*\bopacity-100\b.*"))
    copy_btn.evaluate("element => element.click()") # Click again
    page.wait_for_timeout(1500) # Wait 1.5s more (total 2.5s since first click, but 1.5s since second click)

    # Feedback should still be visible because the second click reset the timeout
    expect(feedback).to_have_class(re.compile(r".*\bopacity-100\b.*"))

    # Wait another 1 second to pass the 2s mark for the second click
    page.wait_for_timeout(1000)
    expect(feedback).to_have_class(re.compile(r".*\bopacity-0\b.*"))
