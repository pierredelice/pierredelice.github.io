"""
Single source of truth for pierredelice.github.io.

Edit the values below, then run:  python3 build.py
That regenerates index.html. No other files need editing for content changes.
"""

PROFILE = {
    "name": "Pierre Antoine Delice",
    "role": "AI Engineer & NLP Researcher · Data Scientist",
    "affiliation": "Ph.D. in Language & Knowledge Engineering",
    "location": "Tlajomulco de Zúñiga, Jalisco, Mexico",
    "location_short": "Jalisco, Mexico",
    "languages": "Spanish · English · French",
    "cvu": "262588",
    "email": "padelice@gmail.com",
    "linkedin": "https://www.linkedin.com/in/padelice",
    "orcid": "0000-0002-4170-4405",
    # Set to your Google Scholar profile URL, or None to hide the icon.
    "scholar": "https://scholar.google.com/citations?user=h5I0WeEAAAAJ&hl=en",
    "github": "https://github.com/pierredelice",
    "cv_pdf": "assets/cv/Pierre_Antoine_Delice_CV.pdf",
    # Source photo (processed into assets/img/profile.jpg by build.py).
    "photo_source": "/Users/pierredelice/Library/CloudStorage/Dropbox/Delice, Pierre.jpg",
}

ABOUT = [
    "I am an AI engineer, NLP researcher, and data scientist with a Ph.D. in "
    "Language and Knowledge Engineering and more than 15 years of experience applying "
    "statistical modeling, machine learning, administrative data, and evidence systems "
    "to public, economic, health, and education-sector decisions.",
    "My recent work focuses on <strong>LLM evaluation and prompting</strong>, "
    "<strong>conversational AI</strong>, <strong>Spanish-language NLP</strong>, "
    "transformer-based domain adaptation, economic news analytics, information retrieval, "
    "and record linkage. I am comfortable moving between research prototypes, "
    "production-oriented data products, teaching, and senior stakeholder advisory roles.",
]

FOUNDATIONS = [
    "Ph.D. in Language and Knowledge Engineering / Computer Science",
    "15+ years applying statistical modeling, machine learning, and evidence systems",
    "Work spanning AI, NLP, data science, public policy, health, education, and economics",
    "Professional communication in Spanish, English, and French",
]

RESEARCH_INTERESTS = [
    "Large language models & prompt engineering",
    "LLM evaluation",
    "Spanish-language NLP",
    "Retrieval-augmented generation (RAG)",
    "Knowledge graphs & ontologies",
    "Record linkage & entity resolution",
    "Economic news analytics",
    "Conversational AI for education",
]

EDUCATION = [
    {
        "degree": "Ph.D., Language and Knowledge Engineering / Computer Science",
        "institution": "Benemérita Universidad Autónoma de Puebla (BUAP)",
        "year": "2025",
    },
    {
        "degree": "M.Sc., Government and Public Affairs",
        "institution": "FLACSO México",
        "year": "2010",
    },
    {
        "degree": "B.A., Economics (Planning Specialization)",
        "institution": "CTPEA, Haiti",
        "year": "2006",
    },
]

SKILL_GROUPS = [
    {"label": "Programming", "items": ["Python", "R", "SQL"]},
    {"label": "AI / NLP", "items": [
        "Large language models", "Prompt engineering", "LLM evaluation", "NLP", "RAG",
        "Embeddings", "Transformers", "Sentiment analysis", "Information retrieval",
        "Deep learning", "Fuzzy models",
    ]},
    {"label": "Data Science", "items": [
        "Statistical modeling", "Survey design", "Record linkage", "Entity resolution",
        "Administrative data", "Economic indicators", "Costing analysis", "Dashboards",
        "Geospatial viz", "M&E",
    ]},
    {"label": "Cloud / Data Engineering", "items": [
        "ETL / ELT", "Microsoft Fabric", "Azure Data Lake", "Databricks",
        "Spark / Spark SQL", "Delta Lake", "dbt", "Docker", "Postgres", "Kafka",
    ]},
    {"label": "Semantic AI / Knowledge Eng.", "items": [
        "Vector databases", "Knowledge graphs", "Ontology modeling", "Semantic indexing",
        "RAG architecture", "Document retrieval",
    ]},
    {"label": "Domains", "items": [
        "Conversational AI for education", "Economic news analytics", "Public health data",
        "Security analytics", "Poverty measurement", "Policy analysis",
    ]},
]

EXPERIENCE = [
    {
        "role": "AI Engineer",
        "dates": "Feb 2025 – Present",
        "org": "Laureate International Universities (via Northware)",
        "loc": "Mexico",
        "bullets": [
            "Developed a conversational AI system for students and prospects across UNITEC and UVM.",
            "Built and improved a WhatsApp registration and enrollment workflow with payment support, "
            "so the chatbot operates closer to a human enrollment adviser.",
            "Analyze and adapt LLM behavior through prompt design, instruction testing, and qualitative response evaluation.",
            "Built ETL and RAG pipelines over documents for prompt evaluation using Python, OpenAI/Ollama tooling, Flask, and MongoDB.",
        ],
    },
    {
        "role": "Adjunct Professor (Profesor Cátedra)",
        "dates": "Aug 2025 – Present",
        "org": "Universidad de Guadalajara",
        "loc": "Jalisco, Mexico",
        "bullets": [
            "Teach undergraduate courses in applied programming, Programming II, applied mathematics, and sustainable projects.",
            "Design applied learning materials connecting programming, data analysis, mathematics, and engineering practice.",
        ],
    },
    {
        "role": "Data Analyst",
        "dates": "Apr 2023 – Dec 2024",
        "org": "National Council of Science and Technology (CONAHCYT)",
        "loc": "Mexico",
        "bullets": [
            "Designed and coordinated the National Survey for Mental Health and Addictions (ENASAMA 2023–2024).",
            "Supported statistical design, data organization, and evidence generation for national research and policy analysis.",
            "Converted research and policy questions into measurable indicators, KPI definitions, and validation criteria with stakeholders.",
        ],
    },
    {
        "role": "Data Analyst / Costing Consultant",
        "dates": "Jun 2023 – Jan 2024",
        "org": "Catholic Relief Services (CRS)",
        "loc": "Mexico",
        "bullets": [
            "Conducted costing analysis for the Grupo de Apoyo a Mujeres program using unstructured datasets from multiple sources.",
            "Produced a costing exercise to support program planning, monitoring, and resource-allocation decisions.",
            "Validated source data, assumptions, and reconciliation rules to improve reliability of cost estimates.",
        ],
    },
    {
        "role": "Technical Advisor & Data Consultant",
        "dates": "2016 – 2023",
        "org": "PAHO · Guerrero Ministry of Health · UNODC · CONEVAL",
        "loc": "Mexico",
        "bullets": [
            "Developed monitoring and evaluation work for community COVID-19 mitigation with the Pan American Health Organization.",
            "Produced diagnostics of violence in Guerrero using survey data and structured interviews, contributing to public-security strategy design.",
            "Designed and implemented the Forensic Medicine Specialty program in Guerrero, including academic standards and accreditation follow-up.",
            "Designed a proposal for a state-level monitoring and evaluation system for CONEVAL.",
        ],
    },
    {
        "role": "Senior Data & Policy Roles",
        "dates": "2008 – 2016",
        "org": "Health, economic development, HIV/AIDS, and planning institutions",
        "loc": "Mexico / Haiti",
        "bullets": [
            "Managed and analyzed national vital statistics datasets for epidemiological surveillance and public policy.",
            "Built dashboards, data models, and statistical analyses for hospital performance and resource allocation.",
            "Developed composite indexes and geospatial visualizations for Mexico City competitiveness and urban policy.",
            "Produced HIV/AIDS prevalence and incidence estimates; conducted cost analysis for Haiti's Poverty Reduction Strategy Paper.",
        ],
    },
]

PROJECTS = [
    {"title": "ML4H ICD-10 Mortality Coding",
     "text": "Leakage-safe Spanish clinical NLP for ICD-10 underlying-cause coding from death-certificate free text, using hierarchy-aware models and candidate reranking to support garbage-code triage in Mexican mortality data.",
     "tags": ["ML4H", "Clinical NLP", "ICD-10", "Health Data"]},
    {"title": "Economic News NLP",
     "text": "Spanish-language economic news as signals for economic analysis and inflation dynamics.",
     "tags": ["NLP", "Economics", "Research"]},
    {"title": "Conversational AI",
     "text": "Education-sector chatbot workflows for student advising, registration, and payments over WhatsApp.",
     "tags": ["LLM", "Chatbot", "Education"]},
    {"title": "LLM Ranking",
     "text": "Listwise LLM ranking for multimodal Spanish political headline classification (2026).",
     "tags": ["LLM", "Ranking", "NLP"]},
]

# doi may be None
PUBLICATIONS = [
    {"cite": "Delice, P. A. & Pinto, D. (2025). “Decoding Economic Insights: The Analytical Power of "
             "News Content.” Journal of Scientometric Research, 14(1), 365–372.",
     "doi": "10.5530/jscires.20251459"},
    {"cite": "Delice, P. A., Pinto, D., García-Guerrero, V. M., & Hernández-López, S. (2024). "
             "“The Economic Value of Words: An Evaluation of News for Economic Analysis.” "
             "IEEE Latin American Electron Devices Conference (LAEDC).",
     "doi": "10.1109/LAEDC61552.2024.10555884"},
    {"cite": "Téllez-Velázquez, A., Delice, P. A., Salgado-Leyva, R., & Cruz-Barbosa, R. (2024). "
             "“On the Explanation of COVID-19 Blood Test Variables Using Fuzzy Models.” "
             "Journal of Intelligent & Fuzzy Systems.",
     "doi": "10.3233/JIFS-219372"},
    {"cite": "Morales-Murillo, V. G., Gómez-Adorno, H., Pinto, D., Cortés-Miranda, I. A., & Delice, P. (2023). "
             "“LKE-IIMAS Team at Rest-Mex 2023: Sentiment Analysis on Mexican Tourism Reviews Using "
             "Transformer-Based Domain Adaptation.” IberLEF 2023.",
     "doi": None},
    {"cite": "Delice, P. A. (2026). “LKE-BUAP at PoliticHeadlines-IberLEF 2026: Listwise LLM Ranking for "
             "Multimodal Spanish Political Headline Classification.” CEUR Workshop Proceedings.",
     "doi": None},
    {"cite": "Delice, P. A. (2026). “IA y empoderamiento económico: lecciones desde proyectos comunitarios.” "
             "Accepted book chapter, UPAEP.",
     "doi": None},
]

HONORS = [
    "IEEE Senior Member, 2025.",
    "Publications Chair, IEEE Latin American Electron Devices Conference (LAEDC), 2025.",
    "Presented economic-news NLP research at LKE 2024, IEEE LAEDC 2024, CIBERTIC 2025, and IEEE IAS Electrical Safety Workshop 2025.",
    "CLACSO Research Grant, 2021; CLACSO Young Researchers Grant, 2012.",
    "Mexico–Chile Bilateral Fund / AMEXCID award for forensic-science training, 2020.",
    "Evaluator, Vive la Ciencia 2024 technical review committee, CONCYTEP.",
]

TRAINING = [
    "Deep Learning Course, Neuromatch Academy — 128 hours, 2023.",
    "Multidimensional Poverty Measurement and Applications, ECLAC / OPHI / MIDEPLAN, 2010.",
]

CONTACT_INTRO = (
    "Open to collaboration on applied AI, NLP research, and data science for the "
    "public and social sectors."
)
