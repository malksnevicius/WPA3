# Vytvorte program, ktorý dokáže spočítať výskyt jednotlivých slov vo vete.
# Použite dáta z adresy:
# https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy3/main/Lekcia6/scratch.txt
import urllib.request
import ssl

if __name__ == "__main__":
    data = str(
        urllib.request.urlopen(
            "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy3/main/Lekcia6/scratch.txt",
            context=ssl._create_unverified_context()
        ).read().decode("utf-8"))
    data = data.replace(",", " ").replace(".", " ").replace("\n", " ")
    data_list = data.split(" ")
    slova_dict = {}
    for word in data_list:
        if slova_dict.get(word, False):
            slova_dict[word] += 1
        else:
            slova_dict[word] = 1    # slova_dict[word] = slova_dict[word] + 1

    print(f"Pocty slov: {slova_dict}")