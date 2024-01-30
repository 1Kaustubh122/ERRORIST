# # import fnvfd
# from pydub import AudioSegment

# import wave



import re
from gradio_client import Client

client = Client("https://bagus-speaker-verification-demo.hf.space/--replicas/xiuli/")
result = client.predict(
		"output.wav",	   # str (filepath on your computer (or URL) of file) in 'Speaker #1' Audio component
		"output2.wav",	# str (filepath on your computer (or URL) of file) in 'Speaker #2' Audio component
		api_name="/predict"
)
result = str(result)


line = re.sub(r'<.*?>', '', result)

lines = line.split('\n')

lines = [line.strip() for line in lines if line.strip()]

Percentage_Matched = lines[1]

print(Percentage_Matched)