import re

class ProblemDescription:
    def __init__(self, test_steps=None, expected_result=None, actual_result=None, tester_analysis=None, logs=None, test_line_reference=None, used_flags=None, fault_occurrence_rate=None, test_scenario_history=None, test_case_reference=None):
        self.test_steps = test_steps
        self.expected_result = expected_result
        self.actual_result = actual_result
        self.tester_analysis = tester_analysis
        self.logs = logs
        self.test_line_reference = test_line_reference
        self.used_flags = used_flags
        self.fault_occurrence_rate = fault_occurrence_rate
        self.test_scenario_history = test_scenario_history
        self.test_case_reference = test_case_reference

    @staticmethod
    def parse(description):
        headers = {
            'test_steps': r"\[1\. Detail Test Steps:\](.*?)\[\d",
            'expected_result': r"\[2\. Expected Result:\](.*?)\[\d",
            'actual_result': r"\[3\. Actual Result:\](.*?)\[\d",
            'tester_analysis': r"\[4\. Tester analysis:\](.*?)\[\d",
            'logs': r"\[5\. Log\(s\) file name containing a fault:\](.*?)\[\d",
            'test_line_reference': r"\[6\. Test-Line Reference/used HW/configuration/tools/SW version\](.*?)\[\d",
            'used_flags': r"\[7\. Used Flags:\](.*?)\[\d",
            'fault_occurrence_rate': r"\[8\. Fault Occurrence Rate:\](.*?)\[\d",
            'test_scenario_history': r"\[9\. Test Scenario History of Execution:\](.*?)\[\d",
            'test_case_reference': r"\[10\. Test Case Reference:\](.*?)\*\*\*",
        }
        data = {}
        for key, regex in headers.items():
            match = re.search(regex, description + "[", re.S)
            if match:
                data[key] = match.group(1).strip()

        return ProblemDescription(**data)

    def __str__(self):
        return (f"\t\tDetail Test Steps: {self.test_steps}\n"
                f"\t\tExpected Result: {self.expected_result}\n"
                f"\t\tActual Result: {self.actual_result}\n"
                f"\t\tTester Analysis: {self.tester_analysis}\n"
                f"\t\tLogs: {self.logs}\n"
                f"\t\tTest-Line Reference: {self.test_line_reference}\n"
                f"\t\tUsed Flags: {self.used_flags}\n"
                f"\t\tFault Occurrence Rate: {self.fault_occurrence_rate}\n"
                f"\t\tTest Scenario History: {self.test_scenario_history}\n"
                f"\t\tTest Case Reference: {self.test_case_reference}")