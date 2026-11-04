# Harsha Vardhan Marothu — Digital Resume

Live: **https://harsha-marothu.streamlit.app**

A one-page digital resume built with Python and Streamlit. Visitors can read the resume, open the projects, and download a PDF copy. The PDF is generated on the fly and carries a QR code and link back to this site.

## Files

| File | What it does |
| --- | --- |
| `resume_data.py` | All resume content. Edit this one file to update both the website and the PDF. |
| `streamlit_app.py` | The website. |
| `resume_pdf.py` | Builds the PDF resume (ReportLab) with the QR code. |
| `.streamlit/config.toml` | Light theme and colours. |

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

To save the PDF without the website: `python resume_pdf.py`
