# Guestbook Application

Guestbook - это простое веб-приложение, которое позволяет пользователям оставлять сообщения с именем и комментарием. Это приложение состоит из двух компонент:

- **Frontend**: Статические файлы, обслуживаемые Nginx.
- **Backend**: Flask приложение для обработки запросов и взаимодействия с базой данных MongoDB.

## Требования

Для запуска Guestbook на вашей системе должны быть установлены следующие компоненты:

- Docker: Для создания и запуска контейнеров с приложением.
- Minikube: Для локального развертывания Kubernetes кластера.
- kubectl: Для управления Kubernetes кластером.

## Установка зависимостей

### Установка Docker

```bash
# Установка Docker
sudo pacman -S docker

# Запуск службы Docker
sudo systemctl start docker

# Добавление пользователя в группу docker (чтобы не использовать sudo при работе с Docker)
sudo usermod -aG docker $USER

# Перезагрузка после изменений
sudo systemctl restart docker
```

### Установка Minikube и kubectl

```bash
# Установка kubectl
sudo pacman -S kubectl

# Установка Minikube
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

# Запуск Minikube
minikube start
```

## Запуск приложения Guestbook

### Шаг 1: Сборка Docker образов

```bash
# Сборка Docker образа для backend
docker build -t guestbook-backend ./backend

# Сборка Docker образа для frontend
docker build -t guestbook-frontend ./frontend
```

### Шаг 2: Запуск в Kubernetes с помощью Minikube

```bash
# Применение манифестов Kubernetes
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/backend-service.yaml
kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/frontend-service.yaml
```

### Шаг 3: Доступ к приложению

```bash
# Получение URL frontend сервиса
minikube service frontend-service --url
```

Откройте полученный URL в браузере для доступа к приложению Guestbook.

## Остановка и очистка

### Остановка Minikube кластера

```bash
minikube stop
```

### Очистка ресурсов Kubernetes

```bash
kubectl delete deployment guestbook-backend
kubectl delete service backend-service
kubectl delete deployment guestbook-frontend
kubectl delete service frontend-service
```

## Дополнительная информация

- `backend/`: Каталог с файлами для создания Docker образа backend.
- `frontend/`: Каталог с файлами для создания Docker образа frontend.
- `kubernetes/`: Каталог с манифестами Kubernetes для развертывания backend и frontend.

### Объяснение:

1. **Заголовок и описание**: Вводная часть, описывающая приложение Guestbook и его компоненты.
2. **Требования**: Перечисление необходимых для запуска приложения компонентов и инструкции по их установке.
3. **Установка зависимостей**: Подробные инструкции по установке Docker, Minikube и kubectl на Arch Linux.
4. **Запуск приложения Guestbook**:
   - **Шаг 1**: Инструкции по сборке Docker образов для backend и frontend компонент.
   - **Шаг 2**: Инструкции по развертыванию приложения в Kubernetes с использованием Minikube.
   - **Шаг 3**: Инструкции по доступу к приложению через полученный URL frontend сервиса.
5. **Остановка и очистка**: Инструкции по остановке Minikube кластера и удалению развернутых ресурсов Kubernetes.
6. **Дополнительная информация**: Уточнение структуры проекта с каталогами `backend/`, `frontend/` и `kubernetes/`, где хранятся соответствующие файлы для Docker сборки и манифесты Kubernetes.
