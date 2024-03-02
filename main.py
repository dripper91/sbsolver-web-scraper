from bs4 import BeautifulSoup
import requests

url = "https://www.sbsolver.com/s/qRtuiof"
answers_page = requests.get(url)
soup = BeautifulSoup(answers_page.text, "html.parser")

new_game_answers = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if ".com/h/" in href:
        answer = href[27:]
        if answer != "":
            new_game_answers.append(answer)

with open('dictionary.txt', 'r', encoding='utf-8') as file:
    existing_words = [line.strip() for line in file]

all_words = set(existing_words + new_game_answers)
sorted_all_words = sorted(all_words)

with open('dictionary.txt', 'w', encoding='utf-8') as file:
    for word in sorted_all_words:
        file.write(f"{word}\n")