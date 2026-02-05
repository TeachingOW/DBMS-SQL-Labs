#!/usr/bin/env python3
"""
Script to enhance HTML files:
1. Fix markdown links (.md to .html)
2. Convert markdown headings in paragraphs (### to <h3>)
3. Convert bold markdown (**text** to <strong>text</strong>)
4. Convert markdown tables to HTML tables
5. Add copy buttons to code blocks
6. Add CSS to prevent code blocks from spanning full page width
"""

import re
import os
import sys
from pathlib import Path


def convert_markdown_table_to_html(markdown_table):
    """Convert a markdown table to HTML table format."""
    lines = [line.strip() for line in markdown_table.strip().split('\n') if line.strip()]
    
    if len(lines) < 2:
        return markdown_table  # Not a valid table
    
    # Check if it's a markdown table (should have | characters)
    if not all('|' in line for line in lines):
        return markdown_table
    
    html_parts = ['<table>']
    
    # Process header row
    header_cells = [cell.strip() for cell in lines[0].split('|') if cell.strip()]
    if header_cells:
        html_parts.append('  <thead>')
        html_parts.append('    <tr>')
        for cell in header_cells:
            html_parts.append(f'      <th>{cell}</th>')
        html_parts.append('    </tr>')
        html_parts.append('  </thead>')
    
    # Skip separator row (line with dashes)
    start_row = 2 if len(lines) > 1 and re.match(r'^[\s\|:\-]+$', lines[1]) else 1
    
    # Process body rows
    if start_row < len(lines):
        html_parts.append('  <tbody>')
        for line in lines[start_row:]:
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells:
                html_parts.append('    <tr>')
                for cell in cells:
                    html_parts.append(f'      <td>{cell}</td>')
                html_parts.append('    </tr>')
        html_parts.append('  </tbody>')
    
    html_parts.append('</table>')
    return '\n'.join(html_parts)


def add_copy_buttons_to_code_blocks(html_content):
    """Add copy buttons to code blocks in HTML content."""
    
    # Pattern to match <pre><code>...</code></pre> blocks
    pattern = r'(<pre>)(<code[^>]*>)(.*?)(</code></pre>)'
    
    def replacer(match):
        pre_open = match.group(1)
        code_open = match.group(2)
        code_content = match.group(3)
        code_close = match.group(4)
        
        # Add a wrapper div with copy button
        return f'''<div class="code-block-wrapper">
  {pre_open}{code_open}{code_content}{code_close}
  <button class="copy-button" onclick="copyCode(this)" title="Copy code">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4 2h8a2 2 0 0 1 2 2v8M4 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>
</div>'''
    
    return re.sub(pattern, replacer, html_content, flags=re.DOTALL)


def convert_bold_markdown(html_content):
    """Convert **text** to <strong>text</strong> in HTML content."""
    # Replace **text** with <strong>text</strong>
    # Simple pattern that matches **text** not inside HTML tags
    pattern = r'\*\*([^\*\n]+?)\*\*'
    
    def replacer(match):
        text = match.group(1)
        # Don't replace if inside an HTML tag (basic check)
        return f'<strong>{text}</strong>'
    
    html_content = re.sub(pattern, replacer, html_content)
    return html_content


def convert_markdown_headings_in_paragraphs(html_content):
    """Convert ### Heading in <p> tags to proper <h3> tags."""
    # Match <p>### followed by text
    pattern = r'<p>###\s+([^<\n]+?)(?:\s*\n|</p>)'
    
    def replacer(match):
        heading_text = match.group(1).strip()
        return f'<h3>{heading_text}</h3>\n<p>'
    
    html_content = re.sub(pattern, replacer, html_content)
    
    # Clean up any <p> tags that are now empty or just have closing tags
    html_content = re.sub(r'<p>\s*</p>', '', html_content)
    
    return html_content


def fix_markdown_links(html_content):
    """Convert .md links to .html links in HTML files."""
    # Replace href="*.md" with href="*.html"
    # Handle both regular links and links with paths
    html_content = re.sub(r'href="([^"]*?)\.md"', r'href="\1.html"', html_content)
    return html_content


def convert_markdown_tables_in_html(html_content):
    """Find and convert markdown tables in HTML content."""
    
    # Pattern to find markdown tables (multiple lines starting with |)
    # This pattern matches blocks of lines that start with |
    lines = html_content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a markdown table
        if line.strip().startswith('|') and '|' in line:
            # Check if the line before ends with <p> without closing
            if result_lines and '<p>' in result_lines[-1] and '</p>' not in result_lines[-1]:
                # Close the paragraph before the table
                result_lines[-1] = result_lines[-1] + '</p>'
            
            # Collect all consecutive table lines
            table_lines = []
            j = i
            while j < len(lines):
                stripped = lines[j].strip()
                if stripped.startswith('|'):
                    # Remove any trailing </p> from table line
                    cleaned = stripped.replace('</p>', '').strip()
                    table_lines.append(cleaned)
                    j += 1
                elif stripped == '</p>':
                    # Skip standalone </p> after table
                    j += 1
                    break
                else:
                    break
            
            # Convert the table if we have at least 2 lines (header + separator or header + data)
            if len(table_lines) >= 2:
                markdown_table = '\n'.join(table_lines)
                html_table = convert_markdown_table_to_html(markdown_table)
                result_lines.append(html_table)
                i = j
            else:
                result_lines.append(line)
                i += 1
        else:
            result_lines.append(line)
            i += 1
    
    return '\n'.join(result_lines)


def add_css_and_js(html_content):
    """Add CSS for copy buttons and JS for copy functionality."""
    
    # CSS for copy button and code block wrapper
    css = """
    /* Code block wrapper with copy button */
    .code-block-wrapper {
      position: relative;
      margin: 20px 0;
      max-width: 100%;
    }
    
    .code-block-wrapper pre {
      margin: 0;
      overflow-x: auto;
      max-width: 100%;
    }
    
    .copy-button {
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
    }
    
    .copy-button:hover {
      opacity: 1;
      background-color: #fff;
    }
    
    .copy-button:active {
      background-color: #e0e0e0;
    }
    
    .copy-button.copied {
      background-color: #4caf50;
      color: white;
      border-color: #4caf50;
    }
    
    .copy-button svg {
      display: block;
    }
    """
    
    # JavaScript for copy functionality
    js = """
    function copyCode(button) {
      const wrapper = button.closest('.code-block-wrapper');
      const codeBlock = wrapper.querySelector('code');
      const text = codeBlock.textContent;
      
      // Copy to clipboard
      navigator.clipboard.writeText(text).then(() => {
        // Show success feedback
        button.classList.add('copied');
        const originalHTML = button.innerHTML;
        button.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M13 4L6 11L3 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
        
        // Reset after 2 seconds
        setTimeout(() => {
          button.classList.remove('copied');
          button.innerHTML = originalHTML;
        }, 2000);
      }).catch(err => {
        console.error('Failed to copy:', err);
        alert('Failed to copy code');
      });
    }
    """
    
    # Insert CSS before </style> or </head>
    if '</style>' in html_content:
        html_content = html_content.replace('</style>', f'{css}\n    </style>')
    elif '</head>' in html_content:
        html_content = html_content.replace('</head>', f'<style>{css}</style>\n</head>')
    
    # Insert JS before </body>
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', f'<script>\n{js}\n  </script>\n</body>')
    
    return html_content


def process_html_file(file_path):
    """Process a single HTML file."""
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Step 1: Fix markdown links (.md to .html)
    content = fix_markdown_links(content)
    
    # Step 2: Convert markdown headings in paragraphs
    content = convert_markdown_headings_in_paragraphs(content)
    
    # Step 3: Convert bold markdown (**text** to <strong>text</strong>)
    content = convert_bold_markdown(content)
    
    # Step 4: Convert markdown tables to HTML
    content = convert_markdown_tables_in_html(content)
    
    # Step 5: Add copy buttons to code blocks (if not already added)
    if 'code-block-wrapper' not in content:
        content = add_copy_buttons_to_code_blocks(content)
    
    # Step 6: Add CSS and JavaScript (if not already added)
    if 'copyCode' not in content:
        content = add_css_and_js(content)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Completed {file_path}")
    else:
        print(f"⚠ No changes needed for {file_path}")



def main():
    """Main function to process all HTML files."""
    html_labs_dir = Path('/home/runner/work/DBMS-SQL-Labs/DBMS-SQL-Labs/html_labs')
    
    if not html_labs_dir.exists():
        print(f"Error: Directory {html_labs_dir} does not exist")
        sys.exit(1)
    
    html_files = list(html_labs_dir.glob('*.html'))
    
    if not html_files:
        print("No HTML files found")
        sys.exit(1)
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    for html_file in sorted(html_files):
        try:
            process_html_file(html_file)
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
            continue
    
    print(f"\n✓ All {len(html_files)} files processed successfully!")


if __name__ == '__main__':
    main()
