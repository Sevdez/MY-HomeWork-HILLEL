def lchain(*iterables):
  gl = []
  for elem in iterables:
    gl.extend(elem)
  return gl

assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]