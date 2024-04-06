from bs4 import BeautifulSoup

file_path = r'C:\Users\nahid\Desktop\CO.txt' #replace your filepath here

with open(file_path, 'r', encoding='utf-8') as file: #replace your file encoding here
    html_code = file.read() #read the file

soup = BeautifulSoup(html_code, 'html.parser') #parse the html code

question_divs = soup.find_all('div', class_='questionLi') #find all divs with class questionLi

filename = "Questions.txt" #replace your filename here

for question_div in question_divs: #loop through all divs
    serial_number = question_div.h3.text.split('.')[0].strip() #get the serial number
    question_text = ' '.join(question_div.h3.text.split(')')[1].split()) #get the question text
    correct_answer = question_div.find('span', class_='colorGreen').text.split(':')[1].strip() #get the correct answer
    options = [li.text.strip() for li in question_div.find('ul', class_='mark_letter').find_all('li')] #get all options
    
    selected_option = next((option for option in options if option.startswith(correct_answer + '.')), None) #get the selected option
    
    with open(filename, "a", encoding='utf-8') as f: #replace your file encoding here
        if selected_option: #if selected option is not None
            f.write(f"({serial_number}) {question_text} Answer: {selected_option}\n") #write to file

print(f"Outputs saved to: {filename}") #print the output filename