#app.py
import pybase64
import base64
import requests
import binascii
import os

# Define a fixed timeout for HTTP requests
TIMEOUT = 20  # seconds

# Define the fixed text for the initial configuration
fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs
"""

# Base64 decoding function
def decode_base64(encoded):
    decoded = ""
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            decoded = pybase64.b64decode(encoded + b"=" * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

# Function to decode base64-encoded links with a timeout
def decode_links(links):
    decoded_data = []
    for link in links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            encoded_bytes = response.content
            decoded_text = decode_base64(encoded_bytes)
            decoded_data.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_data

# Function to decode directory links with a timeout
def decode_dir_links(dir_links):
    decoded_dir_links = []
    for link in dir_links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            decoded_text = response.text
            decoded_dir_links.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_dir_links

# Filter function to select lines based on specified protocols
def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

# Create necessary directories if they don't exist
def ensure_directories_exist():
    output_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base64_folder = os.path.join(output_folder, "Base64")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(base64_folder):
        os.makedirs(base64_folder)

    return output_folder, base64_folder


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

        
# Main function to process links and write output files
def main():
    output_folder, base64_folder = ensure_directories_exist()  # Ensure directories are created

    protocols = ["vmess", "vless", "trojan", "ss", "ssr", "hy2", "tuic", "warp://"]
    links = [
        "https://fs.v2rayse.com/share/20240810/809druuxjx.txt",
        "https://mirror.v2gh.com/https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://mrpooyax.camdvr.org/api/ramezan/alpha.php?sub=1",
        "https://mrpooyax.camdvr.org/api/ramezan/lena.php?sub=1",
        "https://mrpooyax.camdvr.org/api/ramezan/run.php?sub=1",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
        "https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/sub",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix"
    ]
    telegram_urls = [
        "https://t.me/s/Awlix_ir",
        "https://t.me/s/Configforvpn01",
        "https://t.me/s/DailyV2RY",
        "https://t.me/s/DigiV2ray",
        "https://t.me/s/DirectVPN",
        "https://t.me/s/Easy_Free_VPN",
        "https://t.me/s/EliV2ray",
        "https://t.me/s/FOX_VPN66",
        "https://t.me/s/FreakConfig",
        "https://t.me/s/FreeNet1500",
        "https://t.me/s/FreeV2rays",
        "https://t.me/s/FreeVlessVpn",
        "https://t.me/s/God_CONFIG",
        "https://t.me/s/HTTPCustomLand",
        "https://t.me/s/MsV2ray",
        "https://t.me/s/Network_442",
        "https://t.me/s/OutlineVpnOfficial",
        "https://t.me/s/Outline_Vpn",
        "https://t.me/s/ParsRoute",
        "https://t.me/s/PrivateVPNs",
        "https://t.me/s/ServerNett",
        "https://t.me/s/ShadowSocks_s",
        "https://t.me/s/Shadowlinkserverr",
        "https://t.me/s/ShadowsocksM",
        "https://t.me/s/TUICity",
        "https://t.me/s/V2RAY_NEW",
        "https://t.me/s/V2RAY_VMESS_free",
        "https://t.me/s/V2RayOxygen",
        "https://t.me/s/V2Ray_FreedomIran",
        "https://t.me/s/V2pedia",
        "https://t.me/s/V2rayNG3",
        "https://t.me/s/V2rayNGvpni",
        "https://t.me/s/V2rayN_Free",
        "https://t.me/s/VPNCUSTOMIZE",
        "https://t.me/s/VPN_443",
        "https://t.me/s/ViPVpn_v2ray",
        "https://t.me/s/VlessConfig",
        "https://t.me/s/VmessProtocol",
        "https://t.me/s/VorTexIRN",
        "https://t.me/s/WeePeeN",
        "https://t.me/s/YtTe3la",
        "https://t.me/s/beiten",
        "https://t.me/s/beta_v2ray",
        "https://t.me/s/configV2rayForFree",
        "https://t.me/s/configV2rayNG",
        "https://t.me/s/config_v2ray",
        "https://t.me/s/custom_14",
        "https://t.me/s/forwardv2ray",
        "https://t.me/s/foxrayiran",
        "https://t.me/s/free4allVPN",
        "https://t.me/s/freeland8",
        "https://t.me/s/freev2rayssr",
        "https://t.me/s/frev2ray",
        "https://t.me/s/frev2rayng",
        "https://t.me/s/iSeqaro",
        "https://t.me/s/inikotesla",
        "https://t.me/s/iranvpnet",
        "https://t.me/s/mahsaamoon1",
        "https://t.me/s/napsternetv_config",
        "https://t.me/s/networknim",
        "https://t.me/s/proxystore11",
        "https://t.me/s/shadowsocksshop",
        "https://t.me/s/ultrasurf_12",
        "https://t.me/s/v2RayChannel",
        "https://t.me/s/v2_vmess",
        "https://t.me/s/v2line",
        "https://t.me/s/v2rayNG_Matsuri",
        "https://t.me/s/v2rayNG_VPN",
        "https://t.me/s/v2rayNG_VPNN",
        "https://t.me/s/v2ray_ar",
        "https://t.me/s/v2ray_configs_pool",
        "https://t.me/s/v2ray_custom",
        "https://t.me/s/v2ray_for_free",
        "https://t.me/s/v2ray_outlineir",
        "https://t.me/s/v2rayan",
        "https://t.me/s/v2rayn_server",
        "https://t.me/s/v2rayng_fa2",
        "https://t.me/s/v2rayng_org",
        "https://t.me/s/v2rayng_v",
        "https://t.me/s/vip_vpn_2022",
        "https://t.me/s/vmess_iran",
        "https://t.me/s/vmess_vless_v2rayng",
        "https://t.me/s/vmessiran",
        "https://t.me/s/vmessq",
        "https://t.me/s/vpn_ocean",
        "https://t.me/s/vpn_proxy_custom",
        "https://t.me/s/vpnmasi",
        "https://t.me/s/yaney_01",
    ]

    dir_links = [
        "https://mrpooya.top/api/Topfhwqqw.php",
        "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/All_Configs_Sub.txt",
        "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes",
        "https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/main/sub/Mix/mix.txt",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/sub",
        "https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/clashsub.txt",
        "https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/v2raysub.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/mix",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt",
        "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
        "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num",
        "https://raw.githubusercontent.com/yebekhe/ConfigCollector/main/sub/mix",
        "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
        "https://shadowmere.akiel.dev/api/b64sub",
        "https://sub.pmsub.me/base64",
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)

    combined_data = decoded_links + decoded_dir_links
    merged_configs = filter_for_protocols(combined_data, protocols)

    # Clean existing output files
    output_filename = os.path.join(output_folder, "All_Configs_Sub.txt")
    filename1 = os.path.join(output_folder, "All_Configs_base64_Sub.txt")
    
    if os.path.exists(output_filename):
        os.remove(output_filename)
    if os.path.exists(filename1):
        os.remove(filename1)

    for i in range(20):
        filename = os.path.join(output_folder, f"Sub{i}.txt")
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f"Sub{i}_base64.txt")
        if os.path.exists(filename1):
            os.remove(filename1)

    # Write merged configs to output file
    with open(output_filename, "w" ,encoding="utf-8") as f:
        f.write(fixed_text)
        for config in merged_configs:
            f.write(config + "\n")

    for url in telegram_urls:
        v2ray_configs = get_v2ray_links(url)
        if v2ray_configs:
            #//all_v2ray_configs.extend(v2ray_configs)
            with open(output_filename, "a", encoding="utf-8") as f:
                f.write(fixed_text)
                for config in v2ray_configs:
                    f.write(config + "\n")

    # Split merged configs into smaller files (no more than 600 configs per file)
    with open(output_filename, "r",encoding="utf-8") as f:
        lines = f.readlines()

    num_lines = len(lines)
    max_lines_per_file = 600
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file

    for i in range(num_files):
        profile_title = f"🆓 Git:Barry-far | Sub{i+1} 🫂"
        encoded_title = base64.b64encode(profile_title.encode()).decode()
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-Configs
#profile-web-page-url: https://github.com/barry-far/V2ray-Configs
"""

        input_filename = os.path.join(output_folder, f"Sub{i + 1}.txt")
        with open(input_filename, "w",encoding="utf-8") as f:
            f.write(custom_fixed_text)
            start_index = i * max_lines_per_file
            end_index = min((i + 1) * max_lines_per_file, num_lines)
            for line in lines[start_index:end_index]:
                f.write(line)

        with open(input_filename, "r",encoding="utf-8") as input_file:
            config_data = input_file.read()
        
        output_filename = os.path.join(base64_folder, f"Sub{i + 1}_base64.txt")
        with open(output_filename, "w",encoding="utf-8") as output_file:
            encoded_config = base64.b64encode(config_data.encode()).decode()
            output_file.write(encoded_config)

if __name__ == "__main__":
    main()
