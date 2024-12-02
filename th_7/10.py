print("Nguyễn Danh Ánh")
print("235752021610023")
def find_longest_words(text):
  words = text.split()
  max_length = len(max(words, key=len))
  longest_words = [word for word in words if len(word) == max_length]
  return longest_words

text = ("Đây là một đoạn văn bản mẫu để chúng ta thử nghiệm chương trình tìm kiếm từ dài nhất.")
longest = find_longest_words(text)
print("Các từ dài nhất là:", longest)
