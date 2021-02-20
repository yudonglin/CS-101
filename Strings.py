# Yudong Lin - 2/19/2021

text:str = "X-DSPAM-Confidence: 0.8475"

index:int = text.find(":")+1

floating_point:float = float(text[index:])

print(floating_point)