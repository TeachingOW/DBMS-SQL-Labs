#!/usr/bin/env python3
"""
Convert DBMS SQL Lab markdown files to HTML with enhanced table formatting
"""

import os
import re
import markdown
from pathlib import Path

def convert_markdown_to_html(md_content, title="SQL Lab"):
    """Convert markdown content to HTML with custom styling"""
    
    # HTML template with enhanced styling
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        
        h2 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}
        
        h3 {{
            color: #2c3e50;
            margin-top: 25px;
            margin-bottom: 10px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
            border: 1px solid #2980b9;
        }}
        
        td {{
            padding: 12px;
            border: 1px solid #ddd;
            vertical-align: top;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        tr:hover {{
            background-color: #e8f4f8;
        }}
        
        .result-table {{
            border: 2px solid #27ae60;
        }}
        
        .result-table th {{
            background-color: #27ae60;
        }}
        
        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            position: relative;
        }}
        
        pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
        }}
        
        code {{
            background-color: #f8f9fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e83e8c;
        }}
        
        .sql-code {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
            overflow-x: auto;
            position: relative;
        }}
        
        .sql-code::before {{
            content: "SQL";
            position: absolute;
            top: 5px;
            right: 10px;
            background-color: #e74c3c;
            color: white;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 12px;
            font-weight: bold;
        }}
        
        blockquote {{
            background-color: #e8f6f3;
            padding: 15px;
            border-left: 4px solid #27ae60;
            margin: 15px 0;
            border-radius: 5px;
        }}
        
        .note {{
            background-color: #cce5ff;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #007bff;
            margin: 15px 0;
        }}
        
        .warning {{
            background-color: #fdf2e9;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #e67e22;
            margin: 15px 0;
        }}
        
        .navigation {{
            background-color: #34495e;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .nav-button {{
            background-color: #3498db;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 0 5px;
            text-decoration: none;
            display: inline-block;
        }}
        
        .nav-button:hover {{
            background-color: #2980b9;
        }}
        
        ul, ol {{
            padding-left: 20px;
        }}
        
        li {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="navigation">
            <a href="html_viewer.html" class="nav-button">← Back to Labs Overview</a>
            <a href="#" class="nav-button">Print Version</a>
        </div>
        
        {{content}}
        
        <div class="navigation" style="margin-top: 40px;">
            <a href="html_viewer.html" class="nav-button">← Back to Labs Overview</a>
        </div>
    </div>
</body>
</html>"""
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])
    html_content = md.convert(md_content)
    
    # Post-process HTML to enhance SQL code blocks
    html_content = re.sub(
        r'<pre><code class="language-sql">(.*?)</code></pre>',
        r'<div class="sql-code">\1</div>',
        html_content,
        flags=re.DOTALL
    )
    
    # Enhance regular code blocks
    html_content = re.sub(
        r'<pre><code>(.*?)</code></pre>',
        r'<pre><code>\1</code></pre>',
        html_content,
        flags=re.DOTALL
    )
    
    # Mark result tables
    html_content = re.sub(
        r'<table>',
        r'<table class="result-table">',
        html_content
    )
    
    return html_template.format(title=title, content=html_content)

def convert_lab_file(input_file, output_file):
    """Convert a single lab markdown file to HTML"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract title from filename or first heading
        title = Path(input_file).stem.replace('_', ' ').title()
        if md_content.startswith('#'):
            title = md_content.split('\n')[0].strip('# ')
        
        html_content = convert_markdown_to_html(md_content, title)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Converted: {input_file} → {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting {input_file}: {e}")
        return False

def main():
    """Convert all lab markdown files to HTML"""
    base_dir = Path('.')
    html_dir = base_dir / 'html_labs'
    html_dir.mkdir(exist_ok=True)
    
    # Find all markdown files in all directories (excluding README files)
    lab_files = []
    for directory in ['labs', 'inclass', 'other', 'code']:
        if (base_dir / directory).exists():
            lab_files.extend((base_dir / directory).glob('**/*.md'))
    
    # Filter out README files
    lab_files = [f for f in lab_files if 'readme' not in f.name.lower() and 'README' not in f.name]
    
    converted_count = 0
    total_files = len(lab_files)
    
    print(f"🔄 Converting {total_files} lab files to HTML...")
    print("=" * 50)
    
    for md_file in lab_files:
        html_file = html_dir / f"{md_file.stem}.html"
        if convert_lab_file(md_file, html_file):
            converted_count += 1
    
    print("=" * 50)
    print(f"✨ Conversion complete: {converted_count}/{total_files} files converted")
    print(f"📁 HTML files saved in: {html_dir}")
    
    # Create an index file
    create_index_file(html_dir, lab_files)

def create_index_file(html_dir, lab_files):
    """Create an index HTML file listing all converted labs"""
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DBMS SQL Labs - HTML Version</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        .lab-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .lab-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
            transition: transform 0.2s;
        }
        .lab-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .lab-link {
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
            font-size: 18px;
        }
        .lab-link:hover {
            color: #2980b9;
        }
        .lab-type {
            background-color: #3498db;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-bottom: 10px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🗄️ DBMS SQL Labs - HTML Version</h1>
        <p style="text-align: center; color: #666;">Enhanced HTML versions of all SQL labs with better table formatting</p>
        
        <div class="lab-grid">"""
    
    for md_file in sorted(lab_files):
        lab_type = "In-Class" if "inclass" in str(md_file) else "Lab"
        lab_name = md_file.stem.replace('_', ' ').title()
        html_filename = f"{md_file.stem}.html"
        
        index_content += f"""
            <div class="lab-card">
                <div class="lab-type">{lab_type}</div>
                <a href="{html_filename}" class="lab-link">{lab_name}</a>
                <p style="margin-top: 10px; color: #666; font-size: 14px;">
                    Enhanced HTML version with interactive tables and better formatting
                </p>
            </div>"""
    
    index_content += """
        </div>
        
        <div style="text-align: center; margin-top: 40px; padding: 20px; background-color: #e8f6f3; border-radius: 8px;">
            <p><strong>💡 Tip:</strong> These HTML versions provide better table formatting and interactive features compared to the original markdown files.</p>
            <a href="../html_viewer.html" style="background-color: #27ae60; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">← Back to Main Overview</a>
        </div>
    </div>
</body>
</html>"""
    
    index_file = html_dir / 'index.html'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"📋 Index file created: {index_file}")

if __name__ == "__main__":
    main()