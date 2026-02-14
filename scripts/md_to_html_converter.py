#!/usr/bin/env python3
"""
Convert Markdown files to HTML.

If the external `markdown` package is available, use it.
Otherwise, use an internal parser that supports common Markdown features:
- headings
- paragraphs
- unordered/ordered lists
- fenced code blocks
- tables
- blockquotes
- links, bold, italics, inline code
"""

import html
import re
import sys
from pathlib import Path

try:
    import markdown as markdown_pkg  # type: ignore
except Exception:
    markdown_pkg = None

def get_html_template(title, content):
    """Generate HTML template with consistent styling"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; }}
        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        
        /* Code block wrapper with copy button */
        .code-block-wrapper {{
          position: relative;
          margin: 20px 0;
          max-width: 100%;
        }}
        
        .code-block-wrapper pre {{
          margin: 0;
          overflow-x: auto;
          max-width: 100%;
        }}
        
        .copy-button {{
          position: absolute;
          top: 8px;
          right: 8px;
          padding: 6px 8px;
          background-color: rgba(255, 255, 255, 0.9);
          border: 1px solid #ddd;
          border-radius: 4px;
          cursor: pointer;
          opacity: 0.7;
          transition: opacity 0.2s, background-color 0.2s;
          display: flex;
          align-items: center;
          gap: 4px;
        }}
        
        .copy-button:hover {{
          opacity: 1;
          background-color: #fff;
        }}
        
        .copy-button:active {{
          background-color: #e0e0e0;
        }}
        
        .copy-button.copied {{
          background-color: #4caf50;
          color: white;
          border-color: #4caf50;
        }}
        
        .copy-button svg {{
          display: block;
        }}
        
        h1, h2, h3, h4 {{ color: #333; }}
        h1 {{ border-bottom: 2px solid #ddd; padding-bottom: 10px; }}
        h2 {{ border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 30px; }}
        ul, ol {{ margin-left: 20px; }}
        blockquote {{ 
            border-left: 4px solid #ddd; 
            margin-left: 0; 
            padding-left: 20px; 
            color: #666; 
        }}
    </style>

    <!-- Syntax highlighting with highlight.js -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
    <script>hljs.highlightAll();</script>
    
    <script>
    function copyCode(button) {{
        const wrapper = button.closest('.code-block-wrapper');
        const codeBlock = wrapper.querySelector('code');
        const text = codeBlock.textContent;
        
        navigator.clipboard.writeText(text).then(() => {{
            button.classList.add('copied');
            button.textContent = 'Copied!';
            setTimeout(() => {{
                button.classList.remove('copied');
                button.innerHTML = `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 2h8a2 2 0 0 1 2 2v8M4 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>`;
            }}, 2000);
        }});
    }}
    </script>
</head>
<body>
{content}
</body>
</html>"""


def copy_button_html():
    return """<button class="copy-button" onclick="copyCode(this)" title="Copy code">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4 2h8a2 2 0 0 1 2 2v8M4 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>"""

def add_copy_buttons_to_code_blocks(html_content):
    """Add copy buttons to code blocks"""
    pattern = r'<pre><code([^>]*)>(.*?)</code></pre>'
    
    def replacer(match):
        code_attrs = match.group(1)
        code_content = match.group(2)
        
        return f'''<div class="code-block-wrapper">
  <pre><code{code_attrs}>{code_content}</code></pre>
  {copy_button_html()}
</div>'''
    
    return re.sub(pattern, replacer, html_content, flags=re.DOTALL)


def convert_inline(text):
    """Convert inline markdown markup to HTML."""
    placeholders = []

    def stash(value):
        idx = len(placeholders)
        placeholders.append(value)
        return f"@@@{idx}@@@"

    # Protect inline code first.
    text = re.sub(r'`([^`]+)`', lambda m: stash(("code", m.group(1))), text)
    # Protect links.
    text = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        lambda m: stash(("link", m.group(1), m.group(2))),
        text,
    )

    text = html.escape(text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)

    for i, value in enumerate(placeholders):
        token = f"@@@{i}@@@"
        if value[0] == "code":
            replacement = f"<code>{html.escape(value[1])}</code>"
        else:
            replacement = (
                f'<a href="{html.escape(value[2], quote=True)}">'
                f"{html.escape(value[1])}</a>"
            )
        text = text.replace(token, replacement)

    return text


def split_table_row(line):
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [convert_inline(cell.strip()) for cell in row.split("|")]


def simple_markdown_to_html(md_content):
    """A lightweight markdown-to-html converter for common markdown features."""
    lines = md_content.splitlines()
    html_parts = []
    paragraph = []
    in_ul = False
    in_ol = False
    in_code = False
    code_lang = ""
    code_lines = []
    i = 0

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            html_parts.append(f"<p>{convert_inline(' '.join(paragraph).strip())}</p>")
            paragraph = []

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            html_parts.append("</ul>")
            in_ul = False
        if in_ol:
            html_parts.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if in_code:
            if stripped.startswith("```"):
                cls = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                code_html = html.escape("\n".join(code_lines))
                html_parts.append(
                    f'<div class="code-block-wrapper">\n'
                    f'  <pre><code{cls}>{code_html}</code></pre>\n'
                    f"  {copy_button_html()}\n"
                    f"</div>"
                )
                in_code = False
                code_lang = ""
                code_lines = []
            else:
                code_lines.append(line)
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            close_lists()
            in_code = True
            code_lang = stripped[3:].strip()
            code_lines = []
            i += 1
            continue

        # Table block: header + separator + rows.
        if (
            "|" in stripped
            and i + 1 < len(lines)
            and re.match(r'^\s*\|?[:\-\s|]+\|?\s*$', lines[i + 1].strip())
            and "-" in lines[i + 1]
        ):
            flush_paragraph()
            close_lists()
            header_cells = split_table_row(lines[i])
            i += 2  # skip header + separator
            body_rows = []
            while i < len(lines):
                row = lines[i].strip()
                if not row or "|" not in row:
                    break
                body_rows.append(split_table_row(lines[i]))
                i += 1

            html_parts.append("<table>")
            html_parts.append("  <thead>")
            html_parts.append("    <tr>")
            for cell in header_cells:
                html_parts.append(f"      <th>{cell}</th>")
            html_parts.append("    </tr>")
            html_parts.append("  </thead>")
            if body_rows:
                html_parts.append("  <tbody>")
                for row in body_rows:
                    html_parts.append("    <tr>")
                    for cell in row:
                        html_parts.append(f"      <td>{cell}</td>")
                    html_parts.append("    </tr>")
                html_parts.append("  </tbody>")
            html_parts.append("</table>")
            continue

        # Heading.
        heading = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if heading:
            flush_paragraph()
            close_lists()
            level = len(heading.group(1))
            text = convert_inline(heading.group(2).strip())
            html_parts.append(f"<h{level}>{text}</h{level}>")
            i += 1
            continue

        # Horizontal rule.
        if re.match(r'^([-*_])\1{2,}\s*$', stripped):
            flush_paragraph()
            close_lists()
            html_parts.append("<hr>")
            i += 1
            continue

        # Unordered list.
        ul = re.match(r'^\s*[-*+]\s+(.*)$', line)
        if ul:
            flush_paragraph()
            if in_ol:
                html_parts.append("</ol>")
                in_ol = False
            if not in_ul:
                html_parts.append("<ul>")
                in_ul = True
            html_parts.append(f"<li>{convert_inline(ul.group(1).strip())}</li>")
            i += 1
            continue

        # Ordered list.
        ol = re.match(r'^\s*\d+\.\s+(.*)$', line)
        if ol:
            flush_paragraph()
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            if not in_ol:
                html_parts.append("<ol>")
                in_ol = True
            html_parts.append(f"<li>{convert_inline(ol.group(1).strip())}</li>")
            i += 1
            continue

        # Blockquote line.
        block = re.match(r'^\s*>\s?(.*)$', line)
        if block:
            flush_paragraph()
            close_lists()
            html_parts.append(f"<blockquote>{convert_inline(block.group(1))}</blockquote>")
            i += 1
            continue

        # Blank line.
        if not stripped:
            flush_paragraph()
            close_lists()
            i += 1
            continue

        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    close_lists()
    return "\n".join(html_parts)

def convert_md_to_html(md_file_path, output_path):
    """Convert a markdown file to HTML"""
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    if markdown_pkg is not None:
        md = markdown_pkg.Markdown(
            extensions=[
                "extra",
                "codehilite",
                "fenced_code",
                "tables",
                "toc",
            ]
        )
        html_content = md.convert(md_content)
        html_content = add_copy_buttons_to_code_blocks(html_content)
    else:
        html_content = simple_markdown_to_html(md_content)
    
    # Extract title from first H1 or use filename
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1))  # Remove any HTML tags
    else:
        title = Path(md_file_path).stem.replace('_', ' ')
    
    # Generate full HTML
    full_html = get_html_template(title, html_content)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Converted {md_file_path} -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md_to_html_converter.py <input.md> <output.html>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not Path(input_file).exists():
        print(f"Error: Input file {input_file} does not exist")
        sys.exit(1)
    
    convert_md_to_html(input_file, output_file)
