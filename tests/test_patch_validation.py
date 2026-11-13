import unittest

from verification.sandbox import verify_patch


class TestPatchValidationScaffold(unittest.TestCase):
    def test_verify_patch_schema(self) -> None:
        result = verify_patch("/tmp/project")
        self.assertIn("verified", result)
        self.assertIn("retries", result)


if __name__ == "__main__":
    unittest.main()
