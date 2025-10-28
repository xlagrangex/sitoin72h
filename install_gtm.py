#!/usr/bin/env python3
"""
Script per installare Google Tag Manager (GTM-MZKFPFR8) su tutti i file HTML
"""

import os
import re
from pathlib import Path

# Codice GTM per l'head
GTM_HEAD_CODE = '''  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-MZKFPFR8');</script>
  <!-- End Google Tag Manager -->'''

# Codice GTM per il body (noscript)
GTM_BODY_CODE = '''  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MZKFPFR8"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->'''

def install_gtm_on_file(file_path):
    """Installa GTM su un singolo file HTML"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Controlla se GTM è già installato
    if 'GTM-MZKFPFR8' in content:
        print(f"  ✓ GTM already installed in {file_path}")
        return False
    
    # Installa GTM nell'head (dopo </head> o prima di altri script)
    head_pattern = r'(<meta[^>]*name="robots"[^>]*>)'
    if re.search(head_pattern, content):
        content = re.sub(
            head_pattern,
            r'\1\n\n' + GTM_HEAD_CODE + '\n',
            content,
            count=1
        )
    else:
        # Fallback: cerca </head>
        content = content.replace('</head>', GTM_HEAD_CODE + '\n</head>')
    
    # Installa GTM nel body (subito dopo <body)
    body_pattern = r'(<body[^>]*>)'
    if re.search(body_pattern, content):
        content = re.sub(
            body_pattern,
            r'\1\n' + GTM_BODY_CODE + '\n',
            content,
            count=1
        )
    
    # Salva il file modificato
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ GTM installed in {file_path}")
    return True

def main():
    """Installa GTM su tutti i file HTML"""
    html_files = [
        'about.html',
        'blog.html', 
        'contact.html',
        'detail_blog.html',
        'detail_works.html',
        'works.html',
        '401.html',
        '404.html',
        'template/style-guide.html',
        'template/licenses.html',
        'template/instructions.html',
        'template/changelog.html'
    ]
    
    modified_files = []
    
    for html_file in html_files:
        if os.path.exists(html_file):
            if install_gtm_on_file(html_file):
                modified_files.append(html_file)
        else:
            print(f"  ⚠ File not found: {html_file}")
    
    print(f"\n✅ Installation complete!")
    print(f"Modified files: {len(modified_files)}")
    for file in modified_files:
        print(f"  - {file}")

if __name__ == "__main__":
    main()
