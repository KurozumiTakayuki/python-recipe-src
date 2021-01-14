from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()

with open("tmp.txt", mode='rb') as f:
    for b in f:
        detector.feed(b)
        if detector.done:
            break
 
detector.close()
print(detector.result)