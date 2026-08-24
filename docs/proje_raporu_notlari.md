# Proje Raporu Notları

Bu dosya, proje başvuru raporu için birlikte hazırlanan taslak metinleri içerir.
Nihai rapora aktarılırken düzenlenmesi/kısaltılması gerekebilir.

## 1.2. Proje Kapsamı ve Yöntemi

Proje, Nsosyal platformunda paylaşılan görsel, video ve ses içeriklerinin yapay
zeka ile üretilip üretilmediğinin tespit edilerek kullanıcıya sade bir "yapay
zeka ile oluşturulmuştur" etiketiyle sunulmasıyla sınırlıdır; öncelik, dijital
okuryazarlığı düşük yaşlı kullanıcıların korunmasıdır. Teknik olarak, görsellerde
CNN tabanlı sınıflandırma ve frekans/artefakt analizi, videoda kare bazlı ve
zamansal tutarlılık incelemesi, seste ise spektrogram tabanlı analiz kullanılarak
çok modlu bir tespit sistemi kurulacaktır. Çalışma, sosyal medyada içerik
güvenilirliğinin platform ve içerik ekonomisinin sürdürülebilirliği için kritik
olması nedeniyle "İçerik Ekonomisi" tematik alanıyla doğrudan ilişkilidir ve
geliştirilecek model ile veri seti, ileride farklı platformlara entegre
edilebilecek bir API'ye dönüşerek gelecekteki çalışmalara zemin hazırlama
potansiyeli taşımaktadır. Proje, fikir düzeyinde kalmayıp analiz sonucunu anlık
gösteren çalışan bir web uygulaması prototipiyle desteklenecektir.

## Sorun Tanımı (istatistik/akademik destekli)

Sosyal medyada yapay zeka ile üretilen içeriklerin hacmi hızla büyümektedir;
deepfake sayısı iki yılda 500 binden 8 milyona çıkmış (DeepStrike), yapay zeka
kaynaklı dolandırıcılık zararının 2027'de 40 milyar dolara ulaşması
beklenmektedir (Deloitte). Bu sorundan en çok etkilenen kesim yaşlı bireylerdir:
bir çalışmada 65 yaş üstü grubun yapay zeka içeriğini tespit doğruluğu %65,5
iken genç yetişkinlerde bu oran %79,8'dir; 2024'te yaşlı bireylere yönelik
dolandırıcılık zararı %43 artışla 4,89 milyar dolara ulaşmıştır (Journal of
Accountancy). Türkiye'de de yapay zeka kaynaklı dezenformasyonun en çok X ve
TikTok üzerinden yayıldığı akademik olarak tespit edilmiştir (TRT Akademi, 2025).

Mevcut çözümler yetersiz kalmaktadır: C2PA/SynthID gibi köken doğrulama
standartları ekran görüntüsü veya yeniden sıkıştırma gibi basit işlemlerle
kolayca silinebilmekte; Meta, YouTube ve TikTok'un etiketleme sistemleri ise
büyük ölçüde kullanıcı beyanına dayandığından içerik genelde ancak yayıldıktan
sonra etiketlenebilmektedir. Bu boşluk, "Sahi" projesinin platforma entegre,
gerçek zamanlı ve kullanıcı odaklı bir tespit sistemi olarak konumlanmasının
temel gerekçesidir.

## Özgün Çözüm

"Sahi", mevcut çözümlerin aksine içeriği paylaşılmadan/yayılmadan önce otomatik
olarak analiz eden, kullanıcı beyanına bağımlı olmayan bir tespit sistemi sunar.
C2PA/SynthID gibi standartlar ekran görüntüsü alındığında meta veriyi
kaybederken, Sahi görsel, video ve ses içeriğini doğrudan piksel/frekans/
spektrogram düzeyinde analiz ettiğinden meta veriye bağımlı değildir; Meta ve
TikTok gibi platformların içerik yayıldıktan sonra uyguladığı geriye dönük
etiketlemenin aksine, tespit ve etiketleme yayın anında gerçekleşir. Bu
yönüyle Sahi, ticari araçların laboratuvarda %96 iken gerçek dünyada %45-50'ye
düşen doğruluk sorununu, sürekli güncellenen ve platforma özel eğitilen bir
model ile aşmayı hedefler.

Projenin yerli bileşeni, modelin Türkçe sosyal medya içeriği ve yerli üretici
yapay zeka araçlarının bıraktığı izler üzerinden eğitilmesi ile doğrudan yerli
bir sosyal medya platformu olan Nsosyal'e entegre edilmesidir; bu da global
genel amaçlı tespit araçlarının yakalayamadığı yerel içerik örüntülerine karşı
daha yüksek isabet sağlar. Sistem, yaşlı kullanıcılar için sade dil ve görsel
uyarılarla desteklenen arayüzüyle de mevcut çözümlerden ayrışır ve piyasada
doğrudan uygulanabilir, çalışan bir prototiple desteklenir.

## Kaynakça (araştırma sırasında bulunanlar)

- Deepfake Statistics [2026]: Growth, Fraud & Detection Data — https://app.stationx.net/articles/deepfake-statistics
- Elder fraud rises as scammers use AI — Journal of Accountancy — https://www.journalofaccountancy.com/issues/2026/apr/elder-fraud-rises-as-scammers-use-ai/
- Find Out How to Protect Yourself Against AI Scams — AARP — https://www.aarp.org/money/scams-fraud/detecting-ai-fraud/
- Hear Us, then Protect Us: Navigating Deepfake Scams and Safeguard Interventions with Older Adults through Participatory Design — ACM CHI 2025 — https://dl.acm.org/doi/full/10.1145/3706598.3714423
- C2PA Adoption Status 2026: Content Credentials, OpenAI & Google — https://www.eyesift.com/faq/c2pa-content-credentials-2026-cryptographic-provenance-adoption/
- Cross-Platform AI Content Labeling Requirements 2026 — https://www.auditsocials.com/blog/cross-platform-ai-content-labeling-requirements-2026-meta-google-tiktok-youtube-comparison
- Methods and Trends in Detecting AI-Generated Images: A Comprehensive Review (arXiv:2502.15176) — https://arxiv.org/html/2502.15176
- Türkiye'de Yapay Zekânın Dezenformasyon Karnesi — TRT Akademi — https://dergipark.org.tr/tr/pub/trta/article/1557154
- Can Older Adults Detect AI-Generated Content? — The CareSide — https://www.thecareside.com.au/post/ai-content-detection-study/
- Detection of AI-Generated Images: A Mixed Methods Study on Age-Related Differences — Innovation in Aging — https://academic.oup.com/innovateage/article/8/Supplement_1/1301/7939921
