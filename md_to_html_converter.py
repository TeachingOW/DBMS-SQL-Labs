#!/usr/bin/env python3
"""
Convert Markdown files to HTML with proper styling matching the existing HTML labs
"""

import markdown
import sys
import re
from pathlib import Path

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
<div style="background-color: #e7f3ff; padding: 15px; margin-bottom: 20px; border-radius: 5px;">
  <p style="margin: 0;">
    <a href="../../LAB_INDEX.html">📚 Back to Lab Index</a> | 
    <a href="../../Readme.html">🏠 Home</a>
  </p>
</div>

{content}

</body>
</html>"""

def add_copy_buttons_to_code_blocks(html_content):
    """Add copy buttons to code blocks"""
    pattern = r'<pre><code([^>]*)>(.*?)</code></pre>'
    
    def replacer(match):
        code_attrs = match.group(1)
        code_content = match.group(2)
        
        return f'''<div class="code-block-wrapper">
  <pre><code{code_attrs}>{code_content}</code></pre>
  <button class="copy-button" onclick="copyCode(this)" title="Copy code">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4 2h8a2 2 0 0 1 2 2v8M4 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>
</div>'''
    
    return re.sub(pattern, replacer, html_content, flags=re.DOTALL)

def convert_md_to_html(md_file_path, output_path):
    """Convert a markdown file to HTML"""
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML with extensions
    md = markdown.Markdown(extensions=[
        'extra',  # Tables, footnotes, etc.
        'codehilite',  # Code highlighting
        'fenced_code',  # Fenced code blocks
        'tables',  # Table support
        'toc',  # Table of contents
    ])
    
    html_content = md.convert(md_content)
    
    # Add copy buttons to code blocks
    html_content = add_copy_buttons_to_code_blocks(html_content)
    
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
