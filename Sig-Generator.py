import webbrowser
from string import Template
import time
import os

def main():
    run = True

    while run:
        name = input("What is the name?\n")
        title = input("\nWhat is the job title?\n")
        office = input("\nWhat is the Office phone number?\n")
        fax = input("\nWhat is the Fax number?\n")
        email = input("\nWhat is the email address?\n")
        data = {"name":name,
                "title": title,
                "office": office,
                "fax": fax,
                "email": email}

        temp = Template("""

            <style>
            p.arial {
                font-size: 14.5px;
                font-family: Arial, Helvetica, sans-serif;
            }
            </style>
            <p class = "arial">
            <strong>$name</strong><br />
             $title <br />
             Office: $office <br />
             Fax: $fax<br />
            <a href="mailto:$email">$email</a><br />
             Visit us Online at <a href="http://www.treloaronline.com">www.treloaronline.com</a><br />
             <a href="https://www.linkedin.com/company/treloar-and-heisel-inc"><img src="http://treloaronline.com/graphics/li.png" alt="" width="26" height="21" /></a>
             <a href="https://www.facebook.com/TreloarHeisel/timeline"><img src="http://treloaronline.com/graphics/fb.png" alt="" width="26" height="21" /></a><br />
            <a href="http://www.treloaronline.com"><img src="http://treloaronline.com/graphics/th-email101215.jpg" alt="" width="207" height="124" /></a>
            <br /> Treloar &amp; Heisel, Treloar &amp; Heisel Wealth Management, and Treloar &amp; Heisel Risk Management are all divisions of Treloar &amp; Heisel, Inc.</p>
            """)

        file = open('signature.html','w')

        file.write(temp.substitute(data))
        file.close()

        webbrowser.open_new_tab('signature.html')
        time.sleep(5)
        os.remove('signature.html')
if __name__ == '__main__':
    main()