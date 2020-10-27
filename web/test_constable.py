from getGithubData import Github
from datetime import datetime, timedelta
from constable import Constable
import test_config


def test_constable_get_score_case_1:
    test_constable = Constable('test_1','sravankumarmatta',test_config.Access_Token)
    test_constable_required_Scores = {".gitignore":1,"CITATION.md":1,"CODE_OF_CONDUCT":1,"CONTRIBUTING.md":1,"LICENSE":0,"README.md":1,"issues":1,"total_score":6}
    test_constable_returned_Scores =  Constable.get_score()
    assert test_constable_required_Scores == test_constable_returned_Scores

def test_constable_get_score_case_2:
    test_constable = Constable('test_2','sravankumarmatta',test_config.Access_Token)
    test_constable_required_Scores = {".gitignore":1,"CITATION.md":1,"CODE_OF_CONDUCT":1,"CONTRIBUTING.md":0,"LICENSE":0,"README.md":1,"issues":1,"total_score":5}
    test_constable_returned_Scores =  Constable.get_score()
    assert test_constable_required_Scores == test_constable_returned_Scores

def test_contsable_get_grade_case_1:
    test_constable = Constable('test_1','sravankumarmatta',test_config.Access_Token)
    test_constable_required_grade = 'B+'
    test_constable_returned_grade =  Constable.get_grade()
    assert test_constable_required_grade == test_constable_returned_grade

def test_contsable_get_grade_case_2:
    test_constable = Constable('test_2','sravankumarmatta',test_config.Access_Token)
    test_constable_required_grade = 'C'
    test_constable_returned_grade =  Constable.get_grade()
    assert test_constable_required_grade == test_constable_returned_grade
