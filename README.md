# HTTP-Security-Headers-Check
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


