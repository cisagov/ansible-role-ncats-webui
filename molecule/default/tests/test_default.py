"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "directory", [{"mode": "0o750", "path": "/var/cyhy/ncats-webui"}]
)
def test_directories(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize("file", [{"path": "/var/cyhy/ncats-webui/docker-compose.yml"}])
def test_files(host, file):
    """Test that the appropriate files were created."""
    assert host.file(file["path"]).exists
    assert host.file(file["path"]).is_file
