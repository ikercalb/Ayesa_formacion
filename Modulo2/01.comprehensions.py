'''
Ejercicio 1.
Crear una función, task1, que niegue una lista de numeros dada mediante el uso
de listas de compresión. Por ejemplo:
Dado [1, 2, -3, 4, 5] la salida de la función seria [-1, -2, 3, -4, -5]
'''

def task1(numbers):
  invert = [n * -1 for n in numbers]
  return invert


task1([1, 2, -3, 4, 5])
'''
Ejercicio 2.
Crear una función, task2, que dado un número n y una cadena, ponga en mayusculas los n
primeros números de dicha cadena. Por ejemplo:
Dado n=10 y la cadena "Bienvenidos al curso de Python", devuelva "BIENVENIDOs al curso de Python"
'''

def task2(n, phrase):
  result = phrase[:n].upper() + phrase[n:]
  return result

task2(3, 'holaaaa')
'''
Ejercicio 3.
Crear una función, task3, que dado un número n, devuelva una lista con las potencias de todos sus anteriores numeros hasta ellos mismos.
Por ejemplo:
Dado n=4, devolveria: [1, 2, 4, 3, 9, 27, 4, 16, 64, 256] => [1^1, 2^1, 2^2, 3^1, 3^2, 3^3, 4^1, 4^2, 4^3, 4^4]
'''

def task3(n):
  result = [i**j for i in range(1,n+1) for j in range(1,i+1)]
  return result

print(task3(4))


'''
Check area
''' 
import base64
check = b'JycnCkNoZWNrIHJlc3VsdHMKVGFzayAxOgonJycKcHJpbnQoKQpwcmludCgnIyMjIyMjIyMjIyMjIyMjIyMjIyMnKQpwcmludCgnUHJvYmFuZG8gZWplcmNpY2lvIDEnKQpwcmludCgnLS0tLS0tLS0tLS0tLS0tLS0tLS0nKQoKdGFzazFfbGlzdDAgPSBbMSwgMiwgMywgNCwgNV0KdGFzazFfbGlzdDBfcmVzdWx0ID0gWy0xLCAtMiwgLTMsIC00LCAtNV0KdGFzazFfbGlzdDEgPSBbMCwgLTIsIDMsIC00LCAxMDBdCnRhc2sxX2xpc3QxX3Jlc3VsdCA9IFswLCAyLCAtMywgNCwgLTEwMF0KdGFzazFfbGlzdDIgPSBbMCwgMTAwMCwgLTEwMDAsIDEsIC0xXQp0YXNrMV9saXN0Ml9yZXN1bHQgPSBbMCwgLTEwMDAsIDEwMDAsIC0xLCAxXQoKaWYgKHRhc2sxKHRhc2sxX2xpc3QwKSAhPSB0YXNrMV9saXN0MF9yZXN1bHQpOgogIHByaW50KCdFcnJvciBlbiBlamVyY2ljaW8gMSBjb24gZW50cmFkYTogJykKICBwcmludCh0YXNrMV9saXN0MCkKZWxpZiAodGFzazEodGFzazFfbGlzdDEpICE9IHRhc2sxX2xpc3QxX3Jlc3VsdCk6CiAgcHJpbnQoJ0Vycm9yIGVuIGVqZXJjaWNpbyAxIGNvbiBlbnRyYWRhOiAnKQogIHByaW50KHRhc2sxX2xpc3QxKQplbGlmICh0YXNrMSh0YXNrMV9saXN0MikgIT0gdGFzazFfbGlzdDJfcmVzdWx0KToKICBwcmludCgnRXJyb3IgZW4gZWplcmNpY2lvIDEgY29uIGVudHJhZGE6ICcpCiAgcHJpbnQodGFzazFfbGlzdDIpCmVsc2U6CiAgcHJpbnQoJ0VqZXJjaWNpbyAxIHN1cGVyYWRvIDopJykKCicnJwpDaGVjayByZXN1bHRzClRhc2sgMjoKJycnCnByaW50KCkKcHJpbnQoJyMjIyMjIyMjIyMjIyMjIyMjIyMjJykKcHJpbnQoJ1Byb2JhbmRvIGVqZXJjaWNpbyAyJykKcHJpbnQoJy0tLS0tLS0tLS0tLS0tLS0tLS0tJykKCnRhc2syX2xpc3QwID0gJ0hvbGEgYW1pZ29zLCBxdWUgdGFsIGVzdGFpcycKdGFzazJfbGlzdDBfbiA9IDUKdGFzazJfbGlzdDBfcmVzdWx0ID0gJ0hPTEEgYW1pZ29zLCBxdWUgdGFsIGVzdGFpcycKdGFzazJfbGlzdDEgPSAnVmFtb3MgYSBwcm9iYXIgYWxndW5hcyBjb3NhcycKdGFzazJfbGlzdDFfbiA9IDgKdGFzazJfbGlzdDFfcmVzdWx0ID0gJ1ZBTU9TIEEgcHJvYmFyIGFsZ3VuYXMgY29zYXMnCgppZiAodGFzazIodGFzazJfbGlzdDBfbiwgdGFzazJfbGlzdDApICE9IHRhc2syX2xpc3QwX3Jlc3VsdCk6CiAgcHJpbnQoJ0Vycm9yIGVuIGVqZXJjaWNpbyAyIGNvbiBlbnRyYWRhOiAnKQogIHByaW50KHRhc2syX2xpc3QwKQogIHByaW50KHRhc2syX2xpc3QwX24pCmVsaWYgKHRhc2syKHRhc2syX2xpc3QxX24sIHRhc2syX2xpc3QxKSAhPSB0YXNrMl9saXN0MV9yZXN1bHQpOgogIHByaW50KCdFcnJvciBlbiBlamVyY2ljaW8gMiBjb24gZW50cmFkYTogJykKICBwcmludCh0YXNrMl9saXN0MSkKICBwcmludCh0YXNrMl9saXN0MV9uKQplbHNlOgogIHByaW50KCdFamVyY2ljaW8gMiBzdXBlcmFkbyA6KScpCgoKJycnCkNoZWNrIHJlc3VsdHMKVGFzayAzOgonJycKcHJpbnQoKQpwcmludCgnIyMjIyMjIyMjIyMjIyMjIyMjIyMnKQpwcmludCgnUHJvYmFuZG8gZWplcmNpY2lvIDMnKQpwcmludCgnLS0tLS0tLS0tLS0tLS0tLS0tLS0nKQoKdGFzazNfbjAgPSA0CnRhc2szX24wX3Jlc3VsdCA9IFsxLCAyLCA0LCAzLCA5LCAyNywgNCwgMTYsIDY0LCAyNTZdCnRhc2szX24xID0gMwp0YXNrM19uMV9yZXN1bHQgPSBbMSwgMiwgNCwgMywgOSwgMjddCgppZiAodGFzazModGFzazNfbjApICE9IHRhc2szX24wX3Jlc3VsdCk6CiAgcHJpbnQoJ0Vycm9yIGVuIGVqZXJjaWNpbzMgY29uIGVudHJhZGE6ICcpCiAgcHJpbnQodGFzazNfbjApCmVsaWYgKHRhc2szKHRhc2szX24xKSAhPSB0YXNrM19uMV9yZXN1bHQpOgogIHByaW50KCdFcnJvciBlbiBlamVyY2ljaW8gMyBjb24gZW50cmFkYTogJykKICBwcmludCh0YXNrM19uMSkKZWxzZToKICBwcmludCgnRWplcmNpY2lvIDMgc3VwZXJhZG8gOiknKQo='
eval(compile(base64.b64decode(check),'<string>','exec'))