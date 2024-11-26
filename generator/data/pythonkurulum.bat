@echo off
setlocal enabledelayedexpansion
echo Bilgisayar mimarisi kontrol ediliyor...
set "ARCHITECTURE="
if "%PROCESSOR_ARCHITECTURE%" == "AMD64" (
    set "ARCHITECTURE=64"
) else if "%PROCESSOR_ARCHITECTURE%" == "x86" (
    set "ARCHITECTURE=32"
) else (
    echo Mimari algılanamadı. Varsayılan olarak 32-bit seçiliyor...
    set "ARCHITECTURE=32"
)

if "%ARCHITECTURE%" == "64" (
    set "PYTHON_URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"
    echo 64-bit mimari algılandı. Python 64-bit sürümü indirilecek.
) else (
    set "PYTHON_URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6.exe"
    echo 32-bit mimari algılandı. Python 32-bit sürümü indirilecek.
)

set "PYTHON_INSTALLER=python-installer.exe"
echo Python indiriliyor...
curl -o "%PYTHON_INSTALLER%" "%PYTHON_URL%"
if not exist "%PYTHON_INSTALLER%" (
    echo Python indirme başarısız. Lütfen internet bağlantınızı kontrol edin.
    exit /b
)
echo Python kurulumu başlatılıyor...
start /wait "" "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1
if %ERRORLEVEL% neq 0 (
    echo Python kurulumu başarısız oldu.
    exit /b
)

echo Python başarıyla yüklendi. Versiyon kontrol ediliyor...
python --version
if %ERRORLEVEL% neq 0 (
    echo Python yüklendi ancak komut algılanmadı. PATH değişkeninizi kontrol edin.
    exit /b
)
echo Python başarıyla yüklendi ve kullanıma hazır!
del "%PYTHON_INSTALLER%"
pause
