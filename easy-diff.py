# originally written by Satoru Nakamura, https://github.com/nakamura196/koui
# editted for local environment by Shiyuu Shimomura


from koui.api import KouiAPIClient as kac


print('output files are generated to current directory.')

name_1 = input('please enter the first text name. ')
name_input1 = input('please enter the first input file path. ')

name_2 = input('please enter the second text name. ')
name_input2 = input('please enter the second input file path. ')

f1 = open(name_input1, 'r')
f2 = open(name_input2, 'r')

text_1 = f1.read()
text_2 = f2.read()

print('now processing...')

# output xml file
soup_xml = kac.convert(name_1, text_1, name_2, text_2, 'xml')
path_xml = 'out.xml'
with open(path_xml, 'w', encoding='utf-8') as f_xml:
    f_xml.write(str(soup_xml))

# output html file
soup_html = kac.convert(name_1, text_1, name_2, text_2, 'html')
path_html = 'out.html'
with open(path_html, 'w', encoding='utf-8') as f_html:
    f_html.write(str(soup_html))

print('still continueing...')

# calculate Levenshtein distance as 'dintance.csv'
res = kac.compare(path_xml)
df = kac.convertJson2Df(res)
df.to_csv('distance.csv')

print('process ends:')
print('out.xml, out.html and distance.csv are generated.')