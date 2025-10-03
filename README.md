# JWT Implementation Test Results

## 1\. Login exitoso 

![Login Exitoso](https://github.com/JoaquiinAguilar/JWT-DJANGO/blob/main/images/curl-login.png?raw=true)

Se realiza la petición **POST** a la ruta `/api/token/` enviando las credenciales del usuario.

```bash
curl -X POST http://127.0.0.1:8080/api/token/ -H "Content-Type: application/json" -d '''{"username":"admin","password":"admin123"}'''
```

**Respuesta:**

El servidor responde exitosamente con un **token de refresco** y un **token de acceso**.

```json
{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1OTU1MzYxOCwiaWF0IjoxNzU5NDY3MjE4LCJqdGkiOiI4NzE3OGQzMTJiNTg0MjlmODA5YTYxMTUwMDM3M2VmZiIsInVzZXJfaWQiOiIxIn0.Nc5q3ksaFFtT7rwcIzz1snyPeZD9fDjJnU03E2MPJ-s","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NDcwODE4LCJpYXQiOjE3NTk0NjcyMTksImp0aSI6IjE4NzRhZTlkM2MwMDRlNjY5NmNkOWI3ZTc5MjgwMGMxIiwidXNlcl9pZCI6IjEifQ.XWs0tm_ps0FLpwuqCrB_A1AL5zbhh22SrgGl5BSIJig"}
```

-----

## 2\. Acceso a ruta protegida 🔐

![Acceso Ruta Protegida](https://github.com/JoaquiinAguilar/JWT-DJANGO/blob/main/images/curl-token.png?raw=true)

Se realiza la petición **GET** a la ruta `/api/protegida/` utilizando el **token de acceso** en el encabezado `Authorization`.

```bash
curl http://127.0.0.1:8080/api/protegida/ -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NDcwODE4LCJpYXQiOjE3NTk0NjcyMTksImp0aSI6IjE4NzRhZTlkM2MwMDRlNjY5NmNkOWI3ZTc5MjgwMGMxIiwidXNlcl9pZCI6IjEifQ.XWs0tm_ps0FLpwuqCrB_A1AL5zbhh22SrgGl5BSIJig"
```

**Respuesta:**

El servidor valida el token y concede el acceso, devolviendo la información solicitada.

```json
{"message":"¡Acceso autorizado!","user":"admin","email":"admin@example.com"}
```

-----

## 3\. Error al intentar acceder sin token 🚫

![Acceso Denegado](https://github.com/JoaquiinAguilar/JWT-DJANGO/blob/main/images/curl-notToken.png?raw=true)

Se realiza la petición **GET** a la misma ruta protegida, pero esta vez **sin** proporcionar el token de autorización.

```bash
curl http://127.0.0.1:8080/api/protegida/
```

**Respuesta:**

El servidor deniega el acceso y responde con un error de autenticación, como es esperado.

```json
{"detail":"Authentication credentials were not provided."}
```