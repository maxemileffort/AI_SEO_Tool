import os
import streamlit as st
import re

def extract_single_hash_sections(text):
    # Regex to capture content between single instances of '#' characters
    title_pattern = r'(?<=^# )(.*?)(?:\n(?=(#|$)))'
    article_pattern = r'^# (.*?)(?=\n# )'
    titles = re.findall(title_pattern, text, flags=re.MULTILINE | re.DOTALL )
    articles = re.findall(article_pattern, text, flags=re.MULTILINE | re.DOTALL )
    data = zip(["# " + match[0].strip() for match in titles], ["# " + match.strip() for match in articles])
    # Join captured groups into sections for display
    return data

# Function to save articles as text files
def save_articles(articles):
    print("saving articles")
    os.makedirs("articles", exist_ok=True)
    for i, (title, content) in enumerate(articles):
        print(title)
        safe_title = title.strip().replace(' ', '_').replace('/', '_')
        safe_title = safe_title.strip().replace(':', '_')
        filename = f"{safe_title}_{i}.txt"  # Added index to prevent clashes
        filepath = os.path.join("articles", filename)
        try:
            with open(filepath, "w", encoding='utf-8') as file:
                file.write(content.strip())
        except Exception as e:
            st.error(f"Error saving {filename}: {str(e)}")

st.title("Extract Sections Between Single '#' Characters")

# Text area for user input
input_text = st.text_area("Paste your text here:", height=300)

# Submit button
if st.button("Process Text"):
    st.warning('Starting process.')
    if input_text:
        # Process the text and extract sections
        extracted_sections = extract_single_hash_sections(input_text + '\n# ')
        extracted_sections = list(extracted_sections)
        if extracted_sections:
            st.subheader("Extracted Sections:")
            for d in extracted_sections:
                title = d[0]
                article = d[1]
                st.code(title)
                st.write(article)
                st.write("===============")
            # Save articles and generate download links
            # os.makedirs("articles", exist_ok=True)
        
        else:
            st.warning("No sections found with the specified pattern.")
        save_articles(extracted_sections)
        st.warning('Finished process.')
    else:
        st.error("Please paste some text into the text area.")