
with open('test_mq_message.json', 'rt', encoding='utf-8') as fin:
  with open('temp.json', 'wt', encoding='utf-8') as fout:
    for line in fin:
      fout.write(line.replace('6046', 'data'))


