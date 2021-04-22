import requests

#1
# response = requests.get("https://www.mes.gov.ge/index.php?lang=geo")
# if 200 <= response.status_code < 300:
#     data = response.text
#     print(data.count('განათლება'))
#     print(data)
# else:
#     print("Error, status code: ", response.status_code)

#2
# def write_photo(response, i):
#     if 200 <= response.status_code < 300:
#         known_extension = True
#         if 'image/jpeg' in response.headers['Content-Type']:
#             file = open(f"image_{i}.jpeg", 'wb')
#         elif 'image/png' in response.headers['Content-Type']:
#             file = open(f"image_{i}.png", 'wb')
#         elif 'image/svg' in response.headers['Content-Type']:
#             file = open(f"image_{i}.svg", 'wb')
#         elif 'image/webp' in response.headers['Content-Type']:
#             file = open(f"image_{i}.webp", 'wb')
#         else:
#             print("Unknown image extension")
#             known_extension = False
#         if known_extension:
#             file.write(response.content)
#             file.close()
#     else:
#         print("Error, status code: ", response.status_code)
#
#
# response = requests.get("https://httpbin.org/image/jpeg")
# write_photo(response, 1)
# response = requests.get("https://httpbin.org/image/png")
# write_photo(response, 2)
# response = requests.get("https://httpbin.org/image/svg")
# write_photo(response, 3)
# response = requests.get("https://httpbin.org/image/webp")
# write_photo(response, 4)

#3
response = requests.get("https://httpbin.org/ip")
with open('my_ip.txt', 'w') as file:
    file.write(response.json()['origin'])