import os
import pdfkit
from jinja2 import Template

def generate_pdf(data, output='report.pdf'):
    with open('report_generator/report_template.html', 'r', encoding='utf-8') as f:
        template = Template(f.read())
    
    output_dir = 'scan_reports'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output)
    
    rendered = template.render(results=data)
    
    topdf_exe_windows_path = os.path.join( os.path.join('Utilities', 'wkhtmltopdf-windows'), 'wkhtmltopdf.exe')
    
    config = pdfkit.configuration(wkhtmltopdf=topdf_exe_windows_path)

    pdfkit.from_string(rendered, output_path, configuration=config)
    print(f"[+] Styled PDF report saved as {output}")
