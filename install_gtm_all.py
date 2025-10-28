#!/usr/bin/env python3
import os
import re

def install_gtm(file_path, gtm_id):
    """Installa Google Tag Manager in un file HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se GTM è già presente
    if gtm_id in content:
        print(f"GTM già presente in {file_path}")
        return
    
    # Script GTM per head
    gtm_head = f"""  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','{gtm_id}');</script>
  <!-- End Google Tag Manager -->"""
    
    # Noscript GTM per body
    gtm_noscript = f"""  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={gtm_id}"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->"""
    
    # Aggiungi script nel head (prima di </head>)
    if '</head>' in content:
        content = content.replace('</head>', f'{gtm_head}\n</head>')
    
    # Aggiungi noscript nel body (dopo <body>)
    if '<body' in content:
        # Trova il tag body e aggiungi dopo
        body_pattern = r'(<body[^>]*>)'
        content = re.sub(body_pattern, rf'\1\n{gtm_noscript}', content)
    
    # Scrivi il file modificato
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"GTM installato in {file_path}")

def main():
    gtm_id = 'GTM-MZKFPFR8'
    
    # Lista dei file HTML da processare
    html_files = [
        '401.html', '404.html', 'blog.html', 'contact.html', 
        'detail_blog.html', 'detail_works.html', 'works.html'
    ]
    
    for file_name in html_files:
        file_path = os.path.join(os.getcwd(), file_name)
        if os.path.exists(file_path):
            install_gtm(file_path, gtm_id)
        else:
            print(f"File non trovato: {file_path}")

if __name__ == "__main__":
    main()
