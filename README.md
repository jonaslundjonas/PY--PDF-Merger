# PY--PDF-Merger
Merges PDF files to one file

Written by Jonas Lund 2024

Description:
This script combines multiple PDF files into a single PDF file.
The script will detect all PDF files in its directory and merge them.

Requirements:
- Python 3.6 or higher
- PyPDF2 library (install using: pip install PyPDF2)

How to use:
1. Place this script in a folder with your PDF files
2. Run the script
3. Select which PDFs to merge and their order
4. The merged file will be saved in the same directory

Output:
- Creates a single PDF file containing all pages from selected PDFs
- Original files remain unchanged
- Files are merged in the selected order
- Output is saved as 'merged_output.pdf'

Note: The script preserves all content and formatting from the original PDFs.
