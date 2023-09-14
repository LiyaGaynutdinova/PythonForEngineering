# Export požadávků 
## Pip

Chcete-li exportovat požadavky na moduly pro svůj kód Pythonu pomocí `pip`, můžete postupovat podle následujících kroků:

1. Aktivujte prostředí Pythonu nebo virtuální prostředí, ve kterém je váš kód umístěn. Tento krok je nepovinný, ale doporučuje se, abyste zajistili zachycení konkrétních modulů používaných ve vašem projektu.

2. Otevřete rozhraní příkazového řádku nebo terminál.

3. Přejděte do adresáře obsahujícího váš kód v jazyce Python.

4. Spusťte následující příkaz pro vygenerování souboru requirements.txt, který obsahuje seznam všech modulů a jejich verzí použitých ve vašem kódu:
   ```
   pip freeze > requirements.txt
   ```

   Tento příkaz vygeneruje soubor requirements.txt v aktuálním adresáři.

5. Soubor requirements.txt bude obsahovat seznam názvů a verzí modulů, každý na samostatném řádku. Například:
   ```
   numpy==1.21.0
   pandas==1.3.0
   matplotlib==3.4.3
   ```

   Tyto verze modulů odrážejí verze nainstalované ve vašem prostředí v době spuštění příkazu.

Vygenerovaný soubor requirements.txt můžete sdílet s ostatními nebo jej použít k vytvoření stejného prostředí jinde. Umožňuje ostatním nainstalovat požadované moduly a jejich konkrétní verze pomocí následujícího příkazu:
```
pip install -r requirements.txt
```

## Conda

Chcete-li exportovat požadavky na moduly pro kód Pythonu pomocí Condy, můžete postupovat podle následujících kroků:

1. Aktivujte prostředí Conda nebo vytvořte nové prostředí, ve kterém se nachází váš kód. Tento krok je nepovinný, ale doporučuje se, abyste zajistili zachycení konkrétních modulů používaných ve vašem projektu.

2. Otevřete rozhraní příkazového řádku nebo terminál.

3. Přejděte do adresáře obsahujícího váš kód v jazyce Python.

4. Spusťte následující příkaz pro vygenerování souboru environment.yml, který obsahuje seznam všech balíčků Conda a jejich verzí použitých ve vašem kódu:
   ```
   conda env export > environment.yml
   ```

   Tento příkaz vygeneruje soubor environment.yml v aktuálním adresáři.

5. Soubor environment.yml bude obsahovat reprezentaci prostředí Conda ve formátu YAML, včetně názvu, kanálů, závislostí a jejich verzí. Například:
   ```yaml
   name: myenv
   channels:
     - defaults
   dependencies:
     - python=3.9
     - numpy=1.21.0
     - pandas=1.3.0
     - matplotlib=3.4.3
   ```

   Tyto verze balíčků odpovídají verzím nainstalovaným v prostředí Conda v době spuštění příkazu.

Vygenerovaný soubor environment.yml můžete sdílet s ostatními nebo jej použít k vytvoření stejného prostředí jinde. Umožňuje ostatním vytvořit prostředí Conda s požadovanými balíčky a jejich konkrétními verzemi pomocí následujícího příkazu:
```
conda env create -f environment.yml
```