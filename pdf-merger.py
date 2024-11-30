"""
PDF Merger Script
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
"""

import os
from PyPDF2 import PdfReader, PdfWriter
import datetime

def get_pdf_files():
    """Get all PDF files in the script's directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_files = [f for f in os.listdir(script_dir) if f.lower().endswith('.pdf')]
    return pdf_files, script_dir

def display_files(pdf_files):
    """Display available PDF files with their details."""
    print("\nAvailable PDF files:")
    print("-" * 60)
    print(f"{'No.':<4}{'Filename':<40}{'Pages':<8}{'Size':<8}")
    print("-" * 60)
    
    for i, pdf in enumerate(pdf_files, 1):
        try:
            reader = PdfReader(pdf)
            pages = len(reader.pages)
            size_mb = os.path.getsize(pdf) / (1024 * 1024)
            print(f"{i:<4}{pdf:<40}{pages:<8}{size_mb:.1f}MB")
        except Exception as e:
            print(f"{i:<4}{pdf:<40}Error: {str(e)}")
    print("-" * 60)

def get_file_selection(pdf_files):
    """Let user select which files to merge and in what order."""
    selected_files = []
    
    while True:
        print("\nCurrently selected files:")
        if selected_files:
            for i, file in enumerate(selected_files, 1):
                print(f"{i}. {file}")
        else:
            print("No files selected yet")
        
        print("\nOptions:")
        print("- Enter a number (1-{}) to add a file".format(len(pdf_files)))
        print("- Enter 'r' to remove the last file")
        print("- Enter 'c' to clear selection")
        print("- Enter 'd' to display files again")
        print("- Enter 'm' to merge selected files (need at least 2 files)")
        print("- Enter 'q' to quit")
        
        choice = input("\nEnter your choice: ").lower().strip()
        
        if choice == 'q':
            return None
        elif choice == 'r':
            if selected_files:
                removed = selected_files.pop()
                print(f"Removed: {removed}")
            else:
                print("No files to remove!")
        elif choice == 'c':
            selected_files = []
            print("Selection cleared")
        elif choice == 'd':
            display_files(pdf_files)
        elif choice == 'm':
            if len(selected_files) >= 2:
                return selected_files
            else:
                print("Please select at least 2 files before merging!")
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(pdf_files):
                    selected_files.append(pdf_files[idx])
                    print(f"Added: {pdf_files[idx]}")
                else:
                    print(f"Please enter a number between 1 and {len(pdf_files)}")
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {len(pdf_files)} or one of the commands (r/c/d/m/q)")

def merge_pdfs(files, output_filename):
    """Merge selected PDF files into a single PDF."""
    merger = PdfWriter()
    
    total_pages = 0
    for filename in files:
        reader = PdfReader(filename)
        total_pages += len(reader.pages)
        for page in reader.pages:
            merger.add_page(page)
    
    # Add metadata
    merger.add_metadata({
        '/Producer': 'PDF Merger Script by Jonas Lund',
        '/Creator': 'PDF Merger Script',
        '/CreationDate': datetime.datetime.now().strftime('D:%Y%m%d%H%M%S'),
        '/Title': 'Merged PDF Document',
    })
    
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)
    
    return total_pages

def main():
    try:
        # Get list of PDF files
        pdf_files, script_dir = get_pdf_files()
        
        if not pdf_files:
            print("No PDF files found in the script's directory!")
            return
        
        # Display available files
        display_files(pdf_files)
        
        # Get user selection
        selected_files = get_file_selection(pdf_files)
        
        if not selected_files:
            print("Operation cancelled")
            return
        
        # Create output filename
        output_filename = 'merged_output.pdf'
        if os.path.exists(output_filename):
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_filename = f'merged_output_{timestamp}.pdf'
        
        # Merge PDFs
        print("\nMerging PDFs...")
        total_pages = merge_pdfs(selected_files, output_filename)
        
        print(f"\nSuccess! Merged {len(selected_files)} files ({total_pages} pages total)")
        print(f"Output saved as: {output_filename}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
