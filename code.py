from bs4 import BeautifulSoup

file_path = r'C:\Users\Nahid\OneDrive\Desktop\CO.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, 'html.parser')

question_divs = soup.find_all('div', class_='questionLi')

filename = "Questions.txt"

for question_div in question_divs:
    serial_number = question_div.h3.text.split('.')[0].strip()
    question_text = ' '.join(question_div.h3.text.split(')')[1].split())
    correct_answer = question_div.find('span', class_='colorGreen').text.split(':')[1].strip()
    options = [li.text.strip() for li in question_div.find('ul', class_='mark_letter').find_all('li')]
    
    selected_option = next((option for option in options if option.startswith(correct_answer + '.')), None)
    
    with open(filename, "a", encoding='utf-8') as f:
        if selected_option:
            f.write(f"({serial_number}) {question_text} Answer: {selected_option}\n")

print(f"Outputs saved to: {filename}")