## Create a virtual environment

Click below for instructions for your shell.

<details>
<summary>POSIX bash/zsh</summary>

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
```
</details>

<details>
<summary>POSIX fish</summary>

```shell
python3 -m venv venv
source venv/bin/activate.fish
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate.fish
```
</details>

<details>
<summary>POSIX csh/tcsh</summary>

```shell
python3 -m venv venv
source venv/bin/activate.csh
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate.csh
```
</details>

<details>
<summary>POSIX PowerShell Core</summary>

```shell
python3 -m venv venv
venv/bin/Activate.ps1
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
venv/bin/Activate.ps1
```
</details>

<details>
<summary>Windows cmd.exe</summary>

```shell
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
venv\Scripts\activate.bat
```
</details>

<details>
<summary>Windows PowerShell</summary>

```shell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
venv\Scripts\Activate.ps1
```
</details>