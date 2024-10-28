from pyswip import Prolog

# Initialize Prolog instance and load the knowledge base
prolog = Prolog()
prolog.consult("office_rules.pl")

def check_obligation(action, employee, task=None):
    if task:
        query = f"obligatory({action}({employee}, {task}))"
    else:
        query = f"obligatory({action}({employee}))"
    result = list(prolog.query(query))
    if result:
        print(f"Obligation: {employee} must {action.replace('_', ' ')}{' ' + task if task else ''}.")
    else:
        print(f"{employee} is not obligated to {action.replace('_', ' ')}{' ' + task if task else ''}.")

def check_permission(action, employee):
    query = f"permitted({action}({employee}))"
    result = list(prolog.query(query))
    if result:
        print(f"Permission: {employee} may {action.replace('_', ' ')}.")
    else:
        print(f"{employee} is not permitted to {action.replace('_', ' ')}.")

def check_prohibition(action, employee):
    query = f"forbidden({action}({employee}))"
    result = list(prolog.query(query))
    if result:
        print(f"Prohibition: {employee} must not {action.replace('_', ' ')}.")
    else:
        print(f"{employee} is not forbidden to {action.replace('_', ' ')}.")

# Check obligations
check_obligation("attend_meeting", "john")
check_obligation("complete_task", "alice", "task2")

# Check permissions
check_permission("take_break", "john")
check_permission("work_from_home", "alice")

# Check prohibitions
check_prohibition("access_restricted_files", "john")
check_prohibition("leave_early", "alice")
