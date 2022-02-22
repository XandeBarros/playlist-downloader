
# Playlist Downloader

Estava precisando baixar uma playlist do youtube, para o meu celular em formato '.mp3' e como não queria fazer isso uma a uma acabei fazendo esse script em Python para isso.

Faço o uso da Lib Pytube (Não nativa) e da Lib os (Nativa), para não misturar com as outras Libs do meu computador, acabei fazendo um ambiente virtual,  a versão do python usada foi a 3.9.4



## Modo de Usar

### Criando Ambiente Virtual

```powershell
py -m venv pytube-venv
```

### Ativando Ambiente Virtual

Windows (PowerShell)

```powershell
.\pytube-venv\Scripts\Activate.ps1
```

Agora basta instalar a lib pytube com 
```powershell
pip install pytube
```

e rodar o script main.py
```powershell
python main.py
```
