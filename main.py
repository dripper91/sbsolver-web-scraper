from bs4 import BeautifulSoup

with open("answers.html", "r") as answers_page:
    soup = BeautifulSoup(answers_page, "html.parser")

game_answers = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if "com/h" in href:
        start_index = href.find(".com/h/") + len(".com/h/")
        end_index = href.find('/', start_index)
        answer = href[start_index:end_index] if end_index != -1 else href[start_index:]
        if answer != "":
            game_answers.append(answer)

game_answers = list(set(game_answers))
print(game_answers)

