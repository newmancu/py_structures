import unittest
from timed_iterable import TimedSet,TimedList
from time import sleep
from math import ceil

class TestTimedSet(unittest.TestCase):
  file_path = 't1.txt'

  def test_add_maxsize(self):
    self.open_connection()
    maxsize = 20
    N = 105
    ts = TimedSet(1, self.write_to_file, sleeptime=.2, daemon=False, maxsize=maxsize)
    
    for i in range(1,N+1):
      ts.add(str(i))

    ts.stop()
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1

    self.assertEqual(c, ceil(N/maxsize))
    
  def test_add_no_maxsize_1(self):

    self.open_connection()
    N = 105
    ts = TimedSet(1, self.write_to_file, sleeptime=.2, daemon=False)
    
    for i in range(1,N+1):
      ts.add(str(i))

    ts.stop()
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1

    self.assertEqual(c, 1)


  def test_add_no_maxsize_2(self):

    self.open_connection()
    N = 105
    ts = TimedSet(1, self.write_to_file, sleeptime=.2, daemon=False)
    
    for i in range(1,N+1):
      ts.add(str(i))

    self.assertEqual(len(ts), N)
    sleep(.5)
    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1
      self.assertEqual(c, 0)

    sleep(2)
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1
    self.assertEqual(c, 1)
    ts.stop()

  def open_connection(self):
    self.out = open(self.file_path, 'w')

  def close_connection(self):
    self.out.close()

  def write_to_file(self, iterable):
    s = ' '.join(iterable) + '\n'
    self.out.write(s)



class TestTimedList(unittest.TestCase):
  file_path = 't2.txt'

  def test_add_maxsize(self):
    self.open_connection()
    maxsize = 20
    N = 105
    ts = TimedList(1, self.write_to_file, sleeptime=.2, daemon=False, maxsize=maxsize)
    
    for i in range(1,N+1):
      ts.add(str(i))

    ts.stop()
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1

    self.assertEqual(c, ceil(N/maxsize))
    
  def test_add_no_maxsize_1(self):

    self.open_connection()
    N = 105
    ts = TimedList(1, self.write_to_file, sleeptime=.2, daemon=False)
    
    for i in range(1,N+1):
      ts.add(str(i))

    ts.stop()
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1

    self.assertEqual(c, 1)


  def test_add_no_maxsize_2(self):

    self.open_connection()
    N = 105
    ts = TimedList(1, self.write_to_file, sleeptime=.2, daemon=False)
    
    for i in range(1,N+1):
      ts.add(str(i))

    self.assertEqual(len(ts), N)
    sleep(.5)
    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1
      self.assertEqual(c, 0)

    sleep(2)
    self.close_connection()

    with open(self.file_path, 'r') as inp:
      c = 0 
      while inp.readline():
        c += 1
    self.assertEqual(c, 1)
    ts.stop()

  def open_connection(self):
    self.out = open(self.file_path, 'w')

  def close_connection(self):
    self.out.close()

  def write_to_file(self, iterable):
    s = ' '.join(iterable) + '\n'
    self.out.write(s)


if __name__ == '__main__':
  unittest.main()