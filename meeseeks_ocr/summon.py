import argparse
import sys

from meeseeks_ocr.ocr_task import run_ocr

def main():
    parser = argparse.ArgumentParser(description="Meeseeks OCR: Extract text from scanned PDFs")
    parser.add_argument("-i", "--input", required=True, help="Path to the PDF file to be processed")
    parser.add_argument("-o", "--output", help="Path to the output file")

    args = parser.parse_args()

    # Run the OCR task and capture result
    try:
        ocr_output = run_ocr(args.input)

        lines = ocr_output.splitlines()
        line_count = len(lines)

        # If output is specified, write to file
        # If output is not specified, print to console
        # If the output is less than or equal to 500 lines, print it to the console
        # If the output is more than 500 lines, print a message: Output is too long to print and exit
        if args.output:
            with open(args.output, "w") as f:
                f.write(ocr_output)
            print(f"Output written to {args.output}")
        else:
            if line_count <= 500:
                print("=== OCR Output ===")
                print(ocr_output)
            else:
                print("Output exceeds 500 lines.")
                print("Output is too long to print. Please re-run with:")
                print(" --output <output_file>")
                sys.exit(1)

    except Exception as e:
        print(f"Oh no! Well I do that because: {e}")
