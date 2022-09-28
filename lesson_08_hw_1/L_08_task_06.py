import random

def pemrtuate():
    text_fynal = []

    texts = str(input('Введите предложение: \n >>> '))
    texts = texts.split()

    for text in texts:
        text_list = []
        for simbol in text:
            text_list.append(simbol)

        first_simbol = text_list[0]
        last_simbol = text_list[len(text_list) - 1]
        a = ""
        del text_list[0]
        del text_list[len(text_list) - 1]

        while len(text_list) > 0:
            b = text_list[:3]
            random.shuffle(b)
            a += "".join(b)
            del text_list[:3]


        ok_text = first_simbol + a + last_simbol
        text_fynal.append(ok_text)
        return (' '.join(text_fynal))

print(pemrtuate())