"""Site content: apps and UI strings (English + Italian).

Apps are listed newest first. To add an app: add an entry here, drop its
legal markdown in src/legal/<slug>/ and its icon in src/icons/<slug>.png,
then run `python3 src/build.py`.
"""

SITE_URL = "https://a-penna.github.io"
EMAIL = "alessandro_penna@icloud.com"
GITHUB = "https://github.com/a-penna"
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

DOC_LANGS = ["it", "en", "es", "fr", "de"]
LANG_NAMES = {"it": "Italiano", "en": "English", "es": "Español", "fr": "Français", "de": "Deutsch"}

APPS = [
    dict(
        slug="girostella", name="Girostella", year=2026,
        appstore="https://apps.apple.com/app/id6801086873",
        c1="#7c3aed", c2="#22d3ee",
        cat={"en": "Game · Arcade", "it": "Gioco · Arcade"},
        desc={
            "en": "A one-touch space arcade: leave orbit at the right moment and slingshot to the next planet, across 12 cosmic zones.",
            "it": "Un arcade spaziale a un tocco: lascia l'orbita al momento giusto e lanciati verso il pianeta successivo, attraverso 12 zone cosmiche.",
        },
        app_langs=DOC_LANGS,
    ),
    dict(
        slug="gplive", name="GPLive", year=2026,
        appstore="https://apps.apple.com/it/app/id6797024859",
        c1="#15803d", c2="#4ade80",
        cat={"en": "Navigation · Italy only", "it": "Navigazione · Solo Italia"},
        desc={
            "en": "LPG stations across Italy on a map: compare prices and start navigation in a tap.",
            "it": "I distributori GPL di tutta Italia su una mappa: confronta i prezzi e avvia la navigazione con un tocco.",
        },
        app_langs=["it"],
    ),
    dict(
        slug="siglume", name="SigLume", year=2026,
        appstore="https://apps.apple.com/app/id6784931753",
        c1="#b45309", c2="#fbbf24",
        cat={"en": "Productivity", "it": "Produttività"},
        desc={
            "en": "Capture your handwritten signature from a photo, clean it up and sign any PDF, all processed on your device.",
            "it": "Acquisisci la tua firma da una foto, ripuliscila e firma qualsiasi PDF, tutto elaborato sul dispositivo.",
        },
        app_langs=DOC_LANGS,
    ),
    dict(
        slug="swimetrics", name="Swimetrics", year=2026,
        appstore="https://apps.apple.com/app/id6761785509",
        c1="#0369a1", c2="#38bdf8",
        cat={"en": "Sports", "it": "Sport"},
        desc={
            "en": "Advanced swim tracking: distance, pace, SWOLF, stroke rate and long-term trends, with Apple Watch and Health.",
            "it": "Monitoraggio avanzato del nuoto: distanza, passo, SWOLF, frequenza di bracciata e andamento nel tempo, con Apple Watch e Salute.",
        },
        app_langs=DOC_LANGS,
    ),
    dict(
        slug="ironmeasure", name="IronMeasure", year=2026,
        appstore="https://apps.apple.com/app/id6755872551",
        c1="#b91c1c", c2="#f97316",
        cat={"en": "Health & Fitness", "it": "Salute e fitness"},
        desc={
            "en": "Track your body measurements over time and turn them into clear, structured progress.",
            "it": "Registra le misure del corpo nel tempo e trasformale in progressi chiari e strutturati.",
        },
        app_langs=DOC_LANGS,
    ),
    dict(
        slug="id-to-pdf", name="ID to PDF", year=2025,
        appstore="https://apps.apple.com/app/id6754233252",
        c1="#1d4ed8", c2="#818cf8",
        cat={"en": "Utilities", "it": "Utility"},
        desc={
            "en": "Scan both sides of your ID and get a clean, lightweight PDF in seconds.",
            "it": "Scansiona fronte e retro del documento e ottieni in pochi secondi un PDF chiaro e leggero.",
        },
        app_langs=DOC_LANGS,
    ),
]

T = {
    "en": dict(
        html_lang="en",
        title="Alessandro · iOS apps",
        meta_desc="iOS apps by Alessandro, a cybersecurity specialist who builds apps as a hobby: each app with its privacy policy, terms and support.",
        nav_apps="Apps", nav_about="Behind the apps", nav_contact="Contact", nav_home="Home",
        h1='Small apps for iPhone,<br><span class="g">made with care.</span>',
        lead="This is where I collect the iOS apps I've published, each with its privacy policy, terms and support. I'm Alessandro: I work in <b>cybersecurity</b> — my job and a passion of mine — and building apps is one of my hobbies.",
        cta_apps="Browse the apps", scroll="Scroll",
        whoami="— cybersecurity specialist · iOS developer for fun",
        launching="Launching {n} apps…",
        pf_eyebrow="Portfolio · {n} apps", pf_title="Things I've <em>shipped.</em>",
        privacy="Privacy Policy", terms="Terms", support="Support", appstore="App Store",
        iphone="iPhone",
        about_eyebrow="Behind the apps",
        facts=[
            ("A hobby, taken seriously", "Built in my spare time, alongside my job in cybersecurity — a field I'm passionate about, and a habit of care I bring to every app."),
            ("Native and localised", "Written in Swift and SwiftUI, designed for iPhone and translated into five languages."),
            ("A lean workflow", "I rely on AI to streamline production, so that a one-person side project can still reach a professional standard."),
            ("Always growing", "Each app teaches me something new, and I carry it into the next one: with every release I gain experience and build better products."),
        ],
        contact_eyebrow="Contact", contact_title="Got feedback or an <em>idea?</em>",
        contact_text="I read every message, and I'm happy to help with any of my apps.",
        contact_btn="Get in touch",
        footer_right="Made in Italy",
        # app page
        back="All apps", get_app="Download on the App Store",
        langs_label="Available in", free="Free",
        doc_privacy="Privacy Policy", doc_terms="Terms of Use",
        doc_lang="Language",
        eula_title="Terms of Use",
        eula_text="{name} is distributed under Apple's Standard Licensed Application End User License Agreement (EULA).",
        eula_link="Read the Apple Standard EULA",
        only_it="This document is available in Italian only, as the app is available in Italy only.",
        support_title="Need help with <em>{name}?</em>",
        support_text="Write me an email: I usually reply within 2–3 business days.",
        more_apps="More apps",
        notfound_title="Page not found", notfound_text="The page you're looking for doesn't exist or has moved.",
    ),
    "it": dict(
        html_lang="it",
        title="Alessandro · App iOS",
        meta_desc="Le app iOS di Alessandro, tecnico di cybersecurity che sviluppa app per hobby: per ogni app privacy policy, termini e supporto.",
        nav_apps="App", nav_about="Dietro le app", nav_contact="Contatti", nav_home="Home",
        h1='Piccole app per iPhone,<br><span class="g">fatte con cura.</span>',
        lead="Qui raccolgo le app iOS che ho pubblicato, ognuna con la sua privacy policy, i termini e il supporto. Sono Alessandro: lavoro nella <b>cybersecurity</b> — il mio mestiere e una mia passione — e sviluppare app è uno dei miei hobby.",
        cta_apps="Scopri le app", scroll="Scorri",
        whoami="— tecnico di cybersecurity · sviluppatore iOS per divertimento",
        launching="Avvio di {n} app…",
        pf_eyebrow="Portfolio · {n} app", pf_title="Le app che ho <em>pubblicato.</em>",
        privacy="Privacy Policy", terms="Termini", support="Supporto", appstore="App Store",
        iphone="iPhone",
        about_eyebrow="Dietro le app",
        facts=[
            ("Un hobby, preso sul serio", "Le sviluppo nel tempo libero, accanto al mio lavoro nella cybersecurity — un campo che mi appassiona e da cui porto in ogni app la stessa cura."),
            ("Native e tradotte", "Scritte in Swift e SwiftUI, pensate per iPhone e tradotte in cinque lingue."),
            ("Un processo snello", "Mi affido all'AI per ottimizzare la produzione, così anche un progetto portato avanti da solo può raggiungere uno standard professionale."),
            ("Sempre in crescita", "Ogni app mi insegna qualcosa che porto nella successiva: app dopo app accumulo esperienza e costruisco prodotti sempre migliori."),
        ],
        contact_eyebrow="Contatti", contact_title="Hai un feedback o un'<em>idea?</em>",
        contact_text="Leggo ogni messaggio e sono felice di aiutarti con qualsiasi mia app.",
        contact_btn="Scrivimi",
        footer_right="Made in Italy",
        back="Tutte le app", get_app="Scarica su App Store",
        langs_label="Disponibile in", free="Gratis",
        doc_privacy="Privacy Policy", doc_terms="Termini di utilizzo",
        doc_lang="Lingua",
        eula_title="Termini di utilizzo",
        eula_text="{name} è distribuita secondo il Contratto di licenza standard per l'utente finale (EULA) di Apple.",
        eula_link="Leggi l'EULA standard di Apple",
        only_it="Questo documento è disponibile solo in italiano, perché l'app è disponibile solo in Italia.",
        support_title="Ti serve aiuto con <em>{name}?</em>",
        support_text="Scrivimi un'email: di solito rispondo entro 2–3 giorni lavorativi.",
        more_apps="Altre app",
        notfound_title="Pagina non trovata", notfound_text="La pagina che cerchi non esiste o è stata spostata.",
    ),
}
