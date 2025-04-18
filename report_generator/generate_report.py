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

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    pdfkit.from_string(rendered, output_path, configuration=config)
    print(f"[+] Styled PDF report saved as {output}")
