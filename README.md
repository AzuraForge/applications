# AzuraForge: Resmi Uygulama Kataloğu

Bu depo, AzuraForge platformu tarafından resmi olarak desteklenen ve test edilen uygulama eklentilerinin bir listesini içeren basit bir **veri paketidir**.

## 🎯 Ana Sorumluluklar

*   **`official_apps.json`:** Platformdaki `Dashboard` arayüzünün, hangi eklentilerin "resmi" olduğunu bilmesini sağlayan bir JSON dosyası içerir. Bu dosya, eklentinin adı, açıklaması ve GitHub deposu gibi meta verileri barındırır.
*   Bu depo, `api` servisi tarafından bir bağımlılık olarak kullanılır. API, bu paketin içindeki `official_apps.json` dosyasını okuyarak, `worker` tarafından keşfedilen pipeline'ları zenginleştirir.

Bu yapı, UI'da gösterilecek bilgilerin, worker veya uygulama kodundan bağımsız, merkezi bir yerde yönetilmesini sağlar.

---

## 🏛️ Ekosistemdeki Yeri

Bu veri paketi, AzuraForge ekosisteminin bir parçasıdır. Projenin genel mimarisini, vizyonunu ve geliştirme rehberini anlamak için lütfen ana **[AzuraForge Platform Dokümantasyonuna](https://github.com/AzuraForge/platform/tree/main/docs)** başvurun.

---

## 🛠️ Geliştirme

Bu bir uygulama veya servis değil, bir veri paketidir. İçeriğini güncellemek için `src/azuraforge_applications/official_apps.json` dosyasını düzenlemeniz yeterlidir. Yeni bir resmi uygulama eklendiğinde bu dosyaya yeni bir giriş yapılır.