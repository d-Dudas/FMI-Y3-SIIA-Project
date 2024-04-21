from typing import List, Optional
from ProblemDescription import ProblemDescription

class ProblemReport:
    def __init__(self, problem_report_id: str, fault_analysis_id: List[str], attached_prs: List[str],
                 author: str, build: str, description: str, feature: str, group_in_charge: str,
                 state: str, title: str, author_group: str, information_request_id: List[str],
                 status_log: Optional[str], release: List[str], explanation_for_correction_not_needed: List[str],
                 reason_why_correction_is_not_needed: List[str], fault_analysis_feature: List[str],
                 fault_analysis_group_in_charge: List[str], state_changed_to_closed: Optional[str],
                 fault_analysis_title: List[str]):
        self.problem_report_id = problem_report_id 
        self.fault_analysis_id = fault_analysis_id
        self.attached_prs = attached_prs
        self.author = author
        self.build = build
        self.description: ProblemDescription = ProblemDescription.parse(description)
        self.feature = feature
        self.group_in_charge = group_in_charge
        self.state = state
        self.title = title
        self.author_group = author_group
        self.information_request_id = information_request_id
        self.status_log = status_log
        self.release = release
        self.explanation_for_correction_not_needed = explanation_for_correction_not_needed
        self.reason_why_correction_is_not_needed = reason_why_correction_is_not_needed
        self.fault_analysis_feature = fault_analysis_feature
        self.fault_analysis_group_in_charge = fault_analysis_group_in_charge
        self.state_changed_to_closed = state_changed_to_closed
        self.fault_analysis_title = fault_analysis_title

    @classmethod
    def from_dict(cls, data):
        return cls(
            problem_report_id=data.get("problemReportId", ""),
            fault_analysis_id=data.get("faultAnalysisId", []),
            attached_prs=data.get("attachedPRs", []),
            author=data.get("author", ""),
            build=data.get("build", ""),
            description=data.get("description", ""),
            feature=data.get("feature", ""),
            group_in_charge=data.get("groupInCharge", ""),
            state=data.get("state", ""),
            title=data.get("title", ""),
            author_group=data.get("authorGroup", ""),
            information_request_id=data.get("informationrequestID", []),
            status_log=data.get("statusLog", None),
            release=data.get("release", []),
            explanation_for_correction_not_needed=data.get(
                "explanationforCorrectionNotNeeded", []),
            reason_why_correction_is_not_needed=data.get(
                "reasonWhyCorrectionisNotNeeded", []),
            fault_analysis_feature=data.get("faultAnalysisFeature", []),
            fault_analysis_group_in_charge=data.get(
                "faultAnalysisGroupInCharge", []),
            state_changed_to_closed=data.get("stateChangedtoClosed", None),
            fault_analysis_title=data.get("faultAnalysisTitle", [])
        )

    def __str__(self):
        return (f"ProblemReport:\n"
                f"\t(problem_report_id={self.problem_report_id},\n"
                f"\tfault_analysis_id={self.fault_analysis_id},\n"
                f"\tattached_prs={self.attached_prs},\n"
                f"\tauthor={self.author},\n"
                f"\tbuild={self.build},\n"
                f"\tdescription={self.description},\n"
                f"\tfeature={self.feature},\n"
                f"\tgroup_in_charge={self.group_in_charge},\n"
                f"\tstate={self.state},\n"
                f"\ttitle={self.title},\n"
                f"\tauthor_group={self.author_group},\n"
                f"\tinformation_request_id={self.information_request_id},\n"
                f"\tstatus_log={self.status_log},\n"
                f"\trelease={self.release},\n"
                f"\texplanation_for_correction_not_needed={self.explanation_for_correction_not_needed},\n"
                f"\treason_why_correction_is_not_needed={self.reason_why_correction_is_not_needed},\n"
                f"\tfault_analysis_feature={self.fault_analysis_feature},\n"
                f"\tfault_analysis_group_in_charge={self.fault_analysis_group_in_charge},\n"
                f"\tstate_changed_to_closed={self.state_changed_to_closed},\n"
                f"\tfault_analysis_title={self.fault_analysis_title})")
