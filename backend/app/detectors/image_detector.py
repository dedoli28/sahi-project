"""Görsel içerikler için yapay zeka üretimi tespit modülü.

Planlanan yaklaşım:
- CNN tabanlı sınıflandırıcı (gerçek vs. GAN/difüzyon kaynaklı görseller)
- Frekans alanı (FFT) analizi ile üretici modellere özgü artefaktların tespiti
- Piksel/doku tutarsızlığı kontrolü

Şu an yalnızca iskelet/placeholder fonksiyon bulunmaktadır; model eğitimi
ve gerçek çıkarım mantığı sonraki aşamada eklenecektir.
"""

from __future__ import annotations


def detect(image_bytes: bytes) -> dict:
    """Bir görselin yapay zeka ile üretilmiş olma olasılığını döndürür.

    Args:
        image_bytes: Yüklenen görselin ham bayt verisi.

    Returns:
        dict: {"is_ai_generated": bool, "confidence": float, "label": str}
    """
    # TODO: Gerçek model çıkarımını burada uygula.
    return {
        "is_ai_generated": False,
        "confidence": 0.0,
        "label": "belirsiz (model henüz eğitilmedi)",
    }
