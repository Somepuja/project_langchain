# Property Sale Notice Extraction System.
## Description:
Developed an advanced document processing system that extracts critical information from property sale notices using computer vision and natural language processing. The solution automatically processes PDF documents, converts them to images, identifies and crops relevant sections using OpenCV, and employs LangChain with Hugging Face models to extract structured data including borrower details, property specifications, financial values, and auction information. The system intelligently converts Indian numerical formats (lac/crore) to standard numeric form and outputs organized data in Excel format for easy analysis.

## Key Technical Achievements:
- Implemented PDF-to-image conversion with high-resolution output (300 DPI) using PyMuPDF and pdf2image libraries
- Developed computer vision algorithms using OpenCV to automatically detect and extract relevant quadrilateral regions from document images
- Created a specialized prompt engineering system to guide AI models in extracting specific property sale information with high accuracy
- Built an intelligent numerical conversion system that transforms Indian financial notations (lac/crore) into standard numerical formats
- Integrated LangChain framework with Hugging Face models to create a flexible and powerful NLP pipeline

## Technologies Used:
- Languages & Frameworks: Python, LangChain, PyTorch
- AI/ML: Hugging Face Transformers, TinyLlama, Groq API integration
- Computer Vision: OpenCV, PyMuPDF, pdf2image
- Data Processing: Structured data extraction, Excel output formatting
- Environment Management: dotenv for configuration management

## Outcome:
The system successfully automated the extraction of critical property sale information from unstructured PDF notices, reducing manual data entry time by approximately 90%. The solution's ability to handle Indian numerical formats and extract structured data into standardized Excel format improved data accuracy and consistency. This automation enabled faster analysis of property auction information, supporting more informed decision-making processes while eliminating human error in data extraction.
