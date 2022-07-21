import threading as thr
from time import time, sleep
from typing import Iterable

class TimedIterable:
  saveLook: thr.Lock
  addLook: thr.Lock
  _iter: Iterable  

  def __init__(self, timeout: float, savefunc, *args, sleeptime=1, maxsize=None, **kwargs) -> None:
    self.saveLook = thr.Lock()
    self.addLook = thr.Lock()
    self.maxsize = maxsize
    self.timeout = timeout
    self.savefunc = savefunc
    self.start_time = time()
    self.is_running = False
    self.sleeptime = sleeptime

    if kwargs.get('run', True):
      self.run(daemon=kwargs.get('daemon',True))

  def add(self, item):
    with self.addLook:
      self._iter.add(item)
      if self.maxsize is not None and len(self._iter) >= self.maxsize:
        self.save()
      self.start_time = time()
  
  def save(self):
    with self.saveLook:
      if self._iter:
        self.savefunc(self._iter)
        self._iter.clear()
      self.start_time = time()
    
  def _run(self):
    self.is_running = True
    while self.is_running:
      if (time() - self.start_time) >= self.timeout:
        self.save()
      else:
        sleep(self.sleeptime)

  def stop(self):
    self.is_running = False
    self.save()

  def __del__(self):
    self.stop()

  def __len__(self):
    with self.saveLook:
      return len(self._iter)

  def run(self, daemon=True):
    thr.Thread(target=self._run, daemon=daemon).start()


class TimedSet(TimedIterable):
  def __init__(self, timeout: float, savefunc, *args, sleeptime=1, maxsize=None, **kwargs) -> None:
    self._iter = set()
    super().__init__(timeout, savefunc, *args, sleeptime=sleeptime, maxsize=maxsize, **kwargs)


class TimedList(TimedIterable):
  def __init__(self, timeout: float, savefunc, *args, sleeptime=1, maxsize=None, **kwargs) -> None:
    self._iter = list()
    super().__init__(timeout, savefunc, *args, sleeptime=sleeptime, maxsize=maxsize, **kwargs)

  def add(self, item):
    with self.addLook:
      self._iter.append(item)
      if self.maxsize and len(self._iter) >= self.maxsize:
        self.save()
      self.start_time = time()
