alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def answer1(text, rotation):  #использует 1 режим
  result = ""
  for letter in text:  #берет letter из text
    print(letter)
    if (alphabet.find(letter) == -1):  #проверяет есть ли буква в алфавите
      result += letter
    else:  #прибавляет введенное количсетво символов к каждому символу в тексте
      result += (alphabet[(alphabet.find(letter) + rotation) % len(alphabet)])
  return result


def answer2(text, rotation):  #использует 2 режим

  result = ""
  for letter in text:
    if (alphabet.find(letter) == -1):
      result += letter
    else:
      result += (alphabet[(alphabet.find(letter) - rotation) % len(alphabet)])
  return result


mode = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(mode))

if mode == 1:  # запуск 1 режима
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + answer1(text, rotation))
elif mode == 2:  # запуск 2 режима
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + answer2(text, rotation))
elif mode == 3:  # запуск 3 режима
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")

