% Obligations
obligatory(attend_meeting(Employee)) :- mandatory_meeting, employee(Employee).
obligatory(complete_task(Employee, Task)) :- assigned_task(Employee, Task).
obligatory(report_work_done(Employee)) :- completed_task(Employee).

% Permissions
permitted(take_break(Employee)) :- employee(Employee), working_hours.
permitted(work_from_home(Employee)) :- employee(Employee), has_manager_approval(Employee).
permitted(access_shared_files).

% Prohibitions
forbidden(access_restricted_files(Employee)) :- employee(Employee), \+ has_permission(Employee, access_restricted_files).
forbidden(leave_early(Employee)) :- employee(Employee), \+ has_approval(Employee, leave_early).

% Conditional Rules
employee(john).
employee(alice).
assigned_task(john, task1).
assigned_task(alice, task2).
mandatory_meeting.
working_hours.
has_manager_approval(alice).
completed_task(john).
has_permission(john, access_restricted_files).
has_approval(alice, leave_early).