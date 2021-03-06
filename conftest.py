import pytest
from datetime import datetime
from pytest_jsonreport.plugin import JSONReport

@pytest.hookimpl(optionalhook=True)
def pytest_json_modifyreport(json_report):
    """Modifies the report that comes out of --json-report 
    """
    # get number of warnings generated by test
    num_warnings = len(json_report['warnings']) if 'warnings' in json_report else 0
    # the root will vary depending on the device it is run on. We only care that it's run in the group2 directory.
    root = json_report['root'].split("\\")[-1]
    summary_keys = list(json_report['summary'].keys())

    # test is considered a success IF:
        # there are no warnings generated
        # the tests were run at the top-level "group2" directory
        # the summary only has 'passed', 'total', and 'collected' fields. NO XFAIL, XPASS, or FAIL.
    success = True if num_warnings == 0 and root == 'group2' and summary_keys == ['passed', 'total', 'collected'] else False

    # strip excessive information from tests that pass
    tests = json_report['tests']
    for i, test in enumerate(tests):
        if test['outcome'] == "passed":
            t = {}
            for field in ["nodeid", "outcome", "metadata"]:
                t[field] = test[field] if field in test else ""
            tests[i] = t
    
    # put test time in a readable format
    created = datetime.fromtimestamp(json_report['created'])

    json_report['created'] = created
    json_report['success'] = success
    json_report['root'] = root
    json_report['tests'] = tests

    # not useful information for us
    to_delete = ['environment', 'collectors']
    for item in to_delete:
        del json_report[item]
