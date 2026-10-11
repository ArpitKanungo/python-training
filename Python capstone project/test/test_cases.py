import unittest
import tempfile
import os
from src.reader import read_log_stream
from src.parser import parse_log_line
from src.analyzer import LogAnalyzer
from src.reporter import generate_console_summary, export_text_report, export_csv_breakdown

class TestReader(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            list(read_log_stream("invalid_file.log"))
    def test_stream_line(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write("line1\nline2\nline3\n")
            temp_file_name = temp_file.name
        try:
            lines = list(read_log_stream(temp_file_name))
            self.assertEqual(len(lines), 3)
        finally:
            os.remove(temp_file_name)

class TestParser(unittest.TestCase):
    def test_parse_log_line(self):
        log_line = "2026-03-31 10:15:30 [ERROR] [auth_service] Invalid credentials for user "
        parsed = parse_log_line(log_line)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed['level'], "ERROR")
        self.assertEqual(parsed['module'], "auth_service")

    def test_malformed_line(self):
        self.assertIsNone(parse_log_line("malformed line"))
        self.assertIsNone(parse_log_line(""))

class TestAnalyzer(unittest.TestCase):
    def test_analyze_empty_logs(self):
        lines = ["2026-03-31 10:15:30 [ERROR] [db] Timeout ",
                 "2026-03-31 10:16:30 [ERROR] [db] Timeout",
                 "2026-03-31 10:17:30 [INFO] [web] Success",
                 "malformed line"
                ]
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)
        self.assertEqual(analyzer.total_lines, 4)
        self.assertEqual(analyzer.total_parsed, 3)
        self.assertEqual(analyzer.level_counts["ERROR"], 2)
        self.assertEqual(analyzer.get_top_errors(1)[0], ("db: Timeout", 2))

class TestReporter(unittest.TestCase):
    def test_report_generation_and_export(self):
        analyzer = LogAnalyzer()
        report_str = generate_console_summary(analyzer)
        self.assertIn("OPERATIONAL LOG MONITORING REPORT", report_str)
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = os.path.join(temp_dir, "test.csv")
            export_csv_breakdown(analyzer, csv_path)
            self.assertTrue(os.path.exists(csv_path))

if __name__ == "__main__":
    unittest.main()
