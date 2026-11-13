import unittest

from data.clean import clean_records
from data.format_pairs import format_input_analysis_fix


class TestPreprocessingScaffold(unittest.TestCase):
    def test_clean_records_passthrough(self) -> None:
        records = [{"id": 1}]
        self.assertEqual(clean_records(records), records)

    def test_format_pairs_passthrough(self) -> None:
        records = [{"input": "x", "analysis": "y", "fix": "z"}]
        self.assertEqual(format_input_analysis_fix(records), records)


if __name__ == "__main__":
    unittest.main()
