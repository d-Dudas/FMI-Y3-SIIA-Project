from typing import Dict, List


class ProcessedProblemReportData:
    def __init__(self, processed_title_and_description: str, useful_features: Dict[str, str | List[str]], label: str) -> None:
        self.processed_title_and_description: str = processed_title_and_description
        self.useful_features: Dict[str, str | List[str]] = useful_features
        self.label: str = label
        self.encoded_label: int = None

    def __str__(self) -> str:
        return (f"Processed Title and Description: {self.processed_title_and_description}\n"
                f"Useful Features: {self.useful_features}\n"
                f"Label: {self.label}")
