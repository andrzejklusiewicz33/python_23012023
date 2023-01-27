from domain import *
def get_all():
    data = []
    data.append(Product(1, "Bulbulator", 1234, "Urządzenie robiące bul bul", 10))
    data.append(Product(2, "Przyczłap do bulbulatora", 100, "Takie teges co wiesz, no ten to tam", 0))
    data.append((Product(3, "Wihajster z dzyndzlem", 20, "Na śróbki lub na gwoździe, zależy czy tak czy nie", 50)))
    return data