import requests
from bs4 import BeautifulSoup

def get_v2ray_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        divs = soup.find_all('div', class_='tgme_widget_message_text')
        divs2 = soup.find_all('div', class_='tgme_widget_message_text js-message_text before_footer')
        spans = soup.find_all('span', class_='tgme_widget_message_text')
        codes = soup.find_all('code')
        span = soup.find_all('span')
        main = soup.find_all('div')
        
        all_tags = divs + spans + codes + divs2 + span + main

        v2ray_configs = []
        for tag in all_tags:
            text = tag.get_text()
            if text.startswith('vless://') or text.startswith('ss://') or text.startswith('trojan://') or text.startswith('tuic://'):
                v2ray_configs.append(text)

        return v2ray_configs
    else:
        print(f"Failed to fetch URL (Status Code: {response.status_code})")
        return None

def main():
    telegram_urls = [
        "https://t.me/s/v2ray_configs_pool",

    ]

    output_filename = "output.txt"
    fixed_text = "Your fixed text here\n"  # Define fixed_text as needed

    for url in telegram_urls:
        v2ray_configs = get_v2ray_links(url)
        if v2ray_configs:
            with open(output_filename, "a", encoding="utf-8") as f:
                f.write(f"Data from: {url}\n")  # Write fixed_text if necessary
                for config in v2ray_configs:
                    f.write(config + "\n")

if __name__ == "__main__":
    main()
