from mpi4py import MPI
import mmh3
from functools import reduce
 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()
size = comm.Get_size()

workers = [i for i in range(size)]

re_map = []

def mapper(data_chunks):
   text = data_chunks.split(" ")
   mapping = [(i, 1) for i in text]
   partition(mapping=mapping)


def partition(mapping):
   for i, pair in enumerate(mapping):
      word = pair[0]
      parti_id = (mmh3.hash(word) % 3) 
      if (parti_id != rank):
         print(f"Sending word {word} from {rank} to {parti_id}")
         comm.send(pair, dest=parti_id)
      else: 
         print(f"Rank {rank} re-append {word}")
         re_map.append(pair)
      if i == len(mapping) - 1:
         for j in workers:
            if (j == rank):
               continue
            print(f"Rank {rank} sending 1 to {j}")
            comm.send(1, dest=j)

   for i in workers:
      if (i == rank):
         continue
      running = True
      while running:
         data = comm.recv(source=i)
         if data != 1:
            re_map.append(data)
            continue
         running = False
   shuffle()

def get_word(e):
   return e[0]

def shuffle():
   re_map.sort(key=get_word)
   print(re_map)

def accumulate_counts(acc, item):
   word, count = item 
   acc[word] = acc.get(word, 0) + count
   return acc

def reducer():
   word_count = reduce(accumulate_counts, re_map, {})
   print(word_count)
   return word_count

def remove_symbol(text:str):
   symbol = ".?,!@#$%^&*()_+=[]"
   word_without_sym = str.maketrans("-"," ",symbol)
   text = text.translate(word_without_sym)
   text = text.replace("\n", " ")
   return text

with open("WordCount.txt", "w") as f:
   pass
print(f"This is rank: {rank}")
filePath = f"text{rank + 1}.txt"
word_count = []
with open(filePath, "r") as f:
   mapper(remove_symbol(f.read()))
   word_count = reducer()

with open("WordCount.txt", "a") as f:
   for i in word_count:
      text = f"{i} : {word_count[i]}\n"
      f.write(text)
