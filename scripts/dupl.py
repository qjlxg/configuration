import json

# Define the array of Telegram URLs
telegram_urls = [
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/mix",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt",
        "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
        "https://mrpooya.top/api/Topfhwqqw.php",
        "https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes",
        "https://sub.pmsub.me/base64",
        "https://shadowmere.akiel.dev/api/b64sub",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/All_Configs_Sub.txt",
        "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num",
    #    "https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml",
        "https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/v2raysub.txt",
        "https://raw.githubusercontent.com/WilliamStar007/ClashX-V2Ray-TopFreeProxy/main/combine/clashsub.txt",
        "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
        "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt",
        "https://raw.githubusercontent.com/yebekhe/ConfigCollector/main/sub/mix",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/sub",
        "https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/main/sub/Mix/mix.txt"
]


# Remove duplicates by converting the list to a set and back to a list
unique_telegram_urls = list(set(telegram_urls))

# Sort the URLs for better readability
unique_telegram_urls.sort()

# Write the unique URLs to a file
with open("unique_telegram_urls.txt", "w") as file:
    file.write("telegram_urls = [\n")
    for url in unique_telegram_urls:
        file.write(f'    "{url}",\n')
    file.write("]\n")

print("Unique URLs have been saved to 'unique_telegram_urls.txt'.")
