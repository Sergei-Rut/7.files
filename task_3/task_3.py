from os import listdir
from collections import OrderedDict


def get_files_list():
  files = listdir(".")
  file_list_txt = list(filter(lambda x: x.endswith('.txt'), files))
  return  file_list_txt


def get_dict_sorted():
  files_list = get_files_list()
  data = {}
  for files in files_list:
    with open(files, 'r+', encoding='utf-8') as f:
      count = len(f.readlines())
      f.seek(0)
      data[files] = {'count': count, 'data': f.read()}
      data = OrderedDict(sorted(data.items(), key=lambda x: x[1]['count']))
  return data


def get_destination_file():
  data = get_dict_sorted()
  with open("destination_file.txt","w", encoding='utf-8') as f:
    for key, value in data.items():
      f.write('{}\n'.format(key))
      for val in value.values():
        f.write('{}\n'.format(val))


get_destination_file()









