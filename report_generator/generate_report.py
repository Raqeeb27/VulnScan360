import os
import pdfkit
from jinja2 import Template

def generate_pdf(data, output='report.pdf'):
    with open('report_generator/report_template.html', 'r', encoding='utf-8') as f:
        template = Template(f.read())

    rendered = template.render(results=data)

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    pdfkit.from_string(rendered, os.path.join('scan_reports', output), configuration=config)
    print(f"[+] Styled PDF report saved as {output}")
