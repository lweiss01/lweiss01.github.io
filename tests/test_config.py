import os
import yaml
import pytest

CONFIG_FILE = "_config.yml"

def test_config_file_exists():
    """Verify that _config.yml exists."""
    assert os.path.exists(CONFIG_FILE), f"{CONFIG_FILE} does not exist."

def test_config_is_valid_yaml():
    """Verify that _config.yml is valid YAML."""
    if not os.path.exists(CONFIG_FILE):
        pytest.skip(f"{CONFIG_FILE} not found")

    with open(CONFIG_FILE, "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            pytest.fail(f"Failed to parse YAML: {exc}")

    assert isinstance(config, dict), "Config file should be a dictionary."

def test_theme_is_correct():
    """Verify that the theme is set to jekyll-theme-tactile."""
    if not os.path.exists(CONFIG_FILE):
        pytest.skip(f"{CONFIG_FILE} not found")

    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

    assert "theme" in config, "Theme key is missing in config."
    assert config["theme"] == "jekyll-theme-tactile", f"Expected theme 'jekyll-theme-tactile', but got '{config.get('theme')}'"

def test_critical_files_exist():
    """Verify that critical files like README.md and index.md exist."""
    critical_files = ["README.md", "index.md"]
    for file in critical_files:
        assert os.path.exists(file), f"Critical file {file} is missing."
