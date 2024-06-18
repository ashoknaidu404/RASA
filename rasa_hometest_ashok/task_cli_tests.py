import subprocess
import pytest

"""run_taskwarrior_command  methon used for to perform task operation such add list etc..."""
def run_taskwarrior_command(command):
    result = subprocess.run(['task'] + command.split(), capture_output=True, text=True)
    return result.stdout, result.stderr

"""Ensure no task are available"""
@pytest.fixture(autouse=True)
def setup_and_teardown():
    stdout, stderr = run_taskwarrior_command('rc.confirmation=off delete')
    print(stdout)
    stdout, stderr = run_taskwarrior_command('config rc.confirmation off')
    print(stdout)
    yield

##Delete all task after test completed
    #delete_all_tasks()

"""Adding new task """
def test_add_task():
    stdout, stderr = run_taskwarrior_command('add "Test Task 1"')

    print(stdout)
    assert "Created task" in stdout

"""list of task"""
def test_list_tasks():
    stdout, stderr = run_taskwarrior_command('list')
    print(stdout)
    assert "Test Task 1" in stdout

"""Complted tasks"""
def test_complete_task():
    stdout, stderr = run_taskwarrior_command('1 done')
    print(stdout)
    assert "Completed task" in stdout

"""delete a task"""
def test_delete_task():
    stdout, stderr = run_taskwarrior_command('add "Test Task to Delete ashok"')
    print(stdout)
    assert "Created task" in stdout
    stdout, stderr = run_taskwarrior_command('1 delete rc.confirmation=off')
    print(stdout)
    assert "Deleted 1 task" in stdout

"""modification task """
def test_modify_task():
    run_taskwarrior_command('add "Task to Modify"')
    stdout, stderr = run_taskwarrior_command('list')
    print(stdout)
    assert "Task to Modify" in stdout
    stdout, stderr = run_taskwarrior_command('1 modify description: "Modified Task"')
    print(stdout)
    assert "Modified 1 task" in stdout
    stdout, stderr = run_taskwarrior_command('list')
    print(stdout)
    assert "Modified Task" in stdout
    delete_all_tasks()

def delete_all_tasks():
    """
    Deletes all tasks by first listing them and then deleting each task individually.
    """
    # List all pending tasks
    stdout, stderr = run_taskwarrior_command('list')
    print("List of task to delete----> "+stdout)

    # Parse the task IDs from the output
    lines = stdout.splitlines()
    task_ids = []
    for line in lines:
        if line.strip() and line.split()[0].isdigit():
            task_ids.append(line.split()[0])
    print(task_ids)


    # Delete each task individually

    for task_id in task_ids:
        run_taskwarrior_command(f'{task_id} delete rc.confirmation=off')
        print(task_id+"   : ---> killed ")
