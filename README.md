# AI SEO Content Generator
## Overview
The AI SEO Content Generator is a Python-based Streamlit application that helps businesses craft detailed SEO strategies. The app generates tailored SEO reports by leveraging user inputs, including keyword research, pillar page ideas, website structure recommendations, audience questions, and blog drafts.

## Features
1. **Custom SEO Strategy Report:** Generates a foundational SEO strategy report based on business details.
2. **Keyword Research:** Identifies primary and secondary keywords relevant to the business niche.
3. **Pillar Page Ideas:** Provides pillar page ideas with associated subtopics for better content structuring.
4. **Audience Questions:** Lists questions the target audience might search for, categorized under key topics.
5. **Content Outlines and Drafts:** Creates structured outlines and drafts for blog posts based on the SEO strategy.
6. **Export Options:** Allows exporting results in CSV and Word document formats.

## Prerequisites
- Python 3.9+
- An OpenAI API key stored in a `.env` file with the variable `OPENAI_API_KEY`.

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-repo/ai-seo-content-generator.git
cd ai-seo-content-generator
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Set up the environment:

Create a .env file in the project root.
Add your OpenAI API key:
```OPENAI_API_KEY=your_openai_api_key```
4. Run the application:

```bash
streamlit run app.py
```

## How to Use
1. Open the app in your browser (Streamlit provides a local URL upon running).
2. Fill in the following business details:
    - Business Name
    - Business Description
    - Business Type
    - Niche
    - Target Audience
    - Features Page URL
    - Money Page URL
    - Keyword Focus
    - Topic
3. Click Generate SEO Strategy.
4. View the generated:
    - Foundation SEO Strategy
    - Keywords and Secondary Keywords
    - Pillar Page Ideas and Subtopics
    - Audience Questions
    - Content Outlines and Drafts
5. Export the results as CSV or Word documents.
    - For now, preferably the Word docs. The CSV truncates data.

## Templates Used
The app employs LangChain to format and process prompts for generating the following outputs:

- Foundation SEO strategy
- Keyword research
- Pillar page ideas
- Audience questions
- Blog post outlines and drafts

## Export Formats
- CSV: A structured CSV file containing all sections of the SEO strategy.
- Word Document: A well-formatted Word document with headings for each section.

## Troubleshooting
If you encounter errors:

- Verify the OpenAI API key in the .env file.
- Ensure all required Python dependencies are installed.
- Check for missing or invalid input fields in the Streamlit app.
## Future Enhancements
- Enable real-time refinement of sections and drafts.
- Add multi-language support for non-English SEO strategies.
- Incorporate advanced analytics for keyword ranking and competition analysis.
## License
MIT License. See the `LICENSE` file for details.