import argparse
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scan_engine.nmap_scanner import scan_target
from report_generator.generate_report import generate_pdf


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True, help="Target IP address")
    args = parser.parse_args()

    results = scan_target(args.target)

    if not results:
        print("[!] No data returned from scan. Skipping report generation.")
    else:
        generate_pdf(results, output=f'report_{args.target}.pdf')
