# Desafio de projeto - Descomplicando a criação de pacotes
---
<!-- Links usados -->
[Pip]: https://pip.pypa.io/en/stable/
[Pypi]: https://pypi.org
[requisitos]: pacote_pacman_exemplo\requirements.txt
[readme]: pacote_pacman_exemplo\README.md
[setup_pacote]: template_basico_de_um_pacote/setup.py
[pacman-repositorio]: https://github.com/Lyarkh/Pacman
<!---->

Neste primeiro desafio do Bootcamp, foi explicado como desenvolver um pacote e publicar ele para que outros usuários possam usar.

O template de um pacote padrão encotra-se [aqui](template_basico_de_um_pacote/).
O projeto usado de exemplo é uma recriação do jogo [`pacman`](#sobre-pacman).




### Passos de criação do pacote
---

<details>
<summary>Passo 1: Criação do projeto</summary>

- Acrescentar o [README.md][readme] para o projeto contendo:

    - sobre o projeto
    - como instalar
    - como usar e exemplo

- Acrescentar [requirements][requisitos] caso seu pacote dependa de outro pacote existente que seja necessário instalar

- Acrescentar o arquivo [setup.py][setup_pacote].

</details>

<details>
<summary>Passo 2: Criação das distribuções</summary>

- Para subir o pacote, é necessário criar as distribuições do pacote. Seja ela distribução binária ou distribuição de código fonte.

- Não é necessário criar as duas distribuições, mais é o recomendado.

- É necessário fazer algumas instalações para depois criar as distribuições.

    - Entre na pasta pelo promp onde está o pacote e rode os códigos no proprio prompt.

    ```bash
        python -m pip install --upgrade pip
        python -m pip install --user twine
        python -m pip install --user setuptools
    ```

- Em seguida, use o comando a seguir para criar as duas distribuições:

```bash
    python setup.py sdist bdist_wheel
```

</details>

<details>
<summary>Passo 3: Publicando pacote</summary>

Para publicar  o pacote no [Pypi].

- Crie uma conta e verifique o email.
- Depois rode o seguinte código pelo prompt na pasta do pacote. 

```bash
    python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```


</details>


---
<div  id='sobre-pacman'>

<details> 
<summary>Repositório do pacman </summary>

> Para saber mais sobre o projeto que foi usado como exemplo na criação de pacotes. Ele pode ser encontrado [Aqui!][pacman-repositorio]
</details>

