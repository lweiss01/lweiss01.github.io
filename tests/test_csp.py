import os
import re
import pytest

@pytest.fixture(scope="module")
def layout_content():
    layout_path = os.path.join('_layouts', 'default.html')
    assert os.path.exists(layout_path), f"{layout_path} does not exist"
    with open(layout_path, 'r', encoding='utf-8') as f:
        return f.read()

def test_csp_presence(layout_content):
    content = layout_content

    # Regex to find the CSP meta tag
    # It looks for <meta http-equiv="Content-Security-Policy" content="...">
    csp_pattern = re.compile(
        r'<meta\s+http-equiv=["\']Content-Security-Policy["\']\s+content=["\'](.*?)["\']\s*/?>',
        re.IGNORECASE | re.DOTALL
    )

    match = csp_pattern.search(content)
    assert match, "Content-Security-Policy meta tag not found in default.html"

    csp_content = match.group(1)

    # Check for specific directives
    assert "default-src 'self'" in csp_content
    assert "script-src 'self'" in csp_content
    assert "style-src 'self' 'unsafe-inline'" in csp_content
    assert "img-src 'self' data:" in csp_content
    assert "object-src 'none'" in csp_content

def test_no_html5shiv(layout_content):
    content = layout_content

    assert "html5shiv.googlecode.com" not in content, "Legacy html5shiv script should be removed"
