with open('D:\\Testy\\site.html', 'w') as output_file:
    top_part = ""
    output_file.write(top_part)
    title = None
    top_code = f"<!DOCTYPE html>\n<html>\n<head>\n   <title>"
    html_output = "</title>\n<body>\n"
    while True:
        input_list = input().split()
        if input_list[0] == 'h1':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'h2':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'h3':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'h4':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'h5':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'h6':
            html_output += f"<{input_list[0]}> {input_list[1]} </{input_list[0]}>"
        elif input_list[0] == 'title':
            title = input_list[1]
        elif input_list[0] == 'p':
            html_output += f"<p>{input_list[1]}</p>\n"
        elif input_list[0] == 'div':
            html_output += f"<div>{input_list[1]}</div>\n"
        elif input_list[0] == "exit":
            break
    html_output += "</body>\n</html>"
    output_file.write(top_code + title + html_output)

