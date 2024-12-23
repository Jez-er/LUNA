# Команди для взаємодії з проєктом

## Віртуальне середовище

### Створення

```shell
python -m venv .venv
```

### Активація на Windows

```shell
.venv\Scripts\activate
```

### Активація на Mac/Linux

```shell
source .venv/bin/activate
```

---

## Python модулі

### Створення/оновлення requirements.txt

```shell
pip freeze > requirements.txt
```

### Всановлення модулів з requirements.txt

```shell
pip install -r requirements.txt
```
