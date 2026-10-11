import argparse
import sys
import logging
from src.reader import read_log_stream
from src.parser import parse_log_line
from src.analyzer import LogAnalyzer
from src.reporter import generate_console_summary, export_text_report, export_csv_breakdown

def configure_app_logging(log_file = "application.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode = "a"),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    parser = argparse.ArgumentParser(description="Operational Log Monitoring Tool")
    parser.add_argument("--input", "-i", type = str, default = "data/sample.log")
    parser.add_argument("--output-text", type = str, default = "reports/summary_report.txt")
    parser.add_argument("--output-csv", type = str, default = "reports/error_distribution.csv")
    parser.add_argument("--top", type = int, default = 5, help = "Number of top recurring errors/warnings to report")

    args = parser.parse_args()
    configure_app_logging()
    logger = logging.getLogger("LogAnalyzer.Main")
    logger.info(f"Starting Operational Log Monitoring Tool for {args.input}")

    try:
        lines = read_log_stream(args.input)
        analyzer = LogAnalyzer()
        analyzer.ingest_events(lines, parse_log_line)
        report_str = generate_console_summary(analyzer, args.top)
        print(report_str)
        export_text_report(report_str, args.output_text)
        export_csv_breakdown(analyzer, args.output_csv, args.top)
        logger.info("Reports generated successfully.")
        print(f"\nReports written:\n  - {args.output_text}\n  - {args.output_csv}")
    except (FileNotFoundError, PermissionError, IOError) as e:
        logger.error(f"File error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()