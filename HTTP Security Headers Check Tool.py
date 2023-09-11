#!/usr/bin/env python3

import requests
import argparse
from urllib.parse import urlparse
import ipaddress
from colorama import init, Fore, Back, Style
import time

print(""" 
 __    __  .___________..___________..______           _______. _______   ______  __    __  .______       __  .___________.____    ____     __    __   _______      ___       _______   _______ .______           _______.
|  |  |  | |           ||           ||   _  \         /       ||   ____| /      ||  |  |  | |   _  \     |  | |           |\   \  /   /    |  |  |  | |   ____|    /   \     |       \ |   ____||   _  \         /       |
|  |__|  | `---|  |----``---|  |----`|  |_)  |       |   (----`|  |__   |  ,----'|  |  |  | |  |_)  |    |  | `---|  |----` \   \/   /     |  |__|  | |  |__      /  ^  \    |  .--.  ||  |__   |  |_)  |       |   (----`
|   __   |     |  |         |  |     |   ___/         \   \    |   __|  |  |     |  |  |  | |      /     |  |     |  |       \_    _/      |   __   | |   __|    /  /_\  \   |  |  |  ||   __|  |      /         \   \    
|  |  |  |     |  |         |  |     |  |         .----)   |   |  |____ |  `----.|  `--'  | |  |\  \----.|  |     |  |         |  |        |  |  |  | |  |____  /  _____  \  |  '--'  ||  |____ |  |\  \----..----)   |   
|__|  |__|     |__|         |__|     | _|         |_______/    |_______| \______| \______/  | _| `._____||__|     |__|         |__|        |__|  |__| |_______|/__/     \__\ |_______/ |_______|| _| `._____||_______/    
                                                                                                                                                                                                                          
                                                                                                                                                                                    Developed by Morph1ne  """)

default_headers = [
                    # Defaul HTTP Security Headers
                    "X-Content-Type-Options",
                    "X-Frame-Options",
                    "Content-Security-Policy",
                    "Strict-Transport-Security",
                    "X-XSS-Protection",
                    "Referrer-Policy",
                    "Feature-Policy",
                    "Content-Security-Policy-Report-Only",
                    "Cache-Control",
                    "Clear-Site-Data",
                    "X-Permitted-Cross-Domain-Policies",
                    "Expect-CT",
                    "Public-Key-Pins",
                    "X-Content-Security-Policy",
                    "X-Download-Options" ,
                    "X-DNS-Prefetch-Control",
                    "X-Robots-Tag" ,
                    "X-Request-ID"    ,
                    "X-UA-Compatible",
                    # Diğer default başlıkları buraya ekleyebilirsiniz.
                ]

def show_help(): # Rehber Sayfası
    print("""
          HTTP güvenlik başlıkları (HTTP Security Headers), web uygulamalarının ve sitelerin daha güvenli olmasına yardımcı olan özel HTTP başlıklarıdır. 
          Bu başlıklar, web tarayıcılarına ve istemcilere belirli güvenlik önlemlerini uygulamaları konusunda talimatlar verir.
    
          Bu başlıklar, web uygulamalarının ve sitelerin güvenliğini artırmak ve yaygın güvenlik açıklarını azaltmak için kullanılır. 
          Her başlık belirli bir güvenlik tehdidine karşı koruma sağlar ve doğru bir şekilde yapılandırılmaları önemlidir. 
          Bu başlıkları kullanarak, saldırılara karşı daha iyi korunan ve kullanıcı gizliliğini daha iyi sağlayan web uygulamaları geliştirebilirsiniz.
          
          Tool basit ve hızlı bir kullanıma sahiptir. 
          Tool, Genel Amacı HTTP Güvenlik Başlıklarını Taraması ve Eksik olan başlıklar hakkında bilgi vermesidir.
          
          Kullanım Talimatları:
            (1) Siteye attığı request atar ve dönen response ile gelen Başlıkları ayıklar. 
            Burada ki ilk amaç site içerisinde var olan HTTP başlıklarını görmektir.
            Daha sonra bu HTTP Başlıklarına bir index değeri atamaktadır.
            (1) ÖRNEK KULLANIM : www.example.com
                ÖRNEK KULLANIM : 192.168.1.1
            Kullanıcı index atanan HTTP Başlıkları hakkında bilgi almak isterse;
            (2)'de bulunan Seçilen HTTP başlıklarını kontrol et seçeneğini seçebilir.
                ÖRNEK KULLANIM : Domain yada IP adresi giriniz: www.example.com
                                 Taratmak istediğiniz headersların 1,2,3,4,5,9
            (3) Belirli Bir HTTP Başlığını kontrol etmek istiyorsanız.
                ÖRNEK KULLANIM : Domain yada IP adresi giriniz: www.example.com
                                 Taratılacak Headers : X-XSS-Protection
            Dikkat!! Headers ismi düzgün yazılmalıdır. Büyük Küçük harf duyarlıdır. Hata verir.
            (4) IP veya Domain adresi girdikten sonra Tool kendisinde olan Default HTTP Security Başlıklarını Tarar
                ÖRNEK KULLANIM : Domain yada IP adresi giriniz: 192.168.1.1
                                 Domain yada IP adresi giriniz: www.example.com
          
            Default HTTP Security Headers:
            
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Feature-Policy",
            "Content-Security-Policy-Report-Only",
            "Cache-Control",
            "Clear-Site-Data",
            "X-Permitted-Cross-Domain-Policies",
            "Expect-CT",
            "Public-Key-Pins",
            "X-Content-Security-Policy",
            "X-Download-Options" ,
            "X-DNS-Prefetch-Control",
            "X-Robots-Tag" ,
            "X-Request-ID"    ,
            "X-UA-Compatible",  
          
          
""")

def explain_header(header_name): # Bilgilendirme Blokları
    if header_name == "X-XSS-Protection":
        print(Style.RESET_ALL + """
        X-XSS-Protection Başlığı Hakkında Bilgi:
        X-XSS-Protection başlığı, tarayıcılara XSS (Cross-Site Scripting) saldırılarına karşı koruma sağlar.
        Bu başlık, tarayıcılara, kullanıcı tarafından yürütülebilecek potansiyel olarak zararlı kodların
        engellenmesi gerektiğini belirtir. Özellikle tarayıcıların bu tür saldırılara karşı filtrelerini
        etkinleştirmesini sağlar."
        
        Eğer X-XSS-Protection başlığı boş görünüyorsa veya yanlış yapılandırılmışsa,
        bu bir güvenlik açığına yol açabilir. Bu durumda yapılması gerekenler:
        1. Sunucu yapılandırmasını kontrol edin ve X-XSS-Protection başlığını uygun bir şekilde ayarlayın.
        2. Tarayıcı tarafından sağlanan XSS filtrelerini etkinleştirin.
        3. Kullanıcı girdilerini güvenli bir şekilde işlemek için kodunuzu gözden geçirin ve filtreleyin.
        4. OWASP gibi güvenlik kaynaklarından XSS saldırılarına karşı en iyi uygulamaları öğrenin.
        5. Düzenli güncellemeler ve güvenlik testleri yaparak site güvenliğini sürekli olarak izleyin.""")

    elif header_name == "X-Content-Type-Options":
        print(Style.RESET_ALL + """
        X-Content-Type-Options Başlığı Hakkında Bilgi:
        X-Content-Type-Options başlığı, sunucu tarafından belirlenen MIME türünün
        değiştirilmesini engeller. Bu başlığı kullanarak, tarayıcınızın MIME türünü
        kendi başına değiştirmesini engelleyebilirsiniz. Özellikle, bu başlık sayesinde
        tarayıcı, içerik türünün yanlışlıkla değiştirilmesini önler ve güvenlik açıklarını azaltır.
        Etkinleştirmek için sunucunuzun yanıtına 'X-Content-Type-Options: nosniff' eklemelisiniz.""")

    elif header_name == "X-Frame-Options":
        print(Style.RESET_ALL + """
        X-Frame-Options Başlığı Hakkında Bilgi:
        X-Frame-Options başlığı, sitenizin başka siteler içerisinde çerçevelenmesini engeller.
        Bu başlık, clickjacking gibi saldırılara karşı koruma sağlar. Clickjacking, kullanıcıların
        istenmeyen bir şekilde bir sayfada tıklamalarını tetikleyen gizli bir çerçeve kullanarak
        saldırganların kötü niyetli işlemleri gerçekleştirmesine olanak tanır. Bu başlığı etkinleştirmek
        için sunucunuzun yanıtına 'X-Frame-Options: DENY' eklemelisiniz.""")
        

    elif header_name == "Content-Security-Policy":
        print(Style.RESET_ALL + """
        Content-Security-Policy Başlığı Hakkında Bilgi:
        Content-Security-Policy başlığı, tarayıcıda hangi kaynakların yüklenebileceğini ve
        hangi eylemlerin yapılabileceğini tanımlar. Bu başlık, XSS (Cross-Site Scripting) gibi
        saldırılara karşı koruma sağlar. XSS, saldırganların kullanıcının tarayıcısında kötü niyetli
        kodları çalıştırmasına neden olan bir saldırı türüdür. Bu başlığı etkinleştirmek ve
        doğru şekilde yapılandırmak için sunucunuzun yanıtına bir politika eklemelisiniz.""")
        

    elif header_name == "Strict-Transport-Security":
        print(Style.RESET_ALL + """
        Strict-Transport-Security Başlığı Hakkında Bilgi:
        StTransport-Security başlığı, tarayıcının HTTPS üzerinden iletişim kurmasını zorunlu kılar.
        Bu, bağlantı güvenliği için önemlidir ve man-in-the-middle saldırılarına karşı koruma sağlar.
        Man-in-the-middle saldırıları, saldırganların iletişim trafiğini gözlemleyebildiği ve manipüle
        edebildiği saldırılardır. Bu başlığı etkinleştirmek için sunucunuzun yanıtına 'Strict-Transport-Security'
        başlığı eklemelisiniz ve bir süre belirtmelisiniz (örneğin, 'max-age=31536000' ile bir yıl süreyle.""")
        

    elif header_name == "Referrer-Policy":
        print(Style.RESET_ALL + """
        Referrer-Policy Başlığı Hakkında Bilgi:
        Referrer-Policy başlığı, tarayıcılara tarayıcıdan sunucuya referer (yönlendiren)
        bilgisini hangi durumlarda göndereceğini söyler. Bu başlık, gizlilik ve güvenlik açısından
        önemlidir. Saldırganlar, referer bilgisi üzerinden kullanıcıların izini sürebilir veya
        gizli bilgilere erişebilirler.
        
        Bu başlıkla, referer bilgisi davranışını belirleyebilirsiniz. Örneğin, 'no-referrer' kullanarak
        hiçbir referer bilgisi gönderilmemesini sağlayabilirsiniz. Bu başlıkla oynarken dikkatli olmalı
        ve güvenliğinizi ve gizliliğinizi korumak için en iyi uygulamaları takip etmelisiniz.""")
        
    elif header_name == "Feature-Policy":
        print(Style.RESET_ALL + """
        Feature-Policy Başlığı Hakkında Bilgi:
        Feature-Policy başlığı, web sayfanızın belirli özelliklere (örneğin kamera, mikrofon, konum)
        erişim iznini kontrol eder. Bu başlık, kötü amaçlı kullanımları önlemek ve kullanıcı
        gizliliğini korumak için önemlidir

        Bu başlıkla, hangi özelliklere erişime izin verileceğini ve hangi durumlarda izin verilmeyeceğini
        belirleyebilirsiniz. Örneğin, 'geolocation none' kullanarak konum bilgisine erişime izin verilmemesini
        sağlayabilirsiniz. Feature-Policy: camera 'none'; microphone 'self'" gibi bir politika ile erişimi belirleyebilirsiniz.
        Bu başlığı kullanırken, güvenlik politikalarınıza dikkat etmelisiniz.   """)
        
    elif header_name == "Content-Security-Policy-Report-Only":
        print(Style.RESET_ALL + """
        Content-Security-Policy-Report-Only Başlığı Hakkında Bilgi:
        Content-Security-Policy-Report-Only başlığı, Content-Security-Policy (CSP) politikasının
        bir uygulama üzerindeki etkilerini raporlamak için kullanılır, ancak tarayıcının politikayı
        uygulamamasına izin verir. Bu, bir politika yapılandırması test edilirken veya geliştirilirken
        faydalı olabilir.
        
        Bu başlıkla, CSP politikasını aktif hale getirmeden önce politikanın olası etkilerini inceleyebilir
        ve hataları düzeltebilirsiniz. Bu şekilde, kullanıcı deneyimini olumsuz etkilemeden güvenlik.
        açıklarını tespit edebilirsiniz.""")

    elif header_name == "Cache-Control":  
        print(Style.RESET_ALL + """
        Cache-Control Başlığı Hakkında Bilgi:        
        Sayfanın önbelleğe alma davranışını kontrol eder.
        "no-cache", "no-store", "public", "private" gibi değerlerle kullanılır. 
        Önbellek davranışını tanımlamak için kullanılır.""")
    
    elif header_name == "Clear-Site-Data":
        print(Style.RESET_ALL + """
        Clear-Site-Data Başlığı Hakkında Bilgi:
        Tarayıcının önbellek ve veri silme davranışını kontrol eder.
        "cache", "cookies", "storage", "executionContexts" gibi değerlerle kullanılır. 
        Site verilerini temizlemek için kullanılır.""")
    
    elif header_name == "X-Permitted-Cross-Domain-Policies":
        print(Style.RESET_ALL + """
        X-Permitted-Cross-Domain-Policies Başlığı Hakkında Bilgi:
        İçeriğin farklı alan adlarına gömülmesini kontrol eder.
        "none", "master-only", "by-content-type", "all" gibi değerlerle kullanılır. 
        Erişim izinlerini tanımlamak için kullanılır.""")
    
    elif header_name == "Expect-CT":
        print(Style.RESET_ALL + """
        Expect-CT Başlığı Hakkında Bilgi:
        Sertifikat şeffaflığı (Certificate Transparency) politikalarını kontrol eder.
        "enforce", "report-only", "max-age" gibi değerlerle kullanılır. 
        CT politikalarını uygulamak veya test etmek için kullanılır.""")

    elif header_name =="Public-Key-Pins":
        print(Style.RESET_ALL + """
        Public-Key-Pins Başlığı Hakkında Bilgi:
        Tarayıcıda belirtilen sunucu sertifikalarının kullanılmasını zorunlu kılar.
        "pin-sha256", "pin-sha256", "max-age", "includeSubDomains" gibi değerlerle kullanılır. 
        Sertifika güvenliğini artırmak için kullanılır.""")
    
    elif header_name == "X-Content-Security-Policy":
        print(Style.RESET_ALL + """
        X-Content-Security-Policy Başlığı Hakkında Bilgi:
        Content-Security-Policy ile aynı işlevi görür ancak eski tarayıcılarda kullanılır.
        Content-Security-Policy ile aynı şekilde kullanılır, ancak eski tarayıcılarda desteklenir.    """)
        
    elif header_name == "X-Download-Options":
        print(Style.RESET_ALL + """
        X-Download-Options Başlığı Hakkında Bilgi:
        Tarayıcıda potansiyel olarak zararlı içeriklerin indirilmesini kontrol eder.
        "noopen" ve "nosniff" gibi değerlerle kullanılır. 
        Zararlı içerikleri engellemek için kullanılır.   """)
    
    elif header_name == "X-DNS-Prefetch-Control":
        print(Style.RESET_ALL + """
        X-DNS-Prefetch-Control Başlığı Hakkında Bilgi:
        DNS tahminini kontrol eder.
        "on" ve "off" gibi değerlerle kullanılır. 
        Tarayıcının DNS tahmini davranışını kontrol etmek için kullanılır.""")
    
    elif header_name == "X-Robots-Tag":
        print(Style.RESET_ALL + """
        X-Robots-Tag Başlığı Hakkında Bilgi:
        Web tarayıcılarına ve arama motorlarına sayfanın dizinlenme ve taranma davranışını belirtir.
        "index", "noindex", "follow", "nofollow" gibi değerlerle kullanılır. 
        Arama motorlarının sayfayı nasıl işleyeceğini kontrol etmek için kullanılır.""")
    
    elif header_name == "X-Request-ID":
        print(Style.RESET_ALL + """
        X-Request-ID Başlığı Hakkında Bilgi:
        İsteklere benzersiz kimlikler ekler.
        Genellikle geliştirme ve hata ayıklama amaçları için kullanılır. 
        İstekleri izlemek ve tanımlamak için kullanılır.""")

    elif header_name == "X-UA-Compatible":
        print(Style.RESET_ALL + """
        X-UA-Compatible Başlığı Hakkında Bilgi:
        Tarayıcının hangi belge uyumluluğunu kullanması gerektiğini belirtir.
        "IE=edge", "IE=EmulateIE7" gibi değerlerle kullanılır. 
        Belge uyumluluğunu belirlemek için kullanılır.""")    


def get_domain(): # Seçenek 1
    while True:
        input_str = input(Style.RESET_ALL+ "IP adresi veya alan adı girin: "+ Fore.YELLOW)
        try:
            ip_address = ipaddress.ip_address(input_str) 
            domain = f"http://{input_str}"
        except ValueError:
            if not input_str.startswith("http://") and not input_str.startswith("https://"):
                domain = "https://" + input_str  
            else:
                domain = input_str
        try:
            response = requests.head(domain)
            time.sleep(5)
            all_headers = response.headers.keys()
            print(Fore.BLUE + "\nKullanılabilir HTTP Başlıkları:")
            for idx, header in enumerate(all_headers, start=1):
                print(Fore.LIGHTGREEN_EX + f"{idx}) {Fore.YELLOW + header}")
            break
        except requests.exceptions.RequestException:
            print(Fore.RED + "Geçersiz bir domain adresi girdiniz. Lütfen tekrar deneyin.")

def get_selected_indices(all_headers): # Seçenek 1 indexleme
    while True:
        selected_indices = input(Fore.GREEN + "Kontrol edilecek HTTP başlıklarının sıra numaralarını virgülle ayırarak girin: " + Fore.YELLOW)
        try:
            selected_indices = [int(idx) for idx in selected_indices.split(",")]
            if not all(1 <= idx <= len(all_headers) for idx in selected_indices):
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Geçersiz bir sıra numarası girdiniz. Lütfen doğru sıra numaralarını virgülle ayırarak girin.")
    return selected_indices            

def get_domain_index(): # Şeçenek 2
    while True:
        input_str = input(Style.RESET_ALL+ "IP adresi veya alan adı girin: "+ Fore.YELLOW)
        try:
            ip_address = ipaddress.ip_address(input_str)  
            domain = f"http://{input_str}"
        except ValueError:
            if not input_str.startswith("http://") and not input_str.startswith("https://"):
                domain = "https://" + input_str  
            else:
                domain = input_str
        try:
            response = requests.head(domain)
            time.sleep(5)
            all_headers = response.headers.keys()
            selected_indices = get_selected_indices(all_headers)
            selected_headers = []
            for idx, header in enumerate(all_headers, start=1):
                if idx in selected_indices:
                    selected_headers.append(header)
            if selected_headers:
                print(Fore.GREEN + "\nSeçilen HTTP Başlıkları:\n")
                header_list = list(all_headers)  
                for header_index in selected_indices:
                    if 1 <= header_index <= len(header_list):
                        header = header_list[header_index - 1]
                        response_header = response.headers.get(header)
                        print(Fore.GREEN + f"{header_index} {Style.RESET_ALL + header}: {Fore.YELLOW + response_header}")
                        if header not in default_headers:
                            continue
                    else:
                        print(f"{header_index}. başlık bulunamadı.")
            else:
                print("Seçilen başlık bulunamadı.")
            break
        except requests.exceptions.RequestException:
            print(Fore.RED + "Geçersiz bir domain adresi girdiniz. Lütfen tekrar deneyin.")


def single_scan(): # Seçenek 3
    input_str = input(Style.RESET_ALL+ "IP adresi veya alan adı girin (Çıkmak için exit yazınız.): "+ Fore.YELLOW)
    header_name = input(Style.RESET_ALL + "Enter the HTTP security header to check (Çıkmak için exit yazınız.): "+Fore.YELLOW)
    try:
        if not input_str.startswith("http://") and not input_str.startswith("https://"):
            domain = "http://" + input_str  
        else:
            ip_address = ipaddress.ip_address(input_str)  
            domain = f"http://{input_str}"
    except ValueError:
        if not input_str.startswith("http://") and not input_str.startswith("https://"):
            domain = "https://" + input_str  
        else:
            domain = input_str
    try:
        response = requests.head(domain)
        if header_name in response.headers:
            print(f"{header_name} header found: {response.headers[header_name]}")
        else:
            print(Fore.RED + f"{header_name}  header not found.")
            explain_header(header_name)
    except requests.exceptions.RequestException:
                print(Fore.RED + "Error: Invalid IP or domain address.")

def get_security_headers(): # Seçenek 4
    while True:
        input_str = input(Style.RESET_ALL+ "IP adresi veya alan adı girin: "+ Fore.YELLOW)
        try:
            ip_address = ipaddress.ip_address(input_str) 
            domain = f"http://{input_str}"
        except ValueError:
            if not input_str.startswith("http://") and not input_str.startswith("https://"):
                domain = "https://" + input_str  
            else:
                domain = input_str  
        try:
            response = requests.head(domain)
            print(Fore.LIGHTGREEN_EX +"\nBulunan HTTP Başlıklar:")
            for header, value in response.headers.items():
                if header in response.headers:
                    print(f"{Style.RESET_ALL + header}: {Fore.YELLOW + response.headers[header]}")
            print(Fore.BLUE + "\nDefault Olarak Taranan Bazı HTTP Security Başlıkları Bulunamadı:")   
            missing_headers = []
            for header in default_headers:
                if header in response.headers:
                    continue
                else:
                    missing_headers.append(header)
                    print(Fore.RED +f"\n{header} Not found.")
                    explain_header(header)
            if missing_headers:
                print(Fore.RED + "\nThe following headers are missing:")
                for header in missing_headers:
                    print(Fore.YELLOW + "(!) "+ Style.RESET_ALL + header)
                print(Fore.RED + "Please see the information for HTTP Security Headers that are not found.")
            break
        except requests.exceptions.RequestException:
            print(Fore.RED + "Geçersiz bir IP adresi veya alan adı girdiniz. Lütfen tekrar deneyin.")

 

def main():
    global default_headers
    while True:
        print(Style.RESET_ALL + """
        HTTP Security Headers Analiz Aracı
              
        1. Kullanılabilir HTTP Başlıklarını Listele
        2. Seçilen HTTP Başlıklarını Kontrol Et
        3. Belirli Bir HTTP Başlığını Kontrol Et
        4. IP veya Alan Adı ile Default Güvenlik Başlıklarını Kontrol Et
        5. Çıkış
        """)

        choice = input("Bir seçenek seçin" + Fore.CYAN + " (1/2/3/4/5): " + Fore.YELLOW )

        if choice == "1":
            get_domain()
        elif choice == "2":
            get_domain_index()
        elif choice == "3":
            single_scan()                 
        elif choice == "4":
              get_security_headers()      
        elif choice == "5":
            print(Fore.RED + "Çıkış yapılıyor...")
            time.sleep(5)
            break
            
            
init()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g","--guide", action="store_true", help="Yardım sayfasını gösterir")
    args = parser.parse_args()

    if args.guide:
        show_help()
    else:
        main()


