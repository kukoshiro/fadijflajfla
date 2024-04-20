import pickle
from operator import itemgetter

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)


end_data = []
view_count = 0
for text in data[1:]:
    title, views, _ = text.split('\n')
    number = views.split(' ')[0]
    if 'тыс' in views:
        views = int(float(number.replace(',', '.')) * 1000)
    else:
        views = int(number)
    view_count += views
    end_data.append([title, views])

end_data = sorted(end_data, key=itemgetter(1), reverse=True)
print(view_count)
file_data = '\n'.join([i[0] + ' | ' + str(i[1]) for i in end_data])
with open('end.txt', 'w', encoding='utf-8') as f:
    f.write(file_data)