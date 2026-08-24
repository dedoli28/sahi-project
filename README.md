# Sahi

Yapay zeka ile üretilen görsel, video ve ses içeriklerini tespit edip kullanıcıya sade bir "yapay zeka ile oluşturulmuştur" etiketiyle sunan, Nsosyal platformuna entegre çalışacak sistemin prototipi.

## Teknoloji Yığını (planlanan)

- **Backend:** Python, FastAPI
- **Görsel tespiti:** CNN tabanlı sınıflandırıcı + frekans/artefakt analizi (PyTorch, OpenCV, Pillow)
- **Video tespiti:** Kare bazlı analiz + zamansal tutarlılık kontrolü
- **Ses tespiti:** Spektrogram tabanlı özellik çıkarımı (librosa)
- **Frontend:** (henüz başlanmadı — web arayüzü)

## Klasör Yapısı

```
sahi-project/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI giriş noktası
│   │   ├── api/routes.py      # API uç noktaları
│   │   └── detectors/         # görsel/video/ses tespit modülleri
│   ├── tests/
│   └── requirements.txt
├── frontend/                  # web arayüzü (planlanıyor)
├── data/                      # veri seti (raw/processed) — büyük dosyalar repoya eklenmez
├── notebooks/                 # model deneme / eğitim defterleri
└── docs/                      # proje raporu notları
```

## Kurulum (backend)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Sunucu ayağa kalktığında `http://127.0.0.1:8000/health` adresinden kontrol edebilirsiniz.

## GitHub'a Yükleme

Bu klasör henüz bir git deposu değil. Terminalde bu klasörün içinde şu adımları izleyin:

```bash
git init
git add .
git commit -m "İlk commit: proje iskeleti"
```

Sonra GitHub'da boş bir repo oluşturup (README/gitignore eklemeden) şu komutlarla bağlayın:

```bash
git remote add origin https://github.com/<kullanici-adiniz>/sahi.git
git branch -M main
git push -u origin main
```

Bundan sonra geliştirme yaptıkça düzenli commit atmayı unutmayın — jüri commit geçmişine bakacak.
