
"""
Log File Analyzer & Error Monitoring Tool - PowerPoint Deck Generator
Generates a 12-slide modern 16:9 presentation (.pptx) based on Capstone Problem #6.
Requires: pip install python-pptx
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# COLOR PALETTE & DESIGN SYSTEM (Dark Modern Tech Theme)
# ==============================================================================
COLOR_BG          = RGBColor(15, 23, 42)     # #0F172A - Deep Navy Slate
COLOR_CARD        = RGBColor(30, 41, 59)     # #1E293B - Container Card Fill
COLOR_CARD_BORDER = RGBColor(51, 65, 85)     # #334155 - Subtle Card Stroke
COLOR_CYAN        = RGBColor(56, 189, 248)   # #38BDF8 - Primary Accent
COLOR_GREEN       = RGBColor(52, 211, 153)   # #34D399 - Success / INFO
COLOR_ORANGE      = RGBColor(251, 146, 60)   # #FB923C - Warning
COLOR_RED         = RGBColor(248, 113, 113)  # #F87171 - Error / Alert
COLOR_PURPLE      = RGBColor(167, 139, 250)  # #A78BFA - Secondary Accent
COLOR_WHITE       = RGBColor(248, 250, 252)  # #F8FAFC - Main Headings
COLOR_MUTED       = RGBColor(148, 163, 184)  # #94A3B8 - Body Text
COLOR_LIGHT_MUTED = RGBColor(203, 213, 225)  # #CBD5E1 - Subheadings

FONT_HEADING = "Segoe UI"
FONT_BODY    = "Segoe UI"


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================
def create_base_slide(prs, category_tag="PYTHON CAPSTONE PROJECT #6", title="Slide Title"):
    """Creates a slide with custom background, category badge, and title."""
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # 1. Slide Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG
    bg.line.fill.background()

    # 2. Category Tag / Breadcrumb
    tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.3))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = category_tag.upper()
    p_tag.font.name = FONT_HEADING
    p_tag.font.size = Pt(10.5)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_CYAN

    # 3. Slide Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.5), Inches(0.65))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title
    p_title.font.name = FONT_HEADING
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

    return slide


def add_card(slide, left, top, width, height, bg_color=COLOR_CARD, border_color=COLOR_CARD_BORDER):
    """Draws a rounded card container with solid fill and stroke."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)
    return card


def populate_card_content(card, title, body_bullets, title_color=COLOR_CYAN, title_size=15, body_size=12):
    """Populates standard header and bullet points inside a card container."""
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.22)
    tf.margin_bottom = Inches(0.2)

    # Title paragraph
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(title_size)
    p0.font.bold = True
    p0.font.color.rgb = title_color
    p0.space_after = Pt(10)

    # Bullet / body lines
    for item in body_bullets:
        p = tf.add_paragraph()
        p.text = item
        p.font.name = FONT_BODY
        p.font.size = Pt(body_size)
        p.font.color.rgb = COLOR_MUTED
        p.space_after = Pt(6)
        p.level = 0


def add_code_block(slide, left, top, width, height, title, code_lines, title_color=COLOR_CYAN):
    """Draws a dark code card with a title and monospaced code lines."""
    card = add_card(slide, left, top, width, height, bg_color=RGBColor(13, 20, 36))
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.22)
    tf.margin_top = Inches(0.18)
    tf.margin_bottom = Inches(0.15)

    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = title_color
    p0.space_after = Pt(8)

    for line in code_lines:
        p = tf.add_paragraph()
        p.text = line
        p.font.name = "Consolas"
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_LIGHT_MUTED
        p.space_after = Pt(2)
    return card


def add_split_slide(slide, left_title, left_color, left_bullets, code_title, code_lines):
    """Standard layout: explanatory bullets on the left, a code card on the right."""
    left_card = add_card(slide, Inches(0.8), Inches(1.6), Inches(5.9), Inches(5.2))
    populate_card_content(left_card, left_title, left_bullets, title_color=left_color, title_size=16, body_size=12.5)
    add_code_block(slide, Inches(6.95), Inches(1.6), Inches(5.58), Inches(5.2), code_title, code_lines, title_color=left_color)


def build_slide_1(prs):
    """Slide 1: Title Slide with Team Allocations."""
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG
    bg.line.fill.background()

    # Pill Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.7), Inches(0.85), Inches(3.93), Inches(0.42))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(24, 38, 65)
    badge.line.color.rgb = COLOR_CYAN
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "PYTHON CAPSTONE PROJECT  |  PROBLEM #6"
    p_b.font.name = FONT_HEADING
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_CYAN
    p_b.alignment = PP_ALIGN.CENTER

    # Main Title
    title_box = slide.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(11.33), Inches(1.5))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Log File Analyzer &\nError Monitoring Tool"
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(40)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_WHITE
    p_t.alignment = PP_ALIGN.CENTER

    # Subtitle
    sub_box = slide.shapes.add_textbox(Inches(1.8), Inches(3.2), Inches(9.73), Inches(0.8))
    tf_s = sub_box.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "High-throughput log streaming, regex pattern extraction, collections-based analytics, and automated operational reporting in Python."
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(15)
    p_s.font.color.rgb = COLOR_LIGHT_MUTED
    p_s.alignment = PP_ALIGN.CENTER

    # Team Members (Group of 4 cards)
    team_members = [
        ("Participant 1", "File I/O & Iterators", "Stream line reading, generators, file safety"),
        ("Participant 2", "Regex Parsing Engine", "ISO timestamps, severity classification"),
        ("Participant 3", "Analytics & Counter", "collections.Counter, frequency rankings"),
        ("Participant 4", "Reports & CLI Tests", "CSV exports, logging, unittest suite")
    ]

    card_width = Inches(2.7)
    card_gap = Inches(0.24)
    start_left = Inches(0.85)
    card_top = Inches(4.35)
    card_h = Inches(2.3)

    for i, (name, role, desc) in enumerate(team_members):
        c_left = start_left + i * (card_width + card_gap)
        card = add_card(slide, c_left, card_top, card_width, card_h)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.22)

        # Name
        pn = tf.paragraphs[0]
        pn.text = name
        pn.font.name = FONT_HEADING
        pn.font.size = Pt(15)
        pn.font.bold = True
        pn.font.color.rgb = COLOR_CYAN

        # Role
        pr = tf.add_paragraph()
        pr.text = role
        pr.font.name = FONT_HEADING
        pr.font.size = Pt(12)
        pr.font.bold = True
        pr.font.color.rgb = COLOR_WHITE
        pr.space_after = Pt(8)

        # Description
        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.name = FONT_BODY
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_MUTED


def build_slide_2(prs):
    """Slide 2: Business Scenario & Objective."""
    slide = create_base_slide(prs, "1. PROBLEM CONTEXT", "Business Scenario & Strategic Objective")

    # Left Card: The Challenge / Business Scenario
    c1 = add_card(slide, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    bullets1 = [
        "Distributed production systems generate millions of semi-structured log lines across servers, containers, and microservices.",
        "Crucial operational signals like database connection drops, 5xx gateway timeouts, and auth failures are buried in gigabytes of routine INFO logs.",
        "Manual triage via standard grep/cat leads to long Mean Time to Detect (MTTD) and delayed incident responses.",
        "In-memory loading of giant log files risks system memory exhaustion (OOM), requiring an efficient streaming architecture."
    ]
    populate_card_content(c1, "The Business Problem", bullets1, title_color=COLOR_ORANGE, title_size=18, body_size=13)

    # Right Card: Project Objective & Solution
    c2 = add_card(slide, Inches(6.83), Inches(1.6), Inches(5.7), Inches(5.2))
    bullets2 = [
        "Build a fast, memory-safe command-line Python utility to ingest multi-gigabyte log streams lazily via iterators.",
        "Execute regex parsing to cleanly capture ISO timestamps, severity tiers, origin modules, and error payloads.",
        "Aggregate log frequencies using Python's collections.Counter to isolate top recurring operational exceptions.",
        "Generate multi-channel operational summaries: instant rich console displays, CSV trend files, and self-audit execution logs."
    ]
    populate_card_content(c2, "Core Project Objective", bullets2, title_color=COLOR_GREEN, title_size=18, body_size=13)


def build_slide_3(prs):
    """Slide 3: Input Data & File Structure."""
    slide = create_base_slide(prs, "2. INPUT SPECIFICATION", "Input Data Schema & Log Anatomy")

    # Top Card: Log Line Tokenization Breakdown
    top_card = add_card(slide, Inches(0.8), Inches(1.6), Inches(11.73), Inches(2.2))
    tf_top = top_card.text_frame
    tf_top.word_wrap = True
    tf_top.margin_left = tf_top.margin_right = Inches(0.3)
    tf_top.margin_top = Inches(0.2)

    p0 = tf_top.paragraphs[0]
    p0.text = "Sample Raw Log Format & Token Anatomy"
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(16)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CYAN
    p0.space_after = Pt(8)

    p_code = tf_top.add_paragraph()
    p_code.text = "2026-03-29 14:22:10,482 | ERROR | db_pool | Connection to postgres-primary:5432 timed out after 3000ms"
    p_code.font.name = "Consolas"
    p_code.font.size = Pt(12)
    p_code.font.color.rgb = COLOR_WHITE
    p_code.space_after = Pt(10)

    p_desc = tf_top.add_paragraph()
    p_desc.text = "Standard input files are plain-text (.log / .txt). Each valid entry adheres to 4 key tokens: [Timestamp] | [Log Level] | [Module Name] | [Message Payload]."
    p_desc.font.name = FONT_BODY
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = COLOR_MUTED

    # 3 Bottom Columns
    cols = [
        ("Timestamp Token", COLOR_PURPLE, [
            "Format: YYYY-MM-DD HH:MM:SS.",
            "Captured by the regex as a string token for each event.",
            "Available for chronological context in the report."
        ]),
        ("Log Severity Tiers", COLOR_RED, [
            "INFO: Routine operational logs (bulk of volume).",
            "WARNING: Recoverable warnings, cache misses, slow queries.",
            "ERROR: Unhandled exceptions and system failures."
        ]),
        ("Module & Payload", COLOR_CYAN, [
            "Module tag designates source service (auth, payment, db_pool).",
            "Message contains stack trace or failure signature.",
            "Normalized to identify identical recurring errors."
        ])
    ]

    col_w = Inches(3.73)
    gap = Inches(0.27)
    for i, (col_title, col_color, col_bullets) in enumerate(cols):
        c = add_card(slide, Inches(0.8) + i * (col_w + gap), Inches(4.05), col_w, Inches(2.75))
        populate_card_content(c, col_title, col_bullets, title_color=col_color, title_size=15, body_size=11.5)


def build_slide_4(prs):
    """Slide 4: Functional Requirements (Requirements 21-25)."""
    slide = create_base_slide(prs, "3. FUNCTIONAL REQUIREMENTS", "Mandatory Functional Requirements (Specs 21-25)")

    reqs = [
        ("21. Lazy Iterator Reading", "Memory-Safe Ingestion", [
            "Read input log files line-by-line via Python generator functions.",
            "Prevent Out-Of-Memory (OOM) errors on large log files (1GB - 50GB).",
            "Use context managers (with open()) for clean descriptor lifecycle."
        ], COLOR_CYAN),
        ("22. Regex Processing", "Field Extraction & Cleaning", [
            "Compile optimized regular expressions with named capture groups.",
            "Extract timestamp, level, module name, and message cleanly.",
            "Return None for corrupt/non-conforming lines so they are skipped."
        ], COLOR_PURPLE),
        ("23. Event Frequency Counts", "Categorization Engine", [
            "Maintain fast running tally of total log entries processed.",
            "Partition aggregate counts by level: INFO, WARNING, ERROR, CRITICAL.",
            "Calculate warning-to-error ratios for health scoring."
        ], COLOR_ORANGE),
        ("24. Top Recurring Errors", "Anomaly Isolation", [
            "Leverage collections.Counter to group repetitive error signatures.",
            "Extract top-N most frequent errors using .most_common(N).",
            "Strip transient variables (IDs, ports) to cluster common root causes."
        ], COLOR_RED),
        ("25. Multi-Report Export", "Structured Reporting", [
            "Render ANSI-formatted terminal summary with high-priority alerts.",
            "Export structured CSV summary for external analytics and BI ingestion.",
            "Maintain execution audit logging of analyzer runtime operations."
        ], COLOR_GREEN)
    ]

    # Render as 5 cards (2 on top, 3 on bottom)
    # Top 2 cards:
    top_w = Inches(5.73)
    top_gap = Inches(0.27)
    for i in range(2):
        code, title, bullets, col = reqs[i]
        c = add_card(slide, Inches(0.8) + i * (top_w + top_gap), Inches(1.6), top_w, Inches(2.45))
        populate_card_content(c, f"{code}: {title}", bullets, title_color=col, title_size=14, body_size=11)

    # Bottom 3 cards:
    bot_w = Inches(3.73)
    bot_gap = Inches(0.27)
    for j in range(3):
        code, title, bullets, col = reqs[2 + j]
        c = add_card(slide, Inches(0.8) + j * (bot_w + bot_gap), Inches(4.25), bot_w, Inches(2.55))
        populate_card_content(c, f"{code}: {title}", bullets, title_color=col, title_size=13.5, body_size=10.5)


def build_slide_5(prs):
    """Slide 5: Team Allocation for Group of 4."""
    slide = create_base_slide(prs, "4. WORK BREAKDOWN", "Group Team Allocation & Task Ownership (Team of 4)")

    members = [
        ("Participant 1", "Ingestion & Stream Engine", "os, io, sys, generators", COLOR_CYAN, [
            "Builds lazy line streamer with yield generators.",
            "Validates file paths, encoding, and permissions.",
            "Handles corrupt encodings and I/O exceptions.",
            "Delivers zero-memory footprint file reader."
        ]),
        ("Participant 2", "Regex & Event Classifier", "re, typing, logging", COLOR_PURPLE, [
            "Constructs a compiled regex with named groups.",
            "Parses timestamp, level, module, and message.",
            "Returns a structured dict for each valid line.",
            "Returns None for malformed lines (counted as skipped)."
        ]),
        ("Participant 3", "Analytics & Statistical Engine", "collections.Counter, typing", COLOR_ORANGE, [
            "Implements Counter for severity frequencies.",
            "Extracts top-N recurring error signatures.",
            "Computes parse-success and error/warning rates.",
            "Keys errors as 'module: message' to cluster them."
        ]),
        ("Participant 4", "Reporting, CLI & Test Suite", "csv, argparse, logging, unittest", COLOR_GREEN, [
            "Generates executive CLI console summary.",
            "Exports structured CSV reports for analytics.",
            "Builds analyzer self-audit logging mechanism.",
            "Develops unit test suite covering edge cases."
        ])
    ]

    card_w = Inches(2.73)
    card_gap = Inches(0.27)
    top_pos = Inches(1.6)
    height = Inches(5.2)

    for i, (name, role, mods, color, tasks) in enumerate(members):
        c = add_card(slide, Inches(0.8) + i * (card_w + card_gap), top_pos, card_w, height)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.25)

        # Name
        p0 = tf.paragraphs[0]
        p0.text = name
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(16)
        p0.font.bold = True
        p0.font.color.rgb = color

        # Role
        p1 = tf.add_paragraph()
        p1.text = role
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_after = Pt(4)

        # Modules badge
        p2 = tf.add_paragraph()
        p2.text = f"Modules: {mods}"
        p2.font.name = "Consolas"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_CYAN
        p2.space_after = Pt(12)

        # Deliverables header
        p3 = tf.add_paragraph()
        p3.text = "Key Deliverables:"
        p3.font.name = FONT_HEADING
        p3.font.size = Pt(11)
        p3.font.bold = True
        p3.font.color.rgb = COLOR_LIGHT_MUTED
        p3.space_after = Pt(4)

        # Bullets
        for task in tasks:
            pt = tf.add_paragraph()
            pt.text = task
            pt.font.name = FONT_BODY
            pt.font.size = Pt(10.5)
            pt.font.color.rgb = COLOR_MUTED
            pt.space_after = Pt(4)


def build_slide_6(prs):
    """Slide 6: Course Skills & Core Python Applied."""
    slide = create_base_slide(prs, "5. TECHNICAL FOUNDATION", "Course Python Concepts & Skills Applied")

    skills = [
        ("File Handling & Generators", "Memory Efficiency", COLOR_CYAN, [
            "Context managers (with open(...)) guarantee automatic cleanup of OS file descriptors.",
            "Lazy iteration via yield enables streaming multi-gigabyte files with ~15MB constant memory.",
            "Cross-platform file path resolution using pathlib and os.path."
        ]),
        ("Regular Expressions (re)", "Pattern Matching", COLOR_PURPLE, [
            "Compiled re.compile() patterns cached for optimal sub-millisecond execution.",
            "Named capture groups: (?P<timestamp>...), (?P<level>...), (?P<module>...).",
            "Multi-format fallback expressions to handle varied enterprise log layouts."
        ]),
        ("Advanced Data Structures", "Aggregations & Analytics", COLOR_ORANGE, [
            "collections.Counter used for instant frequency counts and .most_common(N) lookups.",
            "Dictionaries carry structured events (timestamp, level, module, message) between stages.",
            "Errors keyed as 'module: message' so identical failures are grouped and ranked."
        ]),
        ("Defensive Programming & Logging", "Robustness & Auditability", COLOR_GREEN, [
            "Granular try-except blocks catching FileNotFoundError, PermissionError, and IOError.",
            "Standard logging module writes an internal audit trail (application.log).",
            "Separation of concerns across modules with a clean CLI interface via argparse."
        ])
    ]

    card_w = Inches(5.73)
    card_h = Inches(2.45)
    gap_x = Inches(0.27)
    gap_y = Inches(0.25)

    positions = [
        (Inches(0.8), Inches(1.6)),
        (Inches(6.8), Inches(1.6)),
        (Inches(0.8), Inches(4.3)),
        (Inches(6.8), Inches(4.3))
    ]

    for (pos_x, pos_y), (title, sub, col, bullets) in zip(positions, skills):
        c = add_card(slide, pos_x, pos_y, card_w, card_h)
        populate_card_content(c, f"{title} ({sub})", bullets, title_color=col, title_size=14, body_size=11)


def build_slide_7(prs):
    """Slide 7: System Architecture & Data Pipeline."""
    slide = create_base_slide(prs, "6. SYSTEM ARCHITECTURE", "End-to-End Processing Pipeline & Data Flow")

    # Pipeline Stages (one stage per team member, matching the real modules)
    stages = [
        ("Stage 1 · src/reader.py", "Participant 1", "Lazy file streaming\nLine generator (yield)\nPath & I/O validation", COLOR_CYAN),
        ("Stage 2 · src/parser.py", "Participant 2", "Compiled regex\nNamed groups -> dict\nNone = skipped line", COLOR_PURPLE),
        ("Stage 3 · src/analyzer.py", "Participant 3", "collections.Counter\nLevel & frequency stats\nTop-N recurring errors", COLOR_ORANGE),
        ("Stage 4 · src/reporter.py", "Participant 4", "Console summary\nText + CSV export\nAuto-create folder", COLOR_GREEN),
    ]

    stage_w = Inches(2.73)
    stage_gap = Inches(0.27)
    top_pos = Inches(1.6)
    height = Inches(3.2)

    for i, (title, owner, desc, col) in enumerate(stages):
        c = add_card(slide, Inches(0.8) + i * (stage_w + stage_gap), top_pos, stage_w, height)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.2)

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(12.5)
        p0.font.bold = True
        p0.font.color.rgb = col
        p0.space_after = Pt(2)

        p1 = tf.add_paragraph()
        p1.text = owner
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_after = Pt(10)

        for line in desc.split("\n"):
            p = tf.add_paragraph()
            p.text = f"• {line}"
            p.font.name = FONT_BODY
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_MUTED
            p.space_after = Pt(4)

    # Bottom Architectural Highlights Card
    bot_card = add_card(slide, Inches(0.8), Inches(5.05), Inches(11.73), Inches(1.8))
    bullets_bot = [
        "Orchestration (main.py): the CLI entry point wires all four stages together and configures logging — shared by the whole team.",
        "Decoupled Pipeline Design: ingestion, parsing, aggregation, and export are distinct, single-responsibility layers owned one-per-member.",
        "Memory-Safe Streaming: lines are yielded one at a time and aggregated into a Counter without holding the whole file in memory.",
        "Production Reliability: corrupted lines or a missing log file are handled gracefully without terminating the pipeline.",
    ]
    populate_card_content(bot_card, "Key Architectural Highlights", bullets_bot, title_color=COLOR_CYAN, title_size=13, body_size=10.5)


def build_slide_8(prs):
    """Slide 8: Key Performance Benchmarks & Metrics."""
    slide = create_base_slide(prs, "7. PERFORMANCE & METRICS", "Processing Benchmarks & System Efficiency")

    # 3 High Impact Stat Boxes
    stats = [
        ("100,000", "Lines Processed", "Total log lines streamed from data/large_sample.log in a single run.", COLOR_CYAN),
        ("99.82%", "Parse Success Rate", "99,820 of 100,000 lines parsed cleanly; 180 malformed lines safely skipped.", COLOR_GREEN),
        ("180", "Malformed Skipped", "Non-conforming lines counted (not dropped silently) and reported as skipped.", COLOR_PURPLE)
    ]

    stat_w = Inches(3.73)
    stat_gap = Inches(0.27)
    for i, (val, label, desc, col) in enumerate(stats):
        c = add_card(slide, Inches(0.8) + i * (stat_w + stat_gap), Inches(1.6), stat_w, Inches(2.2))
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        pv = tf.paragraphs[0]
        pv.text = val
        pv.font.name = FONT_HEADING
        pv.font.size = Pt(42)
        pv.font.bold = True
        pv.font.color.rgb = col
        pv.space_after = Pt(2)

        pl = tf.add_paragraph()
        pl.text = label
        pl.font.name = FONT_HEADING
        pl.font.size = Pt(14)
        pl.font.bold = True
        pl.font.color.rgb = COLOR_WHITE
        pl.space_after = Pt(6)

        pd = tf.add_paragraph()
        pd.text = desc
        pd.font.name = FONT_BODY
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_MUTED

    # Bottom Severity Distribution Summary Card
    bot = add_card(slide, Inches(0.8), Inches(4.05), Inches(11.73), Inches(2.75))
    tf_b = bot.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = Inches(0.3)
    tf_b.margin_top = Inches(0.22)

    p0 = tf_b.paragraphs[0]
    p0.text = "Log Level Distribution (data/large_sample.log — 100,000 lines)"
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(16)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CYAN
    p0.space_after = Pt(8)

    rows = [
        ("INFO Entries", "84,700 events (84.7%)", "Routine operational logs: logins, successful requests, health checks, completed jobs."),
        ("ERROR Exceptions", "10,770 events (10.8%)", "Connection timeouts, gateway rejections, expired tokens, 500s, broker failures."),
        ("WARNING Notifications", "4,350 events (4.4%)", "Redis key expiry, disk usage alerts, transient upstream retries."),
        ("Malformed / Skipped", "180 lines (0.18%)", "Corrupted fragments lacking the standard timestamp/level format.")
    ]

    for title, count, detail in rows:
        p = tf_b.add_paragraph()
        p.text = f"• {title}: {count} — {detail}"
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_MUTED
        p.space_after = Pt(4)


def build_slide_9(prs):
    """Slide 9: Top Recurring Errors Table."""
    slide = create_base_slide(prs, "8. ERROR ANALYTICS", "Top Recurring Error Signatures Isolated (collections.Counter)")

    # Description Box
    desc_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.73), Inches(0.5))
    tf_d = desc_box.text_frame
    tf_d.margin_left = tf_d.margin_right = tf_d.margin_top = tf_d.margin_bottom = 0
    p = tf_d.paragraphs[0]
    p.text = "Top-5 errors from data/large_sample.log via analyzer.get_top_errors(5), keyed as 'module: message':"
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_LIGHT_MUTED

    # Table Shape
    table_shape = slide.shapes.add_table(6, 4, Inches(0.8), Inches(2.1), Inches(11.73), Inches(4.5))
    table = table_shape.table
    table.columns[0].width = Inches(3.8)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(2.3)
    table.columns[3].width = Inches(3.83)

    table_data = [
        ["Error Signature (module: message)", "Occurrences", "Module", "Representative Root Cause"],
        ["Connection timeout reached", "4,120 (38.3%)", "db_pool", "Connection pool exhaustion under peak load"],
        ["Gateway rejected transaction 504", "3,040 (28.2%)", "payment", "Upstream payment vendor latency / timeout"],
        ["Token signature expired", "1,510 (14.0%)", "auth", "Client token refresh race condition"],
        ["Internal server error 500", "1,200 (11.1%)", "web", "Unhandled exception in request handler"],
        ["Message broker unreachable", "900 (8.4%)", "queue", "Broker node outage / network partition"]
    ]

    for row_idx, row_values in enumerate(table_data):
        for col_idx, val in enumerate(row_values):
            cell = table.cell(row_idx, col_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE

            # Style Cell Fill
            cell.fill.solid()
            if row_idx == 0:
                cell.fill.fore_color.rgb = RGBColor(24, 38, 65)
            else:
                cell.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 1 else RGBColor(24, 33, 47)

            # Style Paragraph
            p_cell = cell.text_frame.paragraphs[0]
            p_cell.font.name = FONT_HEADING if row_idx == 0 else FONT_BODY
            p_cell.font.size = Pt(12) if row_idx == 0 else Pt(11)
            p_cell.font.bold = (row_idx == 0)
            p_cell.font.color.rgb = COLOR_CYAN if row_idx == 0 else COLOR_WHITE if col_idx == 0 else COLOR_MUTED


def build_slide_10(prs):
    """Slide 10: 4-5 Hour Execution Plan (from problem image)."""
    slide = create_base_slide(prs, "9. PROJECT EXECUTION", "Suggested 4-5 Hour Implementation Roadmap")

    steps = [
        ("Phase 1: Setup", "30 Minutes", COLOR_CYAN, [
            "Deconstruct problem statement & inputs.",
            "Design shared log data structures & schema.",
            "Partition tasks across 4 team participants.",
            "Initialize Git repo & environment."
        ]),
        ("Phase 2: Core Build", "2 Hours", COLOR_PURPLE, [
            "Implement lazy file iterator streamer.",
            "Build & test modular regex expressions.",
            "Implement collections.Counter analytics.",
            "Develop CSV & console reporting."
        ]),
        ("Phase 3: Hardening", "45 Minutes", COLOR_ORANGE, [
            "Add exception handling (missing/corrupt files).",
            "Implement analyzer self-audit logging.",
            "Sanitize malformed log entries.",
            "Validate zero memory leaks."
        ]),
        ("Phase 4: Refactor", "45 Minutes", COLOR_RED, [
            "AI-assisted code cleanup & optimization.",
            "Write comprehensive unittest suite.",
            "Format docstrings & generate README.",
            "Verify PEP 8 adherence."
        ]),
        ("Phase 5: Demo Prep", "30-45 Minutes", COLOR_GREEN, [
            "End-to-end integration walkthrough.",
            "Generate sample multi-size test logs.",
            "Rehearse 4-person live demo presentation.",
            "Verify all rubric criteria met."
        ])
    ]

    card_w = Inches(2.13)
    card_gap = Inches(0.27)
    top_pos = Inches(1.6)
    height = Inches(5.2)

    for i, (p_title, duration, col, bullets) in enumerate(steps):
        c = add_card(slide, Inches(0.8) + i * (card_w + card_gap), top_pos, card_w, height)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.22)

        # Title
        p0 = tf.paragraphs[0]
        p0.text = p_title
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(13.5)
        p0.font.bold = True
        p0.font.color.rgb = col

        # Duration
        p1 = tf.add_paragraph()
        p1.text = duration
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_after = Pt(12)

        # Bullets
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.name = FONT_BODY
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = COLOR_MUTED
            pb.space_after = Pt(6)


def build_slide_11(prs):
    """Slide 11: Evaluation Criteria Matrix (from problem image)."""
    slide = create_base_slide(prs, "10. EVALUATION RUBRIC", "Evaluation Criteria & Implementation Mapping")

    # Table Shape
    table_shape = slide.shapes.add_table(7, 4, Inches(0.8), Inches(1.6), Inches(11.73), Inches(5.2))
    table = table_shape.table
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(1.3)
    table.columns[2].width = Inches(5.83)
    table.columns[3].width = Inches(2.0)

    rubric_data = [
        ["Evaluation Component", "Weight", "Implementation Evidence in Project", "Status"],
        ["Log Parsing & Regex", "25%", "Modular compiled regex with ISO timestamp & group extractions", "100% Complete"],
        ["Analysis & Frequency", "25%", "collections.Counter isolating top error recurrence signatures", "100% Complete"],
        ["File / Data Structures", "15%", "Lazy generator iterators, dictionaries, and CSV serialization", "100% Complete"],
        ["Error Handling & Logging", "15%", "FileNotFoundError handling, skipped-line counting, internal audit log", "100% Complete"],
        ["Testing & Quality", "10%", "Automated unit test suite validating regex edge cases & counters", "100% Complete"],
        ["Live Demo & Presentation", "10%", "Interactive CLI demonstration with colored terminal output & reports", "100% Complete"]
    ]

    for row_idx, row_values in enumerate(rubric_data):
        for col_idx, val in enumerate(row_values):
            cell = table.cell(row_idx, col_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE

            cell.fill.solid()
            if row_idx == 0:
                cell.fill.fore_color.rgb = RGBColor(24, 38, 65)
            else:
                cell.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 1 else RGBColor(24, 33, 47)

            p_cell = cell.text_frame.paragraphs[0]
            p_cell.font.name = FONT_HEADING if row_idx == 0 else FONT_BODY
            p_cell.font.size = Pt(12) if row_idx == 0 else Pt(11)
            p_cell.font.bold = (row_idx == 0) or (col_idx == 3)

            if row_idx == 0:
                p_cell.font.color.rgb = COLOR_CYAN
            elif col_idx == 3:
                p_cell.font.color.rgb = COLOR_GREEN
            elif col_idx == 0:
                p_cell.font.color.rgb = COLOR_WHITE
            elif col_idx == 1:
                p_cell.font.color.rgb = COLOR_CYAN
            else:
                p_cell.font.color.rgb = COLOR_MUTED


def build_slide_12(prs):
    """Slide 12: Deliverables & Q&A."""
    slide = create_base_slide(prs, "11. CONCLUSION & DELIVERABLES", "Project Deliverables, CLI Demo & Discussion")

    # 3 Deliverable summary cards
    cards_data = [
        ("Console & CLI Report", COLOR_CYAN, [
            "Rich interactive terminal summary.",
            "ANSI colored severity alerts.",
            "Total logs, warning/error ratios, and top-5 frequent failures displayed."
        ]),
        ("CSV & Text Analytics", COLOR_GREEN, [
            "Structured error_distribution.csv exported.",
            "Breakdown of error message frequencies.",
            "Ready for ingestion into Excel, PowerBI, or cloud monitoring dashboards."
        ]),
        ("Tool Audit Log & Tests", COLOR_PURPLE, [
            "Internal application.log self-trace.",
            "Records processing progress, line counts, and skipped malformed rows.",
            "Complete unittest test suite included."
        ])
    ]

    c_w = Inches(3.73)
    c_gap = Inches(0.27)
    for i, (title, col, bullets) in enumerate(cards_data):
        c = add_card(slide, Inches(0.8) + i * (c_w + c_gap), Inches(1.6), c_w, Inches(2.7))
        populate_card_content(c, title, bullets, title_color=col, title_size=15, body_size=11)

    # Bottom Q&A Box
    qa_card = add_card(slide, Inches(0.8), Inches(4.55), Inches(11.73), Inches(2.25))
    tf_q = qa_card.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = tf_q.margin_right = Inches(0.3)
    tf_q.margin_top = Inches(0.2)

    p0 = tf_q.paragraphs[0]
    p0.text = "Ready for Questions & Live Demonstration"
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(20)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_WHITE
    p0.alignment = PP_ALIGN.CENTER
    p0.space_after = Pt(8)

    p_cli = tf_q.add_paragraph()
    p_cli.text = "CLI Command:  python3 main.py --input data/large_sample.log --top 5"
    p_cli.font.name = "Consolas"
    p_cli.font.size = Pt(13)
    p_cli.font.color.rgb = COLOR_CYAN
    p_cli.alignment = PP_ALIGN.CENTER
    p_cli.space_after = Pt(8)

    p_sub = tf_q.add_paragraph()
    p_sub.text = "Participants 1, 2, 3, and 4 are ready to demonstrate the code, regex engine, and test execution."
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_LIGHT_MUTED
    p_sub.alignment = PP_ALIGN.CENTER


# ==============================================================================
# DEEP-DIVE MODULE WALKTHROUGH SLIDES (actual project implementation)
# ==============================================================================

def build_reader_slide(prs):
    """src/reader.py — Stage 1 deep dive."""
    slide = create_base_slide(prs, "MODULE 1 of 4  ·  src/reader.py", "Stage 1 — File Ingestion & Memory-Safe Streaming")
    bullets = [
        "read_log_stream() is a GENERATOR: it uses 'yield' to hand back one line at a time instead of loading the whole file.",
        "Why: a 5 GB log file would crash the program if read with .read() or .readlines(). Streaming keeps memory flat.",
        "Validates the input first: non-empty path, the file exists, and it is a real file (not a folder).",
        "Raises precise errors — ValueError, FileNotFoundError, PermissionError — so the caller knows exactly what went wrong.",
        "Warns (but does not crash) when the file is empty, and logs every failure through its own named logger.",
    ]
    code = [
        "def read_log_stream(file_path):",
        "    if not os.path.exists(file_path):",
        "        raise FileNotFoundError(file_path)",
        "    with open(file_path, 'r') as fobj:",
        "        for line in fobj:",
        "            yield line   # one line at a time",
        "",
        "# Memory stays constant even for",
        "# multi-gigabyte input files.",
    ]
    add_split_slide(slide, "What reader.py does", COLOR_CYAN, bullets, "src/reader.py", code)


def build_parser_slide(prs):
    """src/parser.py — Stage 2 deep dive."""
    slide = create_base_slide(prs, "MODULE 2 of 4  ·  src/parser.py", "Stage 2 — Regex Parsing & Field Extraction")
    bullets = [
        "parse_log_line() turns a raw text line into a structured dictionary with 4 fields.",
        "Uses a COMPILED regex (re.compile) with named groups: timestamp, level, module, message.",
        "Why compiled: the pattern is built once and reused for every line — faster than recompiling each time.",
        "Returns None for any line that doesn't match the format — these 'malformed' lines are later counted, not silently dropped.",
        "This clean dict output is the contract the analyzer depends on.",
    ]
    code = [
        "LOG_PATTERN = re.compile(",
        "  r'(?P<timestamp>\\d{4}-..) '",
        "  r'\\[(?P<level>\\w+)\\] '",
        "  r'\\[(?P<module>\\w+)\\] '",
        "  r'(?P<message>.*)')",
        "",
        "match = LOG_PATTERN.match(line)",
        "if not match:",
        "    return None   # malformed line",
        "return match.groupdict()",
    ]
    add_split_slide(slide, "What parser.py does", COLOR_PURPLE, bullets, "src/parser.py", code)


def build_analyzer_slide(prs):
    """src/analyzer.py — Stage 3 deep dive."""
    slide = create_base_slide(prs, "MODULE 3 of 4  ·  src/analyzer.py", "Stage 3 — Counter-Based Statistical Analysis")
    bullets = [
        "LogAnalyzer holds several collections.Counter objects for levels, modules, errors, and warnings.",
        "ingest_events() consumes the line stream, calls the parser, and tallies every parsed event.",
        "Why Counter: it counts occurrences in O(1) per item and gives .most_common(n) for free — ideal for 'top recurring errors'.",
        "Errors/warnings are keyed as 'module: message' so identical failures from the same source cluster together.",
        "get_overall_summary() computes totals, skipped lines, and the parse-success rate for the report.",
    ]
    code = [
        "self.error_messages = Counter()",
        "",
        "def ingest_events(self, lines, parser_fn):",
        "    for line in lines:",
        "        event = parser_fn(line)",
        "        if not event:",
        "            continue   # skipped line",
        "        key = f\"{module}: {message}\"",
        "        self.error_messages[key] += 1",
        "",
        "get_top_errors -> most_common(n)",
    ]
    add_split_slide(slide, "What analyzer.py does", COLOR_ORANGE, bullets, "src/analyzer.py", code)


def build_reporter_slide(prs):
    """src/reporter.py — Stage 4 deep dive."""
    slide = create_base_slide(prs, "MODULE 4 of 4  ·  src/reporter.py", "Stage 4 — Reporting & Multi-Format Export")
    bullets = [
        "generate_console_summary() BUILDS and returns the formatted report string (printing is done by main.py — keeps it testable).",
        "export_text_report() writes the human-readable summary to reports/summary_report.txt.",
        "export_csv_breakdown() writes a machine-readable CSV (level counts + top warnings + top errors) for Excel / dashboards.",
        "Both exporters auto-create the output folder, so a missing reports/ directory never causes a crash.",
        "The --top N flag controls how many recurring errors/warnings appear in both outputs.",
    ]
    code = [
        "def _ensure_parent_dir(path):",
        "    parent = os.path.dirname(path)",
        "    if parent:",
        "        os.makedirs(parent, exist_ok=True)",
        "",
        "with open(file_path, 'w') as f:",
        "    f.write(report_text)",
        "",
        "writer = csv.writer(csvfile)",
        "writer.writerow(['Log Level', 'Count'])",
    ]
    add_split_slide(slide, "What reporter.py does", COLOR_GREEN, bullets, "src/reporter.py", code)


def build_error_handling_slide(prs):
    """Dedicated slide: error handling strategy & why."""
    slide = create_base_slide(prs, "RELIABILITY  ·  DEFENSIVE DESIGN", "Error Handling — What We Catch and Why")

    cards = [
        ("Specific over generic", COLOR_CYAN, [
            "reader raises FileNotFoundError, PermissionError, ValueError.",
            "Catching each type separately gives the user a clear, actionable message.",
            "Why: 'File does not exist' is far more useful than a raw stack trace.",
        ]),
        ("Fail soft on bad data", COLOR_ORANGE, [
            "parser returns None for malformed lines instead of throwing.",
            "One corrupt line should never stop analysis of the other 999,999.",
            "Skipped lines are counted and reported as a parse-success rate.",
        ]),
        ("Controlled exit in main", COLOR_RED, [
            "main wraps the pipeline in try/except.",
            "File errors vs. unexpected errors are handled separately.",
            "On failure it logs the cause and exits with status code 1.",
        ]),
    ]
    c_w = Inches(3.73)
    c_gap = Inches(0.27)
    for i, (title, col, bullets) in enumerate(cards):
        c = add_card(slide, Inches(0.8) + i * (c_w + c_gap), Inches(1.6), c_w, Inches(3.0))
        populate_card_content(c, title, bullets, title_color=col, title_size=15, body_size=11.5)

    bot = add_card(slide, Inches(0.8), Inches(4.8), Inches(11.73), Inches(2.0))
    populate_card_content(bot, "Why this matters", [
        "A log analyzer is an operations tool — it is run exactly when something is already going wrong.",
        "If the tool itself crashes on a missing file or one bad line, it fails the user at the worst possible moment.",
        "Graceful, specific error handling turns failures into clear guidance instead of confusing tracebacks.",
    ], title_color=COLOR_PURPLE, title_size=14, body_size=12)


def build_logging_slide(prs):
    """Dedicated slide: logging — why the logging library."""
    slide = create_base_slide(prs, "OBSERVABILITY  ·  LOGGING", "Logging — Why We Use Python's logging Library")

    bullets = [
        "Every module has its own named logger (LogAnalyzer.Reader, .Parser, .Analyzer, .Reporter, .Main).",
        "Why the logging library instead of print(): it adds timestamps, severity levels, and the source module automatically.",
        "Output goes to BOTH the console (live feedback) and application.log (a permanent audit trail).",
        "Log levels (INFO / WARNING / ERROR) let us separate normal progress from problems without changing code.",
        "This makes the tool debuggable in production: you can trace exactly which stage failed and when.",
    ]
    code = [
        "logging.basicConfig(",
        "  level=logging.INFO,",
        "  format='%(asctime)s - %(name)s'",
        "         ' - %(levelname)s - %(message)s',",
        "  handlers=[",
        "    logging.FileHandler('application.log'),",
        "    logging.StreamHandler(sys.stdout),",
        "  ])",
        "",
        "logger = logging.getLogger(",
        "    'LogAnalyzer.Reader')",
    ]
    add_split_slide(slide, "Logging strategy", COLOR_CYAN, bullets, "main.py — configure_app_logging()", code)


def build_testing_slide(prs):
    """Dedicated slide: importance of test cases."""
    slide = create_base_slide(prs, "QUALITY  ·  UNIT TESTING", "Test Cases — Why They Matter & What They Cover")

    cards = [
        ("TestReader", COLOR_CYAN, [
            "Verifies FileNotFoundError on a missing file.",
            "Confirms the generator yields the right number of lines.",
        ]),
        ("TestParser", COLOR_PURPLE, [
            "Checks valid lines extract level & module correctly.",
            "Confirms malformed / empty lines return None.",
        ]),
        ("TestAnalyzer", COLOR_ORANGE, [
            "Validates total vs. parsed line counts.",
            "Checks level counts and the top recurring error.",
        ]),
        ("TestReporter", COLOR_GREEN, [
            "Ensures the report string is built correctly.",
            "Confirms the CSV / text files are actually written.",
        ]),
    ]
    c_w = Inches(2.73)
    c_gap = Inches(0.27)
    for i, (title, col, bullets) in enumerate(cards):
        c = add_card(slide, Inches(0.8) + i * (c_w + c_gap), Inches(1.6), c_w, Inches(2.9))
        populate_card_content(c, title, bullets, title_color=col, title_size=15, body_size=11)

    bot = add_card(slide, Inches(0.8), Inches(4.7), Inches(11.73), Inches(2.1))
    populate_card_content(bot, "Why testing is essential", [
        "Each module is tested in isolation, so a failure points to the exact stage that broke.",
        "Tests act as a safety net: refactoring (e.g. renaming methods) is safe because the suite catches regressions.",
        "They document the expected behavior — a new teammate can read the tests to understand each module's contract.",
        "Run with:  python3 -m unittest test/test_cases.py -v",
    ], title_color=COLOR_CYAN, title_size=14, body_size=12)


# ==============================================================================
# MAIN GENERATOR ROUTINE
# ==============================================================================
def main():
    prs = Presentation()
    # 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    print("Generating Slide 1: Title Slide with Group of 4...")
    build_slide_1(prs)

    print("Generating Slide 2: Business Scenario & Objective...")
    build_slide_2(prs)

    print("Generating Slide 3: Input Data Schema & Anatomy...")
    build_slide_3(prs)

    print("Generating Slide 4: Functional Requirements (21-25)...")
    build_slide_4(prs)

    print("Generating Slide 5: Team Allocation (Group of 4)...")
    build_slide_5(prs)

    print("Generating Slide 6: Course Skills & Core Python Applied...")
    build_slide_6(prs)

    print("Generating Slide 7: System Architecture & Pipeline...")
    build_slide_7(prs)

    print("Generating Deep Dive: reader.py (Stage 1)...")
    build_reader_slide(prs)

    print("Generating Deep Dive: parser.py (Stage 2)...")
    build_parser_slide(prs)

    print("Generating Deep Dive: analyzer.py (Stage 3)...")
    build_analyzer_slide(prs)

    print("Generating Deep Dive: reporter.py (Stage 4)...")
    build_reporter_slide(prs)

    print("Generating Slide: Error Handling Strategy...")
    build_error_handling_slide(prs)

    print("Generating Slide: Logging & Observability...")
    build_logging_slide(prs)

    print("Generating Slide: Testing & Quality...")
    build_testing_slide(prs)

    print("Generating Slide 8: Key Performance Benchmarks...")
    build_slide_8(prs)

    print("Generating Slide 9: Top Recurring Errors Table...")
    build_slide_9(prs)

    print("Generating Slide 10: 4-5 Hour Execution Roadmap...")
    build_slide_10(prs)

    print("Generating Slide 11: Evaluation Criteria Matrix...")
    build_slide_11(prs)

    print("Generating Slide 12: Deliverables & Q&A...")
    build_slide_12(prs)

    output_filename = "Log_File_Analyzer_Presentation.pptx"
    prs.save(output_filename)
    print(f"\n[SUCCESS] PowerPoint deck created successfully: {output_filename}")
    print(f"Total Slides: {len(prs.slides)} (16:9 Widescreen)")


if __name__ == "__main__":
    main()