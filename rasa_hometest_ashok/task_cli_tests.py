import subprocess
import pytest

def run_taskwarrior_command(command):
    result = subprocess.run(['task'] + command.split(), capture_output=True, text=True)
    return result.stdout, result.stderr

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Ensure no tasks are left from previous tests
    run_taskwarrior_command('rc.confirmation=off delete')
    run_taskwarrior_command('config rc.confirmation off')

    yield

    # Clean up after each test
    print("==========================")
    run_taskwarrior_command('rc.confirmation=off delete')

def test_add_task():
    stdout, stderr = run_taskwarrior_command('add "Test Task 1"')
    print(stdout,stderr)
    assert "Created task" in stdout

def test_list_tasks():
    stdout, stderr = run_taskwarrior_command('list')
    assert "Test Task 1" in stdout

def test_complete_task():
    stdout, stderr = run_taskwarrior_command('1 done')
    assert "Completed task" in stdout

def test_delete_task():
    stdout, stderr = run_taskwarrior_command('add "Test Task to Delete"')
    assert "Created task" in stdout
    stdout, stderr = run_taskwarrior_command('1 delete rc.confirmation=off')
    assert "Deleted 1 task" in stdout
