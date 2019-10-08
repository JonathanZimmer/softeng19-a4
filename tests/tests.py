from pmgr.__main__ import *
from pmgr.project import Project, TaskException

def test_add():
    args = ["proj1","task1"]
    __main__.add(args)
    assert "task1" in proj1.get_tasks() == True

def test_remove():
    args = ["proj2","task1"]
    __main__.remove(args)
    assert "task1" in proj2.get_tasks() == False


