"""All resume content lives here.

Edit this one file and both the website and the downloadable PDF update.
"""

# Public address of the digital resume (used by the QR code in the PDF).
RESUME_URL = "https://harsha-marothu.streamlit.app"
RESUME_URL_LABEL = "harsha-marothu.streamlit.app"

PDF_FILE_NAME = "Harsha_Vardhan_Marothu_Resume.pdf"

PROFILE = {
    "name": "Harsha Vardhan Marothu",
    "headline": "B.Tech Computer Science & Engineering (Final Year)",
    "tagline": "Python  ·  Machine Learning  ·  3D Technical Artist",
    "location": "Vizianagaram, Andhra Pradesh 535240, India",
    "phone": "+91 93984 96146",
    "phone_link": "tel:+919398496146",
    "email": "harshamarothu3d@gmail.com",
    "linkedin": "https://www.linkedin.com/in/harsha-marothu-87928333a",
    "linkedin_label": "linkedin.com/in/harsha-marothu-87928333a",
    "portfolio": "https://marothuharshavardhan.streamlit.app",
    "portfolio_label": "marothuharshavardhan.streamlit.app",
}

SUMMARY = (
    "Final-year B.Tech Computer Science and Engineering student with hands-on "
    "experience in Python, machine learning and web app deployment. Built a speech "
    "emotion recognition model with about 80% accuracy, deployed full Streamlit web "
    "apps, and spent three years automating 3D production work with Python as a "
    "freelance technical artist. Detail-oriented, quick to learn and a clear "
    "communicator, looking for a full-time role where I can apply analytical "
    "thinking, problem-solving and automation skills."
)

PROJECTS = [
    {
        "name": "Speech Emotion Recognition",
        "category": "Machine Learning",
        "url": "https://emotiondetectionmhv.streamlit.app",
        "url_label": "emotiondetectionmhv.streamlit.app",
        "source": "https://github.com/da25m512/DA6401W_Project",
        "description": (
            "A web app that detects the emotion in a voice recording. Upload a WAV "
            "clip and it predicts one of 8 emotions (such as happy, sad, angry or "
            "calm) with a confidence score."
        ),
        "detail": (
            "Trained a Keras neural network on Librosa audio features (MFCC, chroma, "
            "mel spectrogram) from the RAVDESS dataset, with data augmentation and "
            "class balancing, reaching about 80% test accuracy."
        ),
        "tech": ["Python", "TensorFlow / Keras", "scikit-learn", "Librosa", "Streamlit"],
    },
    {
        "name": "Personal Portfolio & Showreel Website",
        "category": "Web App",
        "url": "https://marothuharshavardhan.streamlit.app",
        "url_label": "marothuharshavardhan.streamlit.app",
        "source": "https://github.com/da25m512/harsha-vardhan-portfolio",
        "description": (
            "A responsive portfolio site that showcases my 3D work, films and "
            "showreel, built and deployed with Python and Streamlit."
        ),
        "detail": (
            "Includes a password-protected admin panel, so every text, image and "
            "video can be updated without touching code, with content saved to GitHub."
        ),
        "tech": ["Python", "Streamlit", "HTML", "CSS", "GitHub"],
    },
]

EXPERIENCE = [
    {
        "role": "Freelance 3D Technical Artist",
        "org": "Self-employed",
        "dates": "Oct 2023 – Oct 2026",
        "points": [
            "Wrote Python scripts to automate modeling, rendering and asset-pipeline "
            "tasks, making delivery faster and more consistent.",
            "Delivered 3D modeling, look-dev, lighting and animation for a feature film "
            "(in post-production), a music lyric video and a production intro.",
            "Worked across Blender, Unreal Engine, Nuke, After Effects and DaVinci "
            "Resolve, from concept to final render.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "B.Tech, Computer Science and Engineering",
        "school": "GIET Engineering College, Rajamahendravaram",
        "dates": "Sept 2023 – Present",
        "note": "Final year · Graduating 2027",
    },
    {
        "degree": "Intermediate Education",
        "school": "Sri Viswa Junior College",
        "dates": "Sept 2021 – Jun 2023",
        "note": "",
    },
]

SKILLS = [
    ("Programming", ["Python", "C"]),
    ("ML & Data", ["TensorFlow / Keras", "scikit-learn", "Librosa", "NumPy", "Pandas", "Matplotlib"]),
    ("Web & Tools", ["Streamlit", "HTML", "CSS", "Git & GitHub"]),
    ("3D & Media", ["Blender", "Unreal Engine", "Nuke", "After Effects", "Photoshop", "DaVinci Resolve"]),
    ("Soft Skills", ["Communication", "Teamwork", "Problem Solving", "Adaptability", "Time Management"]),
]

# level is 1–5 (used for the bars on the website)
LANGUAGES = [
    {"name": "Telugu", "level_text": "Native", "level": 5},
    {"name": "English", "level_text": "Professional", "level": 4},
    {"name": "Hindi", "level_text": "Elementary – can read and understand", "level": 2},
]
