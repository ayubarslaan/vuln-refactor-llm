import unittest

from engine.inference import generate_secure_patch


class TestInferenceScaffold(unittest.TestCase):
    def test_generate_secure_patch_schema(self) -> None:
        result = generate_secure_patch({"cwe": "CWE-79"}, [])
        self.assertIn("explanation", result)
        self.assertIn("patch", result)
        self.assertIn("inputs", result)


if __name__ == "__main__":
    unittest.main()
