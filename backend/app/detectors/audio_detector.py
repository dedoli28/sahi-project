"""Ses içerikleri için yapay zeka üretimi (ör. klonlanmış ses) tespit modülü.

Planlanan yaklaşım:
- Spektrogram tabanlı özellik çıkarımı (librosa)
- Sentetik ses üretimine özgü akustik imzaların sınıflandırılması
"""

from __future__ import annotations


def detect(audio_bytes: bytes) -> dict:
    """Bir ses kaydının yapay zeka ile üretilmiş olma olasılığını döndürür.

    Args:
        audio_bytes: Yüklenen ses dosyasının ham bayt verisi.

    Returns:
        dict: {"is_ai_generated": bool, "confidence": float, "label": str}
    """
    # TODO: Spektrogram çıkarımı + sınıflandırma mantığını burada uygula.
    return {
        "is_ai_generated": False,
        "confidence": 0.0,
        "label": "belirsiz (model henüz eğitilmedi)",
    }
