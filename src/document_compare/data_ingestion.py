import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException


class DocumentComparator:
    def __init__(self):
        pass 
    def delete_existing_files(self):
        """
        Delets exisiting files at the specific loaction
        """
        pass 
    def save_uploaded_files(self,reference_file, actual_file):
        """
        Saves uploaded files to a specific directory.
        """
        pass 

    def read_pdf(self,pdf_path: Path)->str:
        """
        Reads a PDF file and extracts text from each page.
        """
        pass     

