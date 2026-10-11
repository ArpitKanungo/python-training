"""
Member 4 : Reporting Engine (Generates reports based on analyzed log data)
"""
import os
import csv
import logging
from src.analyzer import LogAnalyzer

logger = logging.getLogger("LogAnalyzer.Reporter") # Logger for the reporter module

def generate_console_summary(analyzer: LogAnalyzer):
    """
    Generates a console summary of the analyzed log data.
    """
    summary = analyzer.get_overall_summary()
    summary_lines = [
        "=" * 60,
        "               OPERATIONAL LOG MONITORING REPORT",
        "=" * 60,
        "--- OVERALL METRICS AND HEALTH STATUS ---",
        f" Total lines Read: {summary['Total lines']}",
        f" Successfully parsed: {summary['Total parsed']} ({summary['Parse success rate']})",
        f" Malformed/Skipped lines: {summary['Skipped lines']}",
        f" Total Warnings: {summary['Warning count']}",
        f" Total Errors: {summary['Error count']}",
        "-" * 60,
        "--- LOG LEVEL DISTRIBUTION ---",
    ]

    for level, count in sorted(analyzer.level_counts.items()):
        summary_lines.append(f" {level}: {count}")

    summary_lines.append("=" * 60)
    summary_lines.append("--- TOP RECURRING WARNINGS ---")
    top_warning = analyzer.get_top_warnings(5)
    if not top_warning:
        summary_lines.append(" No recurring warnings found.")
    else:
        for index, (warning, count) in enumerate(top_warning, start=1):
            summary_lines.append(f" {index}. {warning}: {count}")
    summary_lines.append("=" * 60)
    summary_lines.append("--- TOP RECURRING ERRORS ---")
    top_error = analyzer.get_top_errors(5)
    if not top_error:
        summary_lines.append(" No recurring errors found.")
    else:
        for index, (error, count) in enumerate(top_error, start=1):
            summary_lines.append(f" {index}. {error}: {count}")
    summary_lines.append("=" * 60)
    reportStr = "\n".join(summary_lines)
    print(reportStr)
    return reportStr

def export_text_report(report_text, file_path):
    """
    Exports the given report text to a specified file.
    """
    try:
        with open(file_path, "w") as file:
            file.write(report_text)
        logger.info(f"Report successfully exported to {file_path}")
    except Exception as e:
        logger.error(f"Failed to export report to {file_path}: {e}")
        raise e

def export_csv_breakdown(analyzer, file_path):
    """
    Exports a CSV breakdown of log levels, top warnings, and top errors.
    """
    try:
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # Write log level breakdown
            writer.writerow(["Log Level", "Count"])
            for level, count in sorted(analyzer.level_counts.items()):
                writer.writerow([level, count])
            writer.writerow([])

            # Write top warnings
            writer.writerow(["Top Warnings", "Count"])
            top_warning = analyzer.get_top_warnings(5)
            for warning, count in top_warning:
                writer.writerow([warning, count])
            writer.writerow([])

            # Write top errors
            writer.writerow(["Top Errors", "Count"])
            top_error = analyzer.get_top_errors(5)
            for error, count in top_error:
                writer.writerow([error, count])

        logger.info(f"CSV breakdown successfully exported to {file_path}")
    except Exception as e:
        logger.error(f"Failed to export CSV breakdown to {file_path}: {e}")
        raise e