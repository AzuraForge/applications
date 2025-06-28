# ========== DOSYA: applications/setup.py ==========
from setuptools import setup, find_packages

setup(
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # EN ÖNEMLİ KISIM: Paket kurulduğunda .json dosyasının da kopyalanmasını sağlar
    include_package_data=True, 
    package_data={
        "azuraforge_applications": ["*.json"], # "azuraforge_apps_catalog" -> "azuraforge_applications"
    },
)
