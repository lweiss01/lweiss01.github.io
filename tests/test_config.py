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

def check_theme_config(config):
    """Check if the theme is set correctly in the config dictionary."""
    assert "theme" in config, "Theme key is missing in config."
    assert config["theme"] == "jekyll-theme-tactile", f"Expected theme 'jekyll-theme-tactile', but got '{config.get('theme')}'"

def test_theme_is_correct():
    """Verify that the theme is set to jekyll-theme-tactile."""
    if not os.path.exists(CONFIG_FILE):
        pytest.skip(f"{CONFIG_FILE} not found")

    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

    check_theme_config(config)

def test_theme_missing_in_config():
    """Verify that an error is raised if the theme key is missing."""
    config = {"title": "Test"}
    with pytest.raises(AssertionError, match="Theme key is missing in config."):
        check_theme_config(config)

def test_theme_incorrect_in_config():
    """Verify that an error is raised if the theme is incorrect."""
    config = {"theme": "wrong-theme"}
    with pytest.raises(AssertionError, match="Expected theme 'jekyll-theme-tactile'"):
        check_theme_config(config)

def test_critical_files_exist():
    """Verify that critical files like README.md and index.md exist."""
    critical_files = ["README.md", "index.md"]
    for file in critical_files:
        assert os.path.exists(file), f"Critical file {file} is missing."
