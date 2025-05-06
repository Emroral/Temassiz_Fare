# Temassiz_Fare

👋 El Hareketleriyle Fare Kontrolü (Hand Tracking Mouse Control)
Bu proje, Mediapipe ve PyAutoGUI kullanarak el hareketleriyle bilgisayar faresini kontrol etmenizi sağlar. İşaret parmağınızı (landmark 8) hareket ettirerek fare imlecini kontrol edebilir, baş parmağınız (landmark 4) ile işaret parmağınızı birleştirerek tıklama işlemi yapabilirsiniz.

🚀 Özellikler
Gerçek zamanlı el izleme

Fare imlecini işaret parmağıyla kontrol etme

Baş parmak ve işaret parmağı yakınlaştığında otomatik tıklama

Ekran çözünürlüğüne otomatik uyum

🛠️ Gereksinimler
Aşağıdaki Python kütüphaneleri gereklidir:
pip install opencv-python mediapipe pyautogui


🔧 Kurulum ve Kullanım
Bu kodu bir .py dosyasına yapıştırın (örneğin: hand_mouse_control.py)

Gerekli kütüphaneleri yükleyin.

Uygulamayı çalıştırın:
python hand_mouse_control.py

Elinizi kameraya gösterin. İşaret parmağınızı hareket ettirerek imleci kontrol edin. Baş parmak ile işaret parmağını birleştirdiğinizde tıklama gerçekleşir.

⚠️ Notlar
Bu uygulama harici kamera veya dizüstü bilgisayarın yerleşik kamerasıyla çalışabilir.

Elinizin net görünmesi için iyi aydınlatılmış bir ortam tercih edin.

Çoklu monitör kullanıyorsanız ekran koordinatları farklı davranabilir.

