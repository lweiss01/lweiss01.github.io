import os

def test_index_md_exists():
    """Verify that index.md exists in the root directory."""
    assert os.path.exists("index.md"), "index.md does not exist"

def test_index_md_content():
    """Verify that index.md contains the expected heading and names."""
    with open("index.md", "r", encoding="utf-8") as f:
        content = f.read()

    assert "### WEISS" in content, "Heading '### WEISS' not found in index.md"
    assert "- Abe" in content, "Name 'Abe' not found in index.md"
    assert "- Krystyana" in content, "Name 'Krystyana' not found in index.md"
    assert "- Lisa" in content, "Name 'Lisa' not found in index.md"
